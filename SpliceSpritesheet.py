import sys
from PIL import Image

if len(sys.argv)<3:
    print("")
    print("To use: ")
    print("     Arg1: file name")
    print("     Arg2: number of sprites in file")
    print("     Arg3 (optional): destination directory. defaults to script's directory")
    exit()

spritesheet = Image.open(sys.argv[1])
spritewidth = spritesheet.width/int(sys.argv[2])

for i in range(int(sys.argv[2])):
    name = "sprite"+str(i)+".png"
    if len(sys.argv)==4:
        name = sys.argv[3]+"/"+name

    cropped = spritesheet.crop((i*spritewidth, 0, (i*spritewidth)+spritewidth, spritesheet.height))
    cropped.save(name, "PNG")