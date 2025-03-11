SHELL := /bin/bash

all:
	source /opt/ros/noetic/setup.bash && ccache g++ -std=c++14 -o node.o node.cpp `pkg-config --cflags --libs roscpp std_msgs`
