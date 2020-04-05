#!/usr/bin/env bash

SRC_DIR=$1
DEST_DIR=$2
for i in ${SRC_DIR}/*
do
	name=$(echo "$i" | cut -f 1 -d '.')
	#add a mkdir for making sr_${SRC_DIR} in DEST_DIR
	waifu2x-ncnn-vulkan -i $i -o "double_${name}.png" -n 2 -g 0
done

