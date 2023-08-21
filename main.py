"""
Author: Md Mostafizur Rahman
FIle: Generate simulated dataset
"""

import random, os
import pandas as pd
from typing import List, Any
from dataset_settings import NUM_SAMPLES, NUM_DUPLICATES, NUM_MISSING, DATASET_FOLDER

# Function to generate synthetic data
def generate_synthetic_data() -> List[List[Any]]:
    data = []
    for i in range(1, NUM_SAMPLES + 1):
        age = random.randint(20, 80)
        gender = random.choice(['Male', 'Female'])
        bmi = round(random.uniform(18.0, 40.0), 1)
        glucose = random.randint(70, 200)
        insulin = round(random.uniform(3.0, 20.0), 1)
        hba1c = round(random.uniform(5.0, 10.0), 1)
        family_history = random.choice(['Yes', 'No'])

        if family_history == 'Yes':
            diabetes = 'Yes' if random.random() < 0.7 else 'No'
        else:
            diabetes = 'Yes' if random.random() < 0.2 else 'No'

        data.append([i, age, gender, bmi, glucose, insulin, hba1c, family_history, diabetes])

    return data

# Function to introduce duplicates
def introduce_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    duplicate_rows = []
    for _ in range(NUM_DUPLICATES):
        row_index = random.randint(0, len(df) - 1)
        duplicate_rows.append(df.iloc[row_index])
    for row in duplicate_rows:
        # df = df.append(row, ignore_index=True)
        df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    return df

# Function to introduce missing values
def introduce_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    for _ in range(NUM_MISSING):
        row_index = random.randint(0, len(df) - 1)
        col_index = random.randint(3, len(df.columns) - 2)  # Exclude ID and Last Column
        df.iat[row_index, col_index] = None
    return df

# Main program
if __name__ == "__main__":
    # Generate synthetic data
    data = generate_synthetic_data()

    # Create DataFrame
    columns = ['ID', 'Age', 'Gender', 'BMI', 'Glucose', 'Insulin', 'HbA1c', 'FamilyHistory', 'Diabetes']
    df = pd.DataFrame(data, columns=columns)

    # Introduce duplicates
    df = introduce_duplicates(df)

    # Introduce missing values
    df = introduce_missing_values(df)

    # Construct the output path with the folder name
    output_path = os.path.join(DATASET_FOLDER, 'diabetes_dataset.csv')

    # Save the DataFrame to a CSV file
    df.to_csv(output_path, index=False)

    print("Dataset generated and saved as 'diabetes_dataset.csv'")
