#!/bin/bash

#xhost +

sudo docker run --gpus all -e DISPLAY=:0.0 -e QT_X11_NO_MITSHM=1 --net=host -v /tmp/.X11-unix:/tmp/.X11-unix --volume="$HOME/.Xauthority:/root/.Xauthority:rw" -dt advantech_edge_ai:v1 python ../advan/app_video.py
