from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import json

app = FastAPI()

# CORS middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this if you want to restrict allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Paths for CSV and JSON files
csv_file_path = 'D:/everythingfromc/projects/login/Assignement/recipe-search-backend/epi_r.csv'
json_file_path = 'D:/everythingfromc/projects/login/Assignement/recipe-search-backend/updated_recipes.json'

# Load CSV file into a DataFrame at startup and add 'id' column if not present
df = pd.read_csv(csv_file_path)

# Add 'id' column if it doesn't exist
if 'id' not in df.columns:
    df.reset_index(drop=True, inplace=True)  # Ensure the index is 0-based
    df.index.name = 'id'
    df.reset_index(inplace=True)

@app.get("/search")
async def search(q: str = Query(..., description="Search query")):
    # Filter the DataFrame based on the 'title' column
    results = df[df['title'].str.contains(q, case=False, na=False)]
    
    if results.empty:
        return {"message": "No results found"}
    
    # Convert the result to a list of dictionaries and extract the first match
    result_list = results.to_dict(orient='records')
    
    # Extract the 'id' of the first match
    result_id = result_list[0]['id']
    
    # Load the JSON file
    with open(json_file_path, 'r') as f:
        full_recipes = json.load(f)
    
    # Search for the recipe with the matching 'id' in the JSON
    matching_recipe = next((recipe for recipe in full_recipes if recipe['id'] == result_id), None)
    
    if matching_recipe:
        # Print the matching recipe in the backend terminal
        print(f"Matching recipe found: {matching_recipe}")
    else:
        matching_recipe = {"message": "No matching recipe found in JSON."}
    
    # Return both the search result and the matching recipe
    return {
        "search_results": result_list,
        "matching_recipe": matching_recipe
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
