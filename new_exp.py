import os
import shutil
import sys

# --- CONFIGURATION ---
IMAGES_DIR  = 'images' 
TEMPLATE_DIR = 'templates'

# Source filenames (inside templates/)
SRC_SCRIPT = 'base_script.py'
SRC_LATEX  = 'report_template.tex' 

# Destination filenames (inside the new experiment folder)
DST_SCRIPT = 'analysis.py'
DST_LATEX  = 'report.tex'

def main():
    # 1. Check if templates exist
    if not os.path.isdir(TEMPLATE_DIR):
        print(f"Error: '{TEMPLATE_DIR}' directory not found.")
        return

    # 2. Get experiment name (via argument or input)
    if len(sys.argv) > 1:
        exp_name = sys.argv[1]
    else:
        exp_name = input("Enter experiment name (e.g., exp01-speed-of-light): ").strip()

    if not exp_name:
        print("Invalid name.")
        return

    # Sanitize name (lowercase, no spaces)
    folder_name = exp_name.lower().replace(" ", "-")

    # 3. Create Directory
    if os.path.exists(folder_name):
        print(f"Warning: Folder '{folder_name}' already exists.")
        if input("Continue? (y/n): ").lower() != 'y':
            return
    else:
        os.makedirs(folder_name)

    # 4. Copy Files
    try:
        # Copy Python Script
        shutil.copy(os.path.join(TEMPLATE_DIR, SRC_SCRIPT), 
                    os.path.join(folder_name, DST_SCRIPT))
        
        # Copy LaTeX Report
        shutil.copy(os.path.join(TEMPLATE_DIR, SRC_LATEX), 
                    os.path.join(folder_name, DST_LATEX))
        
        shutil.copytree(os.path.join(TEMPLATE_DIR, IMAGES_DIR), 
                    os.path.join(folder_name, IMAGES_DIR))
        
        # Create empty CSV
        with open(os.path.join(folder_name, 'data.csv'), 'w') as f:
            f.write("x,y,y_err\n")

        print(f"✅ Setup complete for '{folder_name}'")
        print(f"   cd {folder_name}")

    except FileNotFoundError as e:
        print(f"Error: Missing template file. {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
