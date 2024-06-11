### Author: JD Elberse
### Date: 11/06/24
### This code extracts PVSVF and DTI-ALPS indices from the derivatives folder

import os
import pandas as pd

# Load, add sub-labels, set sub as index
tsv = pd.read_csv("participants.tsv", sep="\t")
tsv.set_index('participant_id', inplace=True)

# Set parameters
pvs_source = "shiva"
sessions = ["ses-bl","ses-sd"]

# Create new output csv
out = tsv
out['pvsvf-baseline'] = 0
out['pvsvf-sleep-deprivation'] = 0
out['dti-alps-baseline'] = 0
out['dti-alps-sleep-deprivation'] = 0

# Loop over subjects, collect DTI-ALPS data
for sub in tsv.index:
	print(f"Processing {sub}")
	pvs_path = f"derivatives/{pvs_source}/{sub}/pvs.stat.csv"
	if os.path.exists(pvs_path):
		pvs = pd.read_csv(pvs_path).set_index("Session")
		if sessions[0] in pvs.index:
			print(f"PVS (baseline) data found at {pvs_path}")
			pvsvf_bl = pvs.loc[sessions[0]]['PVSVF']
		else:
			pvsvf_bl = "n/a"
		
		if sessions[1] in pvs.index:
			print(f"PVS (SD) data found at {pvs_path}")
			pvsvf_sd = pvs.loc[sessions[1]]['PVSVF']
		else:
			pvsvf_sd = "n/a"
	else:
		print("No PVS data found")
		
		
	
	alps_bl_path = f"derivatives/alps/{sub}/{sessions[0]}/alps.stat/alps.csv"
	if os.path.exists(alps_bl_path):
		print(f"ALPS (baseline) data found at {alps_bl_path}")
		alps_bl = pd.read_csv(alps_bl_path)['alps'].item()
	else:
		print("No ALPS (baseline) data found")
		alps_bl = "n/a"
	
	alps_sd_path = f"derivatives/alps/{sub}/{sessions[1]}/alps.stat/alps.csv"
	if os.path.exists(alps_sd_path):
		print(f"ALPS (SD) data found at {alps_sd_path}")
		alps_sd = pd.read_csv(alps_sd_path)['alps'].item()
	else:
		print("No ALPS (SD) data found")
		alps_sd = "n/a"
	
	out.loc[sub, 'pvsvf-baseline'] = pvsvf_bl
	out.loc[sub, 'pvsvf-sleep-deprivation'] = pvsvf_sd
	out.loc[sub, 'dti-alps-baseline'] = alps_bl
	out.loc[sub, 'dti-alps-sleep-deprivation'] = alps_sd
	print(f"Finished!\n")

out_path = "derivatives/participants_with_indices.tsv"
out.to_csv("derivatives/participants_with_indices.tsv", sep='\t')
print(f"Saved to {out_path}.")