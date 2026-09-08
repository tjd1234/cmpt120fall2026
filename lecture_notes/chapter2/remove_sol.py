# remove_sol.py

#
# This takes a .ipynb as input and prints a version of the notebook with the
# solution cells removed, i.e. all the cells with the tag "solution". 
#

import json
import sys
import os

def remove_sol(fname):
    # Read the notebook as JSON
    with open(fname, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # Filter out cells tagged with 'solution'
    # The notebook structure has a 'cells' array, and each cell has metadata
    nb['cells'] = [cell for cell in nb['cells'] 
        if not (cell.get('metadata', {}).get('tags') and 'solution' in cell['metadata']['tags'])]
    
    # Print the modified notebook content to screen
    print(json.dumps(nb, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python remove_sol.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    remove_sol(input_file)
