## Zurich Dataset (`zurich-bids`)

## Overview

This dataset contains MRI data from a sleep manipulation study conducted at the University of Zurich (Switzerland). It is part of the ENIGMA-Sleep Working Group collection used to study the effects of sleep loss on glymphatic MRI indices. The data are organized according to the Brain Imaging Data Structure (BIDS) and managed with DataLad (git-annex).

## Sample

| Item | Value |
|---|---|
| Site | Zurich |
| Affiliation | University of Zurich |
| Country | Switzerland |
| Participants (N) | 31 |
| Age, mean (SD), years | 36.7 (19.0) |
| Male (%) | 100 |

## Sleep protocol

- **BL**: baseline, habitual
- **SD**: total sleep deprivation, 40h
- **RC**: recovery, habitual

## Imaging data

### T1-weighted (`anat/`)

| Parameter | Value |
|---|---|
| Scanner | GE Signa PET/MR |
| Sequence | BRAVO |
| TR (ms) | 8.4 |
| TE (ms) | 3.22 |
| TI (ms) | 600 |
| Flip angle (°) | 8 |

## Data organization

- `sub-<ID>/ses-<label>/`: raw BIDS data (`anat/`)
- `participants.tsv`: participant-level information
- `sub-<ID>/sub-<ID>_sessions.tsv`: session-level information (condition, visit, date, time)
- `derivatives/`: processed outputs, if present

File contents are tracked with git-annex. After cloning, retrieve data with `datalad get <path>`.

## Original publication

Weigend, S., Holst, S. C., Treyer, V., et al. (2019). Dynamic changes in cerebral and peripheral markers of glutamatergic signaling across the human sleep-wake cycle. *Sleep*, zsz161. [https://doi.org/10.1093/sleep/zsz161](https://doi.org/10.1093/sleep/zsz161)

## Contact

- Jorik D. Elberse: [j.elberse@fz-juelich.de](mailto:j.elberse@fz-juelich.de)
- Masoud Tahmasian: [m.tahmasian@fz-juelich.de](mailto:m.tahmasian@fz-juelich.de)
