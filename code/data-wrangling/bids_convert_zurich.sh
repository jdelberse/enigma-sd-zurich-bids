#!/bin/bash
sd=$(pwd)/sourcedata
dir=$1
subid=$2
ses=$3

if [ -d $dir ]; then
	echo processing sub-$subid
	echo session $ses at $dir
	dcm2bids -d $dir -c code/bids_config_zurich.json  -p $subid -s $ses --force_dcm2bids
fi
