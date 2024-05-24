# cURLimate

cURLimate is a python package/library/module that allowes you to make animated terminal animations like [parrot.live](http://parrot.live).

## Installation

To install it just clone the repo with:

```sh
git clone https://github.com/Antonabi/cURLimate.git
```

and then type:

```sh
pip install curlimate/curlimate
```

Now it should install.

## Usage

To run cURLimate just type in

```sh
cURLimate
```

into your terminal.

## Commands

These are the commands of cURLimate.

### Start

With the start command you can start your server.
Run it with:

```sh
cURLimate start
```

#### Start Command Options

These are the options of the start command:

##### frameDir

```sh
cURLimate start --frameDir yourDir
```

Supply the frameDir option to set the dircetory your frames are stored in.  
(The default is "frames")

##### frameInterval

```sh
cURLimate start --frameInterval 0.42
```

Supply the frameInterval option to set the interval between ervery animation frame.  
(The default is 0.1)

##### framePath

```sh
cURLimate start --framePath your/url/path
```

Supply the framePath option to set the url path where your animation will be. The example sets it to your/url/path, which means you will have to go to `yourServerAddr:port/your/url/path`  
(The default is just the index page ("/"))

##### port

```sh
cURLimate start --port 4269
```

Supply the port option to set the port where your animation will be. If you do it like the example your animation will be on `yourServerAddr:4269/urlPath`.  
(The default is just the index page ("/"))

### imageToAscii

With the imageToAscii command you can convert images to ascii (Also works with gifs). These will be directly saved in your frame dir.  
I didnt make any portion of the image to ascii conversion. I just used the [ascii-magic](https://pypi.org/project/ascii-magic/) library by [leandrobarone](https://pypi.org/user/leandrobarone/), wich made my life so mouch easier. (Big thanks)

Run it like this:

```sh
cURLimate imageToAscii
```

#### imageToAscii Command Options

imageToAscii only has these options:

##### frameDir

```sh
cURLimate imageToAscii --frameDir yourDir
```

Supply the frameDir option to set the dircetory your frames are stored in.  
(The default is "frames")

##### input

```sh
cURLimate imageToAscii --input rickymated.gif
```

You have to provide this argument.

Supply the input argument to provide the path of your file for conversion.
