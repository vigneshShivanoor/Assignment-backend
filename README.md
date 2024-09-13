Recipe Search Platform


Project Description and Objectives
The Recipe Search Platform is a full-stack web application that allows users to search for various recipes by name. The application is built with React.js for the frontend, while the backend (implemented with a Python framework) handles search functionality using OpenSearch for efficient recipe retrieval. The platform provides a clean, user-friendly interface where users can search, view, and explore detailed recipe information, including ingredients, directions, and nutritional information. The main goal is to help users find recipes quickly and easily while offering an intuitive browsing experience.

Objectives:
Develop a fast and responsive recipe search platform.
Efficiently index and retrieve recipe data using OpenSearch.
Provide a clean and intuitive UI for users to browse recipes.
Display detailed recipe information such as ingredients, directions, and nutrition.
Setup and Installation Instructions
1. Clone the repository:
bash
Copy code
git clone https://github.com/vigneshShivanoor/Assignment-frontend.git
2. Backend Setup:
Install Python and Virtual Environment:
Make sure you have Python 3 installed. Set up a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
Install Dependencies:
Navigate to the backend directory and install required packages
pip install unicorn

bash
Copy code
cd backend
pip install -r requirements.txt
Run the Backend:
Make sure your backend server is running:

bash
Copy code
python main1.py
This will start the backend server at http://localhost:8000/.

3. Frontend Setup:
Install Node.js and npm:
Ensure that you have Node.js and npm installed on your machine.

Install Frontend Dependencies:
Navigate to the frontend directory and install dependencies:
npm install axios

bash
Copy code
cd frontend
npm install
Run the Frontend:
Start the React development server:

bash
Copy code
npm start
This will run the frontend server at http://localhost:3000/.

Usage Guidelines
Searching for Recipes:
On the homepage, enter a recipe name in the search box.
Click the Search button to initiate a search.
The search results will display a table of matching recipes, showing relevant details such as ingredients, calories, and other nutritional information.


Detailed View:
If you click on a specific recipe, detailed information such as directions, ingredients, rating, calories, and more will be shown.
Technologies and Frameworks Used

Frontend:
React.js: The main framework for building the UI.
Axios: For making HTTP requests to the backend.
CSS: For styling the application, ensuring a responsive and user-friendly design.

Backend:
Python (with Flask/Django/FastAPI): Handles recipe search queries and serves data to the frontend.
OpenSearch: A search engine based on Elasticsearch, used for indexing and searching recipe data.

Youtube: https://youtu.be/MHwA4PsBUbE
