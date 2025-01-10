#!/usr/bin/bash

DIR=$1

find ${DIR} -maxdepth 1 -type d | wc -l
