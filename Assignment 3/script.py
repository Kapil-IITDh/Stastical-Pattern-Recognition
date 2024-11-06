import json
import base64

# Load the notebook file
with open('Univariate.ipynb', 'r') as f:
    notebook_content = json.load(f)
z =0
# Loop through each cell in the notebook
for cell in notebook_content['cells']:
    if cell['cell_type'] == 'code':
        for output in cell.get('outputs', []):
            if 'data' in output and 'image/png' in output['data']:
                img_data = output['data']['image/png']
                img_name = f"image_{notebook_content['cells'].index(cell)}_{z}.png"
                
                # Decode the base64 image data and save it to a file
                with open(img_name, 'wb') as img_file:
                    img_file.write(base64.b64decode(img_data))
                
                print(f"Saved {img_name}")
                z+=1