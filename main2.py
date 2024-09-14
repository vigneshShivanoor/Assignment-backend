from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import requests
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

# OpenSearch details
opensearch_url = "https://localhost:9200/recipes/_search"
auth = ("admin", "Vignesh@123")

# Paths for JSON file
json_file_path = 'D:/everythingfromc/projects/login/Assignement/recipe-search-backend/updated_recipes.json'

@app.get("/search")
async def search(q: str = Query(..., description="Search query")):
    # Define the query for OpenSearch
    search_query = {
        "query": {
            "match": {
                "title": q
            }
        }
    }
    
    # Send the query to OpenSearch
    response = requests.get(opensearch_url, auth=auth, json=search_query, verify=False)
    
    if response.status_code == 200:
        search_results = response.json()
    else:
        return {"message": f"Error querying OpenSearch: {response.status_code}"}
    
    # Extract the IDs from the search results
    hits = search_results.get('hits', {}).get('hits', [])
    result_ids = [hit['_id'] for hit in hits]
    
    if not result_ids:
        return {"message": "No results found in OpenSearch"}
    
    # Load the JSON file
    with open(json_file_path, 'r') as f:
        full_recipes = json.load(f)
    
    # Search for recipes with the matching 'id' in the JSON
    matching_recipes = [recipe for recipe in full_recipes if recipe['id'] in result_ids]
    
    if matching_recipes:
        # Print the matching recipes in the backend terminal
        print(f"Matching recipes found: {matching_recipes}")
    else:
        matching_recipes = {"message": "No matching recipes found in JSON."}
    
    # Return both the search result and the matching recipes
    return {
        "search_results": hits,
        "matching_recipes": matching_recipes
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
