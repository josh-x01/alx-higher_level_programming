#!/bin/bash
sudo chmod u+x *
git add .
read msg
git commit -m $msg
git push
