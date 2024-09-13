import pandas as pd
import json

# Load the CSV file into a DataFrame
csv_file = 'epi_r.csv'  # Replace with your CSV file path
df = pd.read_csv(csv_file)

# Add an 'id' column to the DataFrame
df.reset_index(drop=True, inplace=True)
df.index.name = 'id'
df.reset_index(inplace=True)

# Convert the DataFrame to a list of dictionaries
data = df.to_dict(orient='records')

# Write the list of dictionaries to a JSON file
json_file = 'output.json'  # Replace with your desired output file path
with open(json_file, 'w') as f:
    json.dump(data, f, indent=4)

print(f'CSV file has been converted to JSON and saved as {json_file}')
