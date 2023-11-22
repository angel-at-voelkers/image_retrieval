import argparse
import sys
from urllib import parse
from xml.etree import ElementTree

import requests
from requests import utils

color_ok = "\033[92m"
color_warn = "\033[93m"
color_fail = "\033[91m"
color_end = "\033[00m"
rendition_widths = (640, 750, 828, 1080, 1200, 1440, 1920)


class Config:
    def __init__(
        self,
        lh_host: str = None,
        uc_host: str = None,
        vercel_host: str = None,
        file: str = None,
        bucket: str = None,
        fetch_lh: bool = False,
        fetch_uc: bool = False,
        fetch_vercel_image_service: bool = True,
        fail_on_error: bool = True,
        verbose: bool = True,
    ):
        super().__init__()
        self.lh_host = lh_host
        self.uc_host = uc_host
        self.vercel_host = vercel_host
        self.file = file
        self.bucket = bucket
        self.fetch_lh = fetch_lh
        self.fetch_uc = fetch_uc
        self.fetch_vercel_image_service = fetch_vercel_image_service
        self.fail_on_error = fail_on_error
        self.verbose = verbose


def cli():
    parser = argparse.ArgumentParser(
        prog="Image retrieval",
        description="Testing the image delivery pipeline.",
    )
    parser.add_argument("--file")
    parser.add_argument("--lh_host")
    parser.add_argument("--uc_host")
    parser.add_argument("--vercel_host")
    parser.add_argument("--verbose", default=True, type=bool)
    parser.add_argument("--fetch_lh", default=False, type=bool)
    parser.add_argument("--fetch_uc", default=False, type=bool)
    parser.add_argument("--fetch_vercel_image_service", default=True, type=bool)
    parser.add_argument("--fail_on_error", default=False, type=bool)
    args = parser.parse_args()
    return Config(
        lh_host=args.lh_host,
        uc_host=args.uc_host,
        vercel_host=args.vercel_host,
        file=args.file,
        fail_on_error=args.fail_on_error,
        fetch_lh=args.fetch_lh,
        fetch_uc=args.fetch_uc,
        fetch_vercel_image_service=args.fetch_vercel_image_service,
        verbose=args.verbose,
    )


class ImageSet:
    def __init__(self, config, manifest_entry: str):
        super().__init__()
        self._manifest_entry = manifest_entry
        self._bucket_url = f"{config.lh_host}/{self._manifest_entry}"
        self._uploadcare_url = f"{config.uc_host}/-/crop/3:2/center/{self._bucket_url}"
        self._renditions = [
            f"{config.vercel_host}/_next/image?url={parse.quote(self._uploadcare_url)}&w={w}&q=75"
            for w in rendition_widths
        ]
        self._image_urls = [self._bucket_url, self._uploadcare_url] + self._renditions

    @property
    def bucket_url(self) -> str:
        return self._bucket_url

    @property
    def uploadcare_url(self) -> str:
        return self._uploadcare_url

    @property
    def vercel_renditions(self) -> list:
        return self._renditions


def parse_xml(xml_file: str):
    tree = ElementTree.parse(xml_file)
    root = tree.getroot()
    image_list = []
    for elem in root:
        if elem.tag == "{http://doc.s3.amazonaws.com/2006-03-01}Contents":
            for sub_child in elem:
                if sub_child.tag == "{http://doc.s3.amazonaws.com/2006-03-01}Key" and (
                    sub_child.text.endswith(".jpeg")
                    or sub_child.text.endswith(".jpg")
                    or sub_child.text.endswith(".png")
                ):
                    image_list.append(sub_child.text)
    return image_list


def fetch_image(image, config):
    headers = utils.default_headers()
    response = requests.get(image, headers=headers)
    if response.status_code != 200:
        print(f"{color_fail}✘ ({response.status_code}){color_end} {image}")
        print_headers(response)
        if config.fail_on_error:
            sys.exit(1)
    if response.status_code == 200:
        if not config.verbose:
            print(f"{color_ok}✔ ({response.status_code}){color_end} {image}")
        else:
            print(f"{color_ok}✔ ({response.status_code}){color_end} {image}")
            print_headers(response)


def print_headers(response):
    for name, value in sorted(response.headers.items(), key=lambda x: x[0]):
        if (
            name.startswith("X-Vercel")
            or name.startswith("Access-Control")
            or name
            in (
                "Access-Control-Allow-Origin",
                "Cache-Control",
                "Content-Security-Policy",
                "Cross-Origin-Resource-Policy",
                "Strict-Transport-Security",
            )
        ):
            print(f"\t{color_warn}{name}: {value}{color_end}")
        else:
            print(f"\t{name}: {value}")


def main():
    config = cli()
    if not config.file:
        print(f"{color_fail}No file specified{color_end}")
        sys.exit(1)

    print(f"Parsing file: {config.file}")
    images = parse_xml(config.file)
    if images:
        print(
            f"{color_ok}{len(images)} images{color_end} are listed in the manifest file"
        )
    else:
        print(f"{color_fail}No images found{color_end}")
        sys.exit(1)

    for image in [ImageSet(config, image) for image in images if image != ""]:
        if config.fetch_lh:
            fetch_image(image.bucket_url, config)
        if config.fetch_uc:
            fetch_image(image.uploadcare_url, config)
        if config.fetch_vercel_image_service:
            for url in image.vercel_renditions:
                fetch_image(url, config)

    sys.exit(0)


if __name__ == "__main__":
    main()
