# Image retrieval

## Usage

### Arguments

#### file

The name of the XML file containing metadata about the images to be retrieved from an AWS S3 bucket. The elements should
respect the namespace `http://doc.s3.amazonaws.com/2006-03-01` and follow the general structure of the following
example:

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ListBucketResult xmlns='http://doc.s3.amazonaws.com/2006-03-01'>
    <Name/>
    <Prefix></Prefix>
    <Marker></Marker>
    <IsTruncated/>
    <Contents>
        <Key/>
        <Generation/>
        <MetaGeneration/>
        <LastModified/>
        <ETag/>
        <Size/>
    </Contents>
</ListBucketResult>
```

It can be loaded from a project folder in Uploadcare.

#### lh_host

The name of the origin server hosting the images.

#### uc_host

The name of the proxy server making images available with extended transformation capabilities.

#### vercel_host

The name of a vercel deployment accessing and delivering images.

#### fetch_lh

Fetch and report on the status of images stored in the origin system. Defaults to `False`.

#### fetch_uc

Fetch and report on the status of images stored from the proxy server. Defaults to `False`.

#### fetch_vercel_image_service

Fetching the various image renditions from the Vercel image service. Defaults to `True`.

#### fail_on_error True

Exists with exit code `1` if any of the images could not be retrieved. Defaults to `False`.

#### verbose

Indicates if the output should be verbose. Defaults to `True`.

### Example invocation

```shell
 poetry run image-retrieval \
  --lh_host https://storage.googleapis.com/THE_BUCKET \
  --uc_host https://SOMETHING_SOMETHING.ucr.io \
  --vercel_host https://SOMETHING_AWESOME.vercel.app \
  --file manifest.xml \
  --fetch_lh True \
  --fetch_uc True \
  --fetch_vercel_image_service True \
  --fail_on_error True \
  --verbose True
```

## Example Output

```
Parsing file: manifest.xml
215 images are listed in the manifest file
✔ (200) https://storage.googleapis.com/THE_BUCKET/002e641a-0679-49e3-aaef-3863bb80768e.jpg
	Accept-Ranges: bytes
	Age: 465
	Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000
	Cache-Control: public, max-age=3600
	Content-Language: en
	Content-Length: 615884
	Content-Type: image/jpeg
	Date: Wed, 22 Nov 2023 09:02:31 GMT
	ETag: "e7dc2e0148d7ccd0b746f54a8ccbe17a"
	Expires: Wed, 22 Nov 2023 10:02:31 GMT
	Last-Modified: Tue, 21 Nov 2023 10:24:02 GMT
	Server: UploadServer
	X-GUploader-UploadID: ABPtcPr6ltuT6yl8GUjnNdVYyHt3rtGqIEu3gPa7DMfk_xGgnToQrKv4RW2RRsyb_sewQ0XUQHN8GJo
	x-goog-generation: 1700562242552997
	x-goog-hash: crc32c=azp4pA==, md5=59wuAUjXzNC3RvVKjMvheg==
	x-goog-metageneration: 1
	x-goog-storage-class: STANDARD
	x-goog-stored-content-encoding: identity
	x-goog-stored-content-length: 615884
✔ (200) https://SOMETHING_SOMETHING.ucr.io/-/crop/3:2/center/https://storage.googleapis.com/THE_BUCKET/002e641a-0679-49e3-aaef-3863bb80768e.jpg
	Access-Control-Allow-Methods: HEAD, GET, OPTIONS
	Access-Control-Allow-Origin: *
	Access-Control-Expose-Headers: Content-Length, Etag, X-Image-Width, X-Image-Height, X-Image-Acceptable-Original, X-Image-Acceptable-Improved
	Cache-Control: public, max-age=31522522
	Connection: keep-alive
	Content-Disposition: inline
	Content-Length: 80498
	Content-Type: image/jpeg
	Date: Wed, 22 Nov 2023 09:10:17 GMT
	ETag: "c4ebe5ce0fecf583c9a56e22e4238496"
	Server: Uploadcare
	X-Image-Height: 753
	X-Image-Width: 1130
	X-Robots-Tag: noindex, nofollow, nosnippet, noarchive
✘ (502) https://SOMETHING_AWESOME.vercel.app/_next/image?url=https%3A//SOMETHING_SOMETHING.ucr.io/-/crop/3%3A2/center/https%3A//storage.googleapis.com/THE_BUCKET/002e641a-0679-49e3-aaef-3863bb80768e.jpg&w=640&q=75
	Cache-Control: public, max-age=0, must-revalidate
	Connection: keep-alive
	Content-Length: 88
	Content-Security-Policy: script-src 'none'; frame-src 'none'; sandbox;
	Content-Type: text/plain; charset=utf-8
	Date: Wed, 22 Nov 2023 09:10:17 GMT
	Server: Vercel
	Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
	X-Vercel-Error: OPTIMIZED_EXTERNAL_IMAGE_REQUEST_UNAUTHORIZED
	X-Vercel-Id: fra1::7gtk5-1700644217844-6c5c893c8038
✘ (502) https://SOMETHING_AWESOME.vercel.app/_next/image?url=https%3A//SOMETHING_SOMETHING.ucr.io/-/crop/3%3A2/center/https%3A//storage.googleapis.com/THE_BUCKET/002e641a-0679-49e3-aaef-3863bb80768e.jpg&w=750&q=75
	Cache-Control: public, max-age=0, must-revalidate
	Connection: keep-alive
	Content-Length: 88
	Content-Security-Policy: script-src 'none'; frame-src 'none'; sandbox;
	Content-Type: text/plain; charset=utf-8
	Date: Wed, 22 Nov 2023 09:10:18 GMT
	Server: Vercel
	Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
	X-Vercel-Error: OPTIMIZED_EXTERNAL_IMAGE_REQUEST_UNAUTHORIZED
	X-Vercel-Id: fra1::bk5lz-1700644218067-6ea9f6992e37
