from pymongo import MongoClient
import pandas as pd

# Connect to MongoDB (adjust the URI as needed)
client = MongoClient('mongodb://localhost:27017/')
db = client['DisasterResponseDB']  # Database name
collection = db['EmergencyPosts']  # Collection name

# Extract data from MongoDB
data = list(collection.find())

# Convert MongoDB data to a Pandas DataFrame
df = pd.DataFrame(data)

# Drop the '_id' column if it exists, as it may cause issues in Power BI
if '_id' in df.columns:
    df = df.drop(columns=['_id'])

# Save the DataFrame to a CSV file
df.to_csv('extracted_data.csv', index=False)

print("Data extracted and saved to extracted_data.csv")
