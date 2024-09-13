import json

def add_ids_to_recipes(json_data):
    # Add 'id' to each recipe in the list
    for index, recipe in enumerate(json_data):
        recipe['id'] = index
    return json_data

def update_recipes_json(input_file, output_file):
    # Read the JSON data from the input file
    with open(input_file, 'r') as infile:
        recipes_json = json.load(infile)
    
    # Add IDs to the recipes
    updated_recipes_json = add_ids_to_recipes(recipes_json)
    
    # Write the updated JSON data to the output file
    with open(output_file, 'w') as outfile:
        json.dump(updated_recipes_json, outfile, indent=4)

# Example usage:
input_file = 'full_format_recipes.json'  # Replace with the path to your input JSON file
output_file = 'updated_recipes.json'  # Replace with the desired output file path

update_recipes_json(input_file, output_file)
