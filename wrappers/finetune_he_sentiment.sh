#!/bin/bash

# transfer all the args to the py script (the parsing is executed inside)
# the only arg that is mandatory is the '--logs_dir' for inner print (&>)

PARAMS=$*

# --logs_dir parsing
[[ $PARAMS =~ --logs_dir[[:space:]]([a-zA-Z./]*) ]] && LOGS_DIR=${BASH_REMATCH[1]}

# set log subdir
dt=$(date '+%d_%m_%Y_%H_%M_%S');
sd=$LOGS_DIR"finetune_he_sentiment/$dt/"
mkdir -p $sd
echo "Logging to: $sd"

# set new path of LOGS_DIR
PARAMS=${PARAMS//${LOGS_DIR}/${sd}}

python src/finetune_he_sentiment.py $PARAMS &> $sd/log.txt

echo "Done!"