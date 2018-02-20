# PNG format and steganography

### PNG format

- Signature : 89  50  4e  47  0d  0a  1a  0a
- Chunks
  - IHDR : header (width, height, interlaced, ... )
  - PLTE : palette
  - IDAT : data chunk ( multiple IDATE possible )
  - IEND : end of PNG

### Tools for analysing PNG

- exiftool
- pngcheck

### Steganography Method

- Putting additional data after IEND
  - exiftool can check this

- manipulating image size
  - __weight, height can be manipulated__
  - IHDR crc value might be wrong if size if fixed
  - image viewers cannot detect original size

---

### References

> http://www.libpng.org/pub/png/spec/1.1/PNG-Rationale.html#R.PNG-file-signature

> https://en.wikipedia.org/wiki/Portable_Network_Graphics
