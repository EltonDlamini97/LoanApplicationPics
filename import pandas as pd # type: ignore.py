import pandas as pd # type: ignore
import os

# Load the dataset
dataset_path = 'Images/ProjectFinalResult.csv'
df = pd.read_csv(dataset_path, delimiter=';')

# Define the base URL
base_url = 'https://raw.githubusercontent.com/EltonDlamini97/LoanApplicationPics/main/'

# Generate the URLs
df['Image_URL'] = df['Images'].apply(lambda x: base_url + os.path.basename(x))

# Save the updated dataset
df.to_csv('LoanApplicationPic/ProjectFinalResult_URLs.csv', index=False)

