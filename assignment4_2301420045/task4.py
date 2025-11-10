#!/bin/bash

echo "kernel Version: "
uname -r

echo "User:"

whoami

echo "Hardware info: "

lscpu | grep 'Virtualisation'
