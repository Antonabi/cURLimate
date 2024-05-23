from PIL import Image
from ascii_magic import AsciiArt
import imageio
import os
from tqdm import tqdm
import struct

from . import colors


def validateInput(inputArgs):
    # no gif input
    if inputArgs.input == None:
        print(colors.fail("You didnt provide an input gif."))
        print(colors.header("(Do that with --input.)"))
        quit(code=4269)

    # provided gif doesn't exist
    if os.path.exists(inputArgs.input) == False:
        print(colors.fail("The gif doesn't exist."))
        quit(code=4269)
    
    # dir doesn't exist
    if os.path.isdir(inputArgs.frameDir) == False:
        print(colors.fail(f"The frame dir '{inputArgs.frameDir}' doesnt exist."))
        if input(colors.okgreen("Do you want to create it?")+" (y/n)") == "y":
            os.makedirs(inputArgs.frameDir)
            if os.path.isdir(inputArgs.frameDir):
                print(colors.okblue(f"Succesfully created directory '{inputArgs.frameDir}'"))
            else:
                print(colors.fail(f"Something went wrong while creating '{inputArgs.frameDir}'"))
        else:
            print(colors.fail("cURLimate won't run with a frame directory. Create it and use the --frameDir arg to specify the name or create a dir named frame. (You can just run this again and it will ask you if you want to create it. Then it will create it for you.)"))
            quit(code=4269)

    try:
        frames = imageio.mimread(inputArgs.input)
    except struct.error:
        print(colors.fail("The file you've providid is either not an image or gif or imageio cant work with that."))
        quit(code=4269)

def imageConvert(args):
    validateInput(args)
    print(colors.header("Creating frame/s..."))

    frames = imageio.mimread(args.input)

    for i, frame in tqdm(enumerate(frames), total=len(frames), ncols=50):

        pillowedFrame = Image.fromarray(frame)
        asciiFrame = AsciiArt.from_pillow_image(pillowedFrame)

        asciiFrame.to_file(f"{args.frameDir}/frame{i}.txt")

    print(colors.bold("\nSuccessfully created the frame/s"))