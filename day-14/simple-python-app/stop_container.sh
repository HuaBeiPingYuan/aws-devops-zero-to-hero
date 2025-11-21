#!/bin/bash
set -e

containerID=docker ps | awk -F" " '{Print $1}'

docker rm -f $containerID
wget https://aws-codedeploy-eu-north-1.s3.eu-north-1.amazonaws.com/latest/install
