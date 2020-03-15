# Freddie-Video-SuperResolution
Real time Video super resolution software (in progress)

FREDDIE- Finally, a Rad Enhancer for Dynamic Digital Immersive Entertainment

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

	souce ~/.venvs/freddie/bin/activate

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

