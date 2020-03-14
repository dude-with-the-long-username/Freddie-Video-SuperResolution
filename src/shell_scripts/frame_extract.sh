#!/usr/bin/env bash
# TODO: comment bottom paragraph <07-02-20, Balamurali M> #

SRC_FILE=$1
FRAME_DIR=$2
#mkdir -p $FRAME_DIR
name=$(echo "$SRC_FILE" | cut -f 1 -d '.')
#extract all frames
ffmpeg -i ${SRC_FILE} $FRAME_DIR/"${name}%d".bmp
# add -r 1/1 to drop frames, check man

#####################################
#  purely for remembering purposes  #
#####################################
# i don't plan on making the below lines to single script as of yet
