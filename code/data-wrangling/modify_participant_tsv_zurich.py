### Author: JD Elberse
### Date: 07/03/24
### This code creates the participants.tsv out of the Zurich demographics table

import pandas as pd
import numpy as np

# Load the excel file
excel = pd.read_excel("sourcedata/PSS Study Masterfile_SH_20022024.xlsx")

# Create the participant tsv
tsv = pd.DataFrame()

## Zurich has "PSS" in front of the subject numbers.
## We have to replace it with "sub-" to make it BIDS-appropriate.

# Replace & Set Index
excel['Subject Nr'] = excel['Subject Nr'].str.replace("PSS","sub-")
excel.set_index('Subject Nr', inplace=True)

# Participant ID
tsv['participant_id'] = excel.index
tsv.set_index('participant_id', inplace=True)

# Age
tsv['age'] = excel['Age at study']

# Sex
## All subjects in this dataset are male.
tsv['sex'] = np.repeat("M",len(tsv))

# Group
## Partial sleep deprivation = 3
## Total sleep deprivation = 4
## Zurich has total deprivation.
tsv['group'] = np.repeat(4,len(tsv))

# Site
tsv['site'] = np.repeat("Zurich",len(tsv))

# PSQI score
tsv['psqi_score'] = excel['PSQI']

# KSS score
tsv['kss_score_baseline'] = excel['KSS_d1_0-15']
tsv['kss_score_sd'] = excel['KSS_d2_24-39']

# Chronotype
## We have to convert MEQ to Chronotype
tsv['chronotype'] = excel['MEQ']
tsv.loc[tsv["chronotype"].between(16,41), "chronotype"] = 2 # Evening
tsv.loc[tsv["chronotype"].between(42,58), "chronotype"] = 3 # Intermediate
tsv.loc[tsv["chronotype"].between(59,86), "chronotype"] = 1 # Morning

# BMI
tsv['bmi'] = excel['Body Mass Index (kg/m2)']

# Save in dataset folder
tsv.to_csv("participants.tsv", sep="\t", na_rep="n/a")