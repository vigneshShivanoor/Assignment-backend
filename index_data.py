# import json
# from opensearchpy import OpenSearch


# client = OpenSearch(
#     hosts=[{'host': 'localhost', 'port': 9200}],
#     http_compress=True,
# )

# INDEX_NAME = "recipes"


# def create_index():
#     if not client.indices.exists(INDEX_NAME):
#         index_body = {
#             "settings": {
#                 "index": {
#                     "number_of_shards": 1,
#                     "number_of_replicas": 0
#                 }
#             },
#             "mappings": {
#                 "properties": {
#                     "recipe_name": {"type": "text"},
#                     "description": {"type": "text"}
#                 }
#             }
#         }
#         client.indices.create(index=INDEX_NAME, body=index_body)
#         print(f"Index '{INDEX_NAME}' created.")
#     else:
#         print(f"Index '{INDEX_NAME}' already exists.")


# def index_data():
#     with open("recipes.json", "r") as file:
#         recipes = json.load(file)
#         for recipe in recipes:
#             response = client.index(index=INDEX_NAME, body=recipe)
#             print(f"Indexed recipe: {recipe['recipe_name']}")

# if __name__ == "__main__":
#     create_index()
#     index_data()


from opensearchpy import OpenSearch

client = OpenSearch(
    hosts=[{'host': 'localhost', 'port': 9200}],
    http_compress=True
)

# Test a simple ping
if client.ping():
    print("Connected successfully!")
else:
    print("Failed to connect.")
