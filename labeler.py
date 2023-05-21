#!/usr/bin/env python3

from mutagen.id3 import ID3, TALB, TCON, TDRC, TIT2, TPE1, TRCK, APIC
import sys
import glob

for filename in glob.glob("*.mp3"):
    #print(filename)

    tracknumber = filename[0:2]
    songname = filename[2:-4]

    albumart = open(sys.argv[5], "rb")

    audio = ID3(filename)

    audio["TALB"] = TALB(encoding=3, text=sys.argv[1])
    audio["TCON"] = TCON(encoding=3, text=sys.argv[3])
    audio["TDRC"] = TDRC(encoding=3, text=sys.argv[4])
    audio["TIT2"] = TIT2(encoding=3, text=songname)
    audio["TPE1"] = TPE1(encoding=3, text=sys.argv[2])
    audio["TRCK"] = TRCK(encoding=3, text=tracknumber)

    audio["APIC"] = APIC(encoding=3, mime="image/jpeg", type=3, desc=u"Cover", data=albumart.read())

    audio.save()
