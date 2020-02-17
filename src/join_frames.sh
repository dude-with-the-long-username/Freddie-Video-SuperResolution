#!/usr/bin/env bash

SRC_DIR=$1
DEST_FILE=$2
PREFIX=""
#ffmpeg -loop 1 -i ${SRC_DIR}/"${PREFIX}%d.bmp" $DEST_FILE
ffmpeg -r 1/5 -i ${SRC_DIR}/"{PREFIX}%d.bmp" -c:v libx264 -vf fps=25 -pix_fmt yuv480p $DEST_FILE
#-c:v libx264 -pix_fmt yuv420p 
