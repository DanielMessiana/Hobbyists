import pandas as pd
import json

print('Starting script')

# Read the Excel file into a DataFrame
df = pd.read_excel('C:/Users/Pokev/OneDrive/Desktop/Hobbyists/scripts/hobby_data.xlsx', usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

df.dropna(inplace=True)

# Convert the DataFrame to a list of dictionaries
hobbies = df.to_dict(orient='records')

# Add the Django model and primary key fields to each dictionary
for i, hobby in enumerate(hobbies):
    hobby['model'] = 'survey.hobby'
    hobby['pk'] = i + 1

# Write the hobby data to a JSON file
with open('hobby_data.json', 'w') as f:
    json.dump(hobbies, f, indent=4)