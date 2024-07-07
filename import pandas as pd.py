import pandas as pd
import os
import subprocess

# Load the dataset
dataset_path = 'Images/ProjectFinalResult.csv'
df = pd.read_csv(dataset_path, delimiter=';')

# Define the base URL
base_url = 'https://raw.githubusercontent.com/EltonDlamini97/LoanApplicationPics/main/'

# Generate the URLs
df['Image_URL'] = df['Images'].apply(lambda x: base_url + os.path.basename(x))

# Define the updated dataset path
updated_dataset_path = 'LoanApplicationPic/ProjectFinalResult_URLs.csv'

# Save the updated dataset
df.to_csv(updated_dataset_path, index=False)

# Git commands to add, commit, and push the updated CSV to the repository
repo_path = 'LoanApplicationPics'  # Change this to your repository's path

# Move the updated dataset to the repository directory
os.replace(updated_dataset_path, os.path.join(repo_path, updated_dataset_path))

# Change directory to the repository
os.chdir(repo_path)

# Run Git commands to push the changes
subprocess.run(['git', 'add', updated_dataset_path])
subprocess.run(['git', 'commit', '-m', 'Add ProjectFinalResult with image URLs'])
subprocess.run(['git', 'push', 'origin', 'main'])
