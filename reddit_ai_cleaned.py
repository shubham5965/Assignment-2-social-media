import json
import pandas as pd

# Function to load and clean the JSON data
def clean_reddit_data(file_name):
    # Load the JSON file
    with open(file_name, 'r') as file:
        data = json.load(file)
    
    # Convert to pandas DataFrame for easier manipulation
    df = pd.DataFrame(data)
    
    # Remove rows with missing values
    df.dropna(inplace=True)

    # Drop unnecessary columns if not required
    # For example, 'url', 'id', etc. Modify this based on the columns you don't need.
    df = df.drop(columns=['url', 'id'], errors='ignore')

    # Convert the 'created' column to a datetime format
    df['created'] = pd.to_datetime(df['created'], errors='coerce')

    # Filter posts where the score is greater than 3
    df = df[df['score'] > 1]

    # Reset index after cleaning and filtering
    df.reset_index(drop=True, inplace=True)

    # Save the filtered data back to a JSON file
    cleaned_file_name = file_name.replace(".json", "_filtered_cleaned.json")
    df.to_json(cleaned_file_name, orient='records', indent=4)
    
    print(f"Filtered and cleaned data saved to {cleaned_file_name}")
    print(f"Total rows after filtering: {len(df)}")
    return df

# Clean and filter both JSON files
reddit_future_jobs_cleaned = clean_reddit_data('reddit_ai_future_jobs_data.json')
reddit_jobs_large_cleaned = clean_reddit_data('reddit_ai_jobs_large_data.json')
