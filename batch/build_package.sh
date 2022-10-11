#!/bin/bash 

# !!! Only run script with BASH command !!! #

currentDir=$(pwd)

# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
echo $SCRIPT

# Absolute path this script is in, thus /home/user/bin
SCRIPTPATH=$(dirname "$SCRIPT")
echo "scriptPath: $SCRIPTPATH"
cd "$SCRIPTPATH/.."
python3.8 -m build && \
cd "$currentDir"
