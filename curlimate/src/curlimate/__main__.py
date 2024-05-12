import argparse

from . import server
from . import colors
from . import imageStuff

colors = colors.colors()

LOGO = rf"""
       {colors.OKCYAN}_   _  ____   _      {colors.HEADER}_                    _         
{colors.FAIL}  ___ {colors.OKCYAN}| | | ||  _ \ | |    {colors.HEADER}(_) _ __ ___    __ _ | |_   ___ 
{colors.FAIL} / __|{colors.OKCYAN}| | | || |_) || |    {colors.HEADER}| || '_ ` _ \  / _` || __| / _ \
{colors.FAIL}| (__ {colors.OKCYAN}| |_| ||  _ < | |___ {colors.HEADER}| || | | | | || (_| || |_ |  __/
{colors.FAIL} \___|{colors.OKCYAN} \___/ |_| \_\|_____|{colors.HEADER}|_||_| |_| |_| \__,_| \__| \___|
            {colors.OKGREEN}-make animated cURL server thingies-{colors.ENDC}
                                                           
"""

def parseDoubleArgs(argInput, dataType):
    print([argInput, dataType])
    try:
        # try to convert it to the type
        argValue = dataType(argInput)
        return argValue
    except ValueError:
        # if there is no arg just return true
        return True

def printIntro():
    print(LOGO)

def debug(args):
    print(args)

def main():
    printIntro()

    parser = argparse.ArgumentParser(description="cURLimate commands", prog="cURLimate", epilog=f"{colors.FAIL}c{colors.OKCYAN}URL{colors.HEADER}imate{colors.ENDC} by {colors.OKGREEN}Antonabi{colors.ENDC}")

    subparsers = parser.add_subparsers(dest="command", title="commands", description="commands")

    #------defining commands------

    # start command
    startParser = subparsers.add_parser("start", help="starts the programm")
    startParser.set_defaults(func=server.start)

    startParser.add_argument("--frameDir", help="directory containing frames", default="frames", type=str)
    startParser.add_argument("--frameInterval", help="time between frames", default=0.1, type=float)
    startParser.add_argument("--loop", help="loop the anmation", type=lambda x: parseDoubleArgs(x, int), const=True, nargs="?", default=1)
    startParser.add_argument("--urlPath", help="path which the ascii anmation is hosted on", default="", type=str)
    startParser.add_argument("--port", help="port which the ascii anmation is hosted on", default=8000, type=int)

    #debug command
    debugParser = subparsers.add_parser("debug", help="doing debug thingies")
    debugParser.set_defaults(func=debug)

    # imageToAscii command
    imageParser = subparsers.add_parser("imageToAscii", help="converts an image to ascii frames (into your folder) (also works with gifs)")
    imageParser.set_defaults(func=imageStuff.imageConvert)

    imageParser.add_argument("--frameDir", help="directory containing frames", default="frames", type=str)
    imageParser.add_argument("--input", help="path of the input file", type=str)

    # parse the args
    args = parser.parse_args()

    if args.command == None:
        parser.print_help()
        
    elif hasattr(args, "func"):
        args.func(args)