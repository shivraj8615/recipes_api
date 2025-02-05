from flask import Flask, request, jsonify, render_template_string
from recipes import recipes_1_cotton_dark, recipes_2_cotton_medium, recipes_3_cotton_light, recipes_4_polyester_dark, recipes_5_pc_dark, recipes_5_sample_shade
app = Flask(__name__)
@app.route('/get_recipe', methods=['GET'])
def get_recipe():
    fabric_type = request.args.get('fabric_type')  # Get fabric type from query params
    shade = request.args.get('shade')  # Get shade from query params
    
    # Check if fabric type and shade exist in the recipes dictionary
    if fabric_type == "Cotton" and shade== "dark":
        recipe = recipes_1_cotton_dark
        return jsonify(recipe)
    if fabric_type == "Cotton" and shade== "medium":
        recipe = recipes_2_cotton_medium
        return jsonify(recipe)
    if fabric_type == "Cotton" and shade== "light":
        recipe = recipes_3_cotton_light
        return jsonify(recipe)
      # Return the recipe as a JSON response
    if fabric_type == "Polyster" and  shade=="dark":
        recipe = recipes_4_polyester_dark
        return jsonify(recipe)
    if fabric_type == "Polycotton" and shade == "dark":
        recipe = recipes_5_pc_dark
        return jsonify(recipe)
    else:
        return jsonify({"error": "Recipe not found"}), 404  # Return an error if not found


if __name__ == '__main__':
    app.run()
