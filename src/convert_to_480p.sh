#!/usr/bin/env bash
SRC_FILE=$1
DEST_FILE="480p_$1"
DEST_RES="858x480"
ffmpeg -i ${SRC_FILE} -threads 0 -preset ultrafast -s $DEST_RES ${DEST_FILE}
# OR (doesn't work sometimes)
# ffmpeg -i ${SRC_FILE} -vf scale=480:-1 ${DEST_FILE}
