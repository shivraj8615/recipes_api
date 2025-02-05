from flask import Flask, request, jsonify
import json
from recipes import (
    recipes_1_cotton_dark,
    recipes_2_cotton_medium,
    recipes_3_cotton_light,
    recipes_4_polyester_dark,
    recipes_5_pc_dark,
)

app = Flask(__name__)

# Mapping of fabric types and shades to their corresponding recipe variables
recipes_dict = {
    ("cotton", "dark"): recipes_1_cotton_dark,
    ("cotton", "medium"): recipes_2_cotton_medium,
    ("cotton", "light"): recipes_3_cotton_light,
    ("polyester", "dark"): recipes_4_polyester_dark,
    ("polycotton", "dark"): recipes_5_pc_dark,
}

@app.route('/get_recipe', methods=['GET'])
def get_recipe():
    # Get parameters, strip whitespaces, and make lowercase to avoid case issues
    fabric_type = request.args.get('fabric_type', '').strip().lower()
    shade = request.args.get('shade', '').strip().lower()

    # Validate that both parameters are provided
    if not fabric_type or not shade:
        return jsonify({"error": "Both 'fabric_type' and 'shade' parameters are required."}), 400

    # Check if the requested fabric type and shade exist in our dictionary
    recipe = recipes_dict.get((fabric_type, shade))
    if recipe:
        return app.response_class(
            response=json.dumps(recipe, indent=4),  # Pretty JSON format
            mimetype='application/json'
        )
    else:
        return jsonify({"error": f"Recipe not found for fabric '{fabric_type}' and shade '{shade}'"}), 404

if __name__ == '__main__':
    app.run()

