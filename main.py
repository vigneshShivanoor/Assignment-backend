from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# CORS middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this if you want to restrict allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Load CSV file into a DataFrame at startup
csv_file_path = 'D:/everythingfromc/projects/login/Assignement/recipe-search-backend/epi_r.csv'
df = pd.read_csv(csv_file_path)

@app.get("/search")
async def search(q: str = Query(..., description="Search query")):
    # Filter the DataFrame based on the 'title' column
    results = df[df['title'].str.contains(q, case=False, na=False)]
    
    if results.empty:
        return {"message": "No results found"}
    
    # Convert the result to a list of dictionaries
    return results.to_dict(orient='records')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
