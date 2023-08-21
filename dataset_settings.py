'''
Author: Md Mostafizur Rahman
File: Configuration file
'''

from pathlib import Path

# dorectory related
ROOT = Path(__file__).resolve().parent
DATASET_FOLDER = ROOT / "dataset"

# Global variables
NUM_SAMPLES= 500
NUM_DUPLICATES= 20
NUM_MISSING = int(NUM_SAMPLES * 0.1)  # 10% missing values
