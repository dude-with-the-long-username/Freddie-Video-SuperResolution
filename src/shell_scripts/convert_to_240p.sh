#!/usr/bin/env bash
SRC_FILE=$1
DEST_FILE="240p_${1}"
DEST_RES="427x240"
ffmpeg -i ${SRC_FILE} -threads 0 -preset ultrafast -s $DEST_RES ${DEST_FILE}
# OR (doesn't work sometimes)
# ffmpeg -i ${SRC_FILE} -filter:scale=240 ${DEST_FILE}
