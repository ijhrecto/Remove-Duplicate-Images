# Remove-Duplicate-Images
Remove duplicate images using perceptual hashing

1. This image duplicate remover uses perception hashing(phash) from imagehash.
2. Image files should be in a single folder
3. removes images if PIL can't read it (may be turned off)
4. creates the hashes, gets the first unique hash, and lists the files mapped from the hashes
5. deletes the files not listed as unique files

## Dependencies
PIL
imagehash
