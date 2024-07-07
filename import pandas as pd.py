import pandas as pd
import os
import subprocess

# Load the dataset
dataset_path = 'Images/ProjectFinalResult.csv'
df = pd.read_csv(dataset_path, delimiter=';')

# Define the base URL
base_url = 'https://github.com/EltonDlamini97/LoanApplicationPics/raw/main/'

# Generate the URLs
df['Image_URL'] = df['Images'].apply(lambda x: base_url + os.path.basename(x))

# Save the updated dataset
updated_dataset_path = 'Images/ProjectFinalResult_with_URLs.csv'
df.to_csv(updated_dataset_path, index=False)

# Define the local repository path
repo_path = 'LoanApplicationPics'

# Copy the updated dataset to the repository
os.replace(updated_dataset_path, os.path.join(repo_path, 'Images/ProjectFinalResult_with_URLs.csv'))

# Change directory to the repository
os.chdir(repo_path)

# Run Git commands to push the changes to GitHub
subprocess.run(['git', 'add', 'Images/ProjectFinalResult_with_URLs.csv'])
subprocess.run(['git', 'commit', '-m', 'Add ProjectFinalResult with image URLs'])
subprocess.run(['git', 'push', 'origin', 'main'])