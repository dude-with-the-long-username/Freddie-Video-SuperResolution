#!/usr/bin/env bash

SRC_DIR=$1
DEST_FILE=$2
PREFIX=$3
#ffmpeg -loop 1 -i ${SRC_DIR}/"${PREFIX}%d.png" $DEST_FILE
#ffmpeg -r 1/5 -i ${SRC_DIR}/"${PREFIX}%d.png" -c:v libx264 -vf fps=25 -pix_fmt yuv480p $DEST_FILE
#-c:v libx264 -pix_fmt yuv420p 
ffmpeg -framerate 23.976 -i "${SRC_DIR}/${PREFIX}%d.png" $2
