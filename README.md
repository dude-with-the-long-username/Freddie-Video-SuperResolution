# Freddie-Video-SuperResolution

Real time Video super resolution software (in progress)

FREDDIE- Finally, a Rad Enhancer for Dynamic Digital Immersive Entertainment



## Abstract 

Freddie reduces the time needed for Waifu2x to upscale animation (sometimes live-action) videos by applying compression techniques. Just as Netflix uses compression to quickly stream videos to your home, Freddie uses compression to expedite the waifu2x upscaling process.

## Motivation 

Waifu2x (https://github.com/nagadomi/waifu2x) is a powerful tool for upscaling anime-styled images to a higher resolution. It does this using a convolutional neural network, which can bring greater visual fidelity to images by removing the noise produced from resolution upscaling or compression.

![Image of a Waifu2x Upscale](https://i.imgur.com/irRaQ07.png)

*Image: An image of lower resolution ( left ) being brought to a higher resolution using waifu2x (right). Source: Wikipedia*


While waifu2x may take 2-4 seconds on a modern graphics card to produce a higher resolution image, this becomes problematic when upscaling frames in a video, as one video-second can take multiple minutes to process. Considering the number of visual redundancies found in anime, having an algorithm to identify these redundancies and recycling them would prove to be an effective time-reducing step to help upscale videos to higher resolutions. Freddie does this by applying I-frame and p-frame compression to anime-styled videos to reduce the work needed by the GPU.


![Image of I-Frame Compression](https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/I_P_and_B_frames.svg/1920px-I_P_and_B_frames.svg.png)
*Image: Different compression types being visualized with PacMan. Source: Wikipedia*

## Methods

Freddie is an upscaling-specific compression algorithm targeted at reducing the GPU time needed to upscale a video. Without going in-depth into the tools used, the following image summarizes the Freddie process, and how it uses previous frames to create future frames.

![Image of Dandere2x](https://i.imgur.com/7cqZz4I.png)

By only upscaling the content that can't be produced from a previous frame, Freddie can dramatically speed up the upscaling process by only upscaling essential information.

## Results



### Preformance Differences

The time-reduction Freddie produces varies based on the user input, as well as the settings used. However, in a benchmark video, Freddie provided a dramatic improvement in time over frame by frame upscaling(without exploiting temporal redundancies):

| Upscaler       | Time    |
| -------------- | ------- |
| Freddie        | 03:37 m |
| Frame by frame | 18:34 m |

# Development environment setup

Install [ffmpeg](https://ffmpeg.org/) version 4 or above for `pyAV` to work

You can check the version of your ffmpeg with

	ffmpeg -version

## Arch linux

Arch linux users will have the latest version of ffmpeg by default. If any
libraries are missing, you can guess the package names from the ubuntu
instructions. `¯\_(ツ)_/¯`

	sudo pacman -Syu ffmpeg

## Ubuntu

Ubuntu 18.04 LTS (the same as google colab) users might have version 3.x.x by
default. Run these commands to get the latest version

	sudo apt remove ffmpeg -y #remove the old version
	
	sudo add-apt-repository ppa:jonathonf/ffmpeg-4 -y
	
	sudo apt install ffmpeg -y
	
	ffmpeg -version #check if latest 4.x.x

After you install latest ffmpeg, install other dependencies of pyAV with

	sudo apt install -y libavformat-dev libavcodec-dev libavdevice-dev \
	libavutil-dev libswscale-dev libswresample-dev libavfilter-dev -y

## Virtual environment

Make a virtual environment if you haven't already

	mkdir ~/.venvs
	python3 -m venv ~/.venvs/freddie

If you get a venv module not found error, you probably have an older version of
python. Install the latest one a try again.

Source the virtual environment.

	source ~/.venvs/freddie/bin/activate

> NOTE: do this step every time you start working on the project. You should
> see an indication that virtual environment is active in your shell

Install python requirements

	pip install -r requirements.txt
	
	OR
	
	pip3 install -r requirements.txt # if pip is for python2

Open a text editor like vscode inside the virtualenv by entering this command

	code .

(similarly for other text editors)

All done, now you can develop on Freddie

## Exiting the virtual environment

To exit the virtualenv, either close your shell or enter this command to your
shell.

	deactivate

## Updating dependencies

If you add any more dependencies to freddie, make sure to update
requirements.txt with

> Make sure you are in the virtual environment before running this command.`pip`
> will make a list of all the python packages you have installed if you run it
> outside the virtualenv

	pip freeze > requirements.txt
	
	OR
	
	pip3 freeze > requirements.txt # if pip is for python2

souce