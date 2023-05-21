# album-labeler
A small Python script to add metadata to mp3 files.

## Installation
Install python and `mutagen` module
```
pip install mutagen
```
Move script to some directory included in $PATH (e.g. `/usr/local/bin`) to run it from any directory.

## Usage
1. Move all mp3 files from the same album to the same directory. Change filenames to match pattern: two digit track number and then song title (`01 Black Planet.mp3`, `02 Walk Away.mp3` etc.). Album information will be added to all files in the directory.
2. Download album cover in JPG format. Place it in album directory for convenience.
3. Fill all album information and run the following line: 
```
labeler.py "<album name>" "<artist name>" "<genre>" "<release date>" "<path/to/cover/image>"
```

## To Do
I most possibly won't implement any of the following things in the future, but if I will have some time and no other thing to do I can try.
- [ ] Custom order of arguments
- [ ] More filename patterns
- [ ] More album cover formats
- [ ] Probably some way to auto-fill album information from internet
