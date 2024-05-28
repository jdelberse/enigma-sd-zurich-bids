#!/bin/bash
# v1.3

CPUS='1'
RAM='8G'
DISK='90G'

ROOT_DIR=/data/project/sleep_ENIGMA_deprivation/raw-glymphatic/zurich-bids
RAW_DIR=$ROOT_DIR/sourcedata
LOGS_DIR=$ROOT_DIR/logs
WORK_DIR=/tmp

# create the logs dir if it doesn't exist
[ ! -d "${LOGS_DIR}" ] && mkdir -p "${LOGS_DIR}"

# print the .submit header
printf "# The environment
universe       = vanilla
getenv         = True
request_cpus   = ${CPUS}
request_memory = ${RAM}
request_disk   = ${DISK}

# Execution
executable     = $ROOT_DIR/code/bids_convert_zurich.sh
\n"

# loop over all subjects
sd=$ROOT_DIR/sourcedata
for dir in $sd/*; do
	ses=${dir#$sd/pss*day}
	subid=${dir#$sd/pss}
	subid=${subid%day$ses}
    printf "arguments = $dir $subid $ses \n"
    printf "log       = ${LOGS_DIR}/\$(Cluster).\$(Process).${subid}.${ses}.log.txt\n"
    printf "output    = ${LOGS_DIR}/\$(Cluster).\$(Process).${subid}.${ses}.out.txt\n"
    printf "error     = ${LOGS_DIR}/\$(Cluster).\$(Process).${subid}.${ses}.err.txt\n"
    printf "Queue\n\n"
done
