import pandas as pd
import json

# Read the Excel file
df = pd.read_excel('Pasco items.xlsx')

# Convert the dataframe to a list of dictionaries
data = df.to_dict(orient='records')

# Function to convert non-serializable objects
def convert_to_serializable(obj):
  if isinstance(obj, pd.Timestamp):
    return obj.isoformat()
  raise TypeError("Type not serializable")

# Convert to JSON
json_data = json.dumps(data, indent=4, default=convert_to_serializable)

# Save JSON to file
with open('data.json', 'w') as json_file:
  json_file.write(json_data)