import pandas as pd
import os

# Load the dataset
dataset_path = 'ProjectFinalResult.csv'
if not os.path.exists(dataset_path):
    raise FileNotFoundError(f"The dataset '{dataset_path}' does not exist.")

df = pd.read_csv(dataset_path, delimiter=';')

# Print the column names to debug
print("Columns in the dataset:", df.columns)

# Define the base URL for GitHub Pages
base_url = 'https://studious-sniffle-qjq557r7956f46q7-8000.app.github.dev/Images/'

# Check if 'Images' column exists before processing
if 'Image' not in df.columns:
    raise KeyError("The 'Images' column is not present in the dataset.")

# Generate the URLs
df['Image_URL'] = df['Image'].apply(lambda x: base_url + os.path.basename(x))

# Ensure the output directory exists
output_dir = 'LoanApplicationPic'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save the updated dataset
output_path = os.path.join(output_dir, 'ProjectFinalResult_URLs.csv')
df.to_csv(output_path, index=False, sep=';')

print(f"Updated dataset saved to {output_path}")
