### Author: JD Elberse
### Date: 11/03/24
### This code relabels the Zurich dataset sessions

import os
import pandas as pd
import argparse as ap

# Specify if this is a test or if data should actually be renamed
parser = ap.ArgumentParser(prog='RenameSessionLabels',
    description='Labels sessions according to how the participant slept')
parser.add_argument('-t', '--test', action='store_true')
args = parser.parse_args()

# Load, add sub-labels, set sub as index
tsv = pd.read_csv("participants.tsv", sep="\t")
tsv.set_index('participant_id', inplace=True)

for sub in tsv.index:
    ses_labs = {"ses-nn" : "ses-bl", 
                "ses-tsd" : "ses-sd", 
                "ses-rc" : "ses-rc"}
    
    for ses in ses_labs.keys():
        for ext in ['nii.gz','json']:
            old_scan = f"{sub}/{ses}/anat/{sub}_{ses}_T1w.{ext}"
            new_scan = f"{sub}/{ses}/anat/{sub}_{ses_labs[ses]}_T1w.{ext}"
        
            if os.path.exists(old_scan) and not os.path.exists(new_scan):
                print(f"{old_scan} >>> {new_scan}")
                if not args.test:
                    os.rename(old_scan, new_scan)
            else:
                print(f"{new_scan} exists. Skipping...")            
        
        old_dir = f"{sub}/{ses}"
        new_dir = f"{sub}/{ses_labs[ses]}"

        if os.path.exists(old_dir) and not os.path.exists(new_dir):
            print(f"{old_dir} >>> {new_dir}")
            if not args.test:
                os.rename(old_dir, new_dir)
        else:
            print(f"{new_dir} exists. Skipping...")