import pandas as pd # type: ignore
import os

# Load the dataset
dataset_path = 'Images/ProjectFinalResult.csv'
df = pd.read_csv(dataset_path, delimiter=';')

# Define the base URL
base_url = 'https://github.com/EltonDlamini97/LoanApplicationPics.git'

# Generate the URLs
df['Image_URL'] = df['Images'].apply(lambda x: base_url + os.path.basename(x))

# Save the updated dataset
df.to_csv('Images/ProjectFinalResult_with_URLs.csv', index=False)