✘ (502) https://SOMETHING_AWESOME.vercel.app/_next/image?url=https%3A//SOMETHING_SOMETHING.ucr.io/-/crop/3%3A2/center/https%3A//storage.googleapis.com/THE_BUCKET/002e641a-0679-49e3-aaef-3863bb80768e.jpg&w=828&q=75
	Cache-Control: public, max-age=0, must-revalidate
	Connection: keep-alive
	Content-Length: 88
	Content-Security-Policy: script-src 'none'; frame-src 'none'; sandbox;
	Content-Type: text/plain; charset=utf-8
	Date: Wed, 22 Nov 2023 09:10:18 GMT
	Server: Vercel
	Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
	X-Vercel-Error: OPTIMIZED_EXTERNAL_IMAGE_REQUEST_UNAUTHORIZED
	X-Vercel-Id: fra1::ngl42-1700644218269-dac0655c8851
✔ (200) https://SOMETHING_AWESOME.vercel.app/_next/image?url=https%3A//SOMETHING_SOMETHING.ucr.io/-/crop/3%3A2/center/https%3A//storage.googleapis.com/THE_BUCKET/002e641a-0679-49e3-aaef-3863bb80768e.jpg&w=1080&q=75
	Accept-Ranges: bytes
	Access-Control-Allow-Origin: *
	Age: 30691
	Cache-Control: public, max-age=31536000, must-revalidate
	Connection: keep-alive
	Content-Disposition: inline; filename="002e641a-0679-49e3-aaef-3863bb80768e.jpg"
	Content-Length: 57775
	Content-Security-Policy: script-src 'none'; frame-src 'none'; sandbox;
	Content-Type: image/jpeg
	Cross-Origin-Resource-Policy: cross-origin
	Date: Wed, 22 Nov 2023 00:38:46 GMT
	Last-Modified: Wed, 22 Nov 2023 00:38:46 GMT
	Server: Vercel
	Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
	Timing-Allow-Origin: *
	Vary: Accept
	X-Vercel-Cache: HIT
	X-Vercel-Id: fra1::85bzk-1700644218485-652cd0864d69
✔ (200) https://SOMETHING_AWESOME.vercel.app/_next/image?url=https%3A//SOMETHING_SOMETHING.ucr.io/-/crop/3%3A2/center/https%3A//storage.googleapis.com/THE_BUCKET/002e641a-0679-49e3-aaef-3863bb80768e.jpg&w=1200&q=75
	Accept-Ranges: bytes
	Access-Control-Allow-Origin: *
	Age: 30691
	Cache-Control: public, max-age=31536000, must-revalidate
	Connection: keep-alive
	Content-Disposition: inline; filename="002e641a-0679-49e3-aaef-3863bb80768e.jpg"
	Content-Length: 70614
	Content-Security-Policy: script-src 'none'; frame-src 'none'; sandbox;
	Content-Type: image/jpeg
	Cross-Origin-Resource-Policy: cross-origin
	Date: Wed, 22 Nov 2023 00:38:47 GMT
	Last-Modified: Wed, 22 Nov 2023 00:38:47 GMT
	Server: Vercel
	Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
	Timing-Allow-Origin: *
	Vary: Accept
	X-Vercel-Cache: HIT
	X-Vercel-Id: fra1::w5g59-1700644218557-a447b3c8ad1a
✘ (502) https://SOMETHING_AWESOME.vercel.app/_next/image?url=https%3A//SOMETHING_SOMETHING.ucr.io/-/crop/3%3A2/center/https%3A//storage.googleapis.com/THE_BUCKET/002e641a-0679-49e3-aaef-3863bb80768e.jpg&w=1440&q=75
	Cache-Control: public, max-age=0, must-revalidate
	Connection: keep-alive
	Content-Length: 88
	Content-Security-Policy: script-src 'none'; frame-src 'none'; sandbox;
	Content-Type: text/plain; charset=utf-8
	Date: Wed, 22 Nov 2023 09:10:19 GMT
	Server: Vercel
	Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
	X-Vercel-Error: OPTIMIZED_EXTERNAL_IMAGE_REQUEST_UNAUTHORIZED
	X-Vercel-Id: fra1::t456c-1700644218653-be660cd41b74
✔ (200) https://SOMETHING_AWESOME.vercel.app/_next/image?url=https%3A//SOMETHING_SOMETHING.ucr.io/-/crop/3%3A2/center/https%3A//storage.googleapis.com/THE_BUCKET/002e641a-0679-49e3-aaef-3863bb80768e.jpg&w=1920&q=75
	Accept-Ranges: bytes
	Access-Control-Allow-Origin: *
	Age: 32826
	Cache-Control: public, max-age=31536000, must-revalidate
	Connection: keep-alive
	Content-Disposition: inline; filename="002e641a-0679-49e3-aaef-3863bb80768e.jpg"
	Content-Length: 70614
	Content-Security-Policy: script-src 'none'; frame-src 'none'; sandbox;
	Content-Type: image/jpeg
	Cross-Origin-Resource-Policy: cross-origin
	Date: Wed, 22 Nov 2023 00:03:12 GMT
	Last-Modified: Wed, 22 Nov 2023 00:03:11 GMT
	Server: Vercel
	Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
	Timing-Allow-Origin: *
	Vary: Accept
	X-Vercel-Cache: HIT
	X-Vercel-Id: fra1::755kw-1700644219195-61e79f63c2ed
```