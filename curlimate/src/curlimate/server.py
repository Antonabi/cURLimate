from flask import Flask, Response, request, render_template
import time
import os
from gunicorn.app.base import BaseApplication
import socket

from . import colors

inputArgs = None #presetting the args

def validateInput(inputArgs):
    # dir doesn't exist
    try:
        os.listdir(inputArgs.frameDir)
    except FileNotFoundError:
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

    # dir is empty
    if os.listdir(inputArgs.frameDir) == []:
        print(colors.fail(f"The frame dir '{inputArgs.frameDir}' is empty."))
        print(colors.warning("If you want to display an animation, fill it with frames."))
        quit(code=4269)

    if inputArgs.urlPath == "getServerAddress":
        print(colors.fail(f"You are not allowed to use 'getServerAddress' as an urlPath."))
        print(colors.warning("(It's used by the programm)"))
        quit(code=4269)

def start(args):
    validateInput(args)
    global inputArgs
    inputArgs = args
    global address
    address = f"http://{getServerIp()}:{inputArgs.port}/{inputArgs.urlPath}"
    print(args)

    print(colors.magenta("Starting server..."))
    options = {
        "bind": "0.0.0.0:8000"
    }
    FlaskGunicornApplication(app, options).run()

def generateAnimation():
        
    frames = os.listdir(inputArgs.frameDir)
    frames.sort()

    if inputArgs.loop == True and type(inputArgs.loop) == bool:
        while True:
            for frame in frames:
                
                with open(f"{inputArgs.frameDir}/{frame}", 'r') as frameFile:
                    frameData = f"{frameFile.read()}\n{colors.clear()}"
                    yield frameData
                    time.sleep(inputArgs.frameInterval)
    else:
        for loop in range(inputArgs.loop):
            for frame in frames:
                    
                    with open(f"{inputArgs.frameDir}/{frame}", 'r') as frameFile:
                        frameData = f"{frameFile.read()}\n{colors.clear()}"
                        yield frameData
                        time.sleep(inputArgs.frameInterval)


def getServerIp():
    # create a socket conn to get the hostname of the server
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))  # connect with Google DNS
    serverIp = s.getsockname()[0]  # get the ip of the server
    s.close()
    return serverIp

# ----- actual server ------


# defining server and stuff (bro I just spent one hour of my life figouring why tf I need this)
class FlaskGunicornApplication(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        for key, value in self.options.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application

def handleFalseReqs(inputRequest):
    headers = inputRequest.headers

    if "User-Agent" in headers and "curl" in headers.get("User-Agent"):
        return False
    else:
        return True

app = Flask(__name__)

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def handleReqs(path: str):

    if path == "getServerAddress":
        return {"address": address}

    if handleFalseReqs(request):
        libPath = os.path.dirname(os.path.abspath(__file__))
        htmlPath = os.path.join(libPath, "sites/wrongClient.html")

        with open(htmlPath, "r") as f:
            html = f.read()

        return html
    
    if path == inputArgs.urlPath:
        # Send per mime stream to the client
        return Response(generateAnimation(), mimetype="text/plain")
    else:
        return f"Where are you now? Under the sea, under the sea e... - Faded Singer\n (Go to /{inputArgs.urlPath} to see the animation)"