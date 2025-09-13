# --------------------------------------------
# Imports
# --------------------------------------------
import subprocess
import sys
import pathlib
from utils_logger import logger

# --------------------------------------------
# Function to run scripts
# --------------------------------------------
def run_scripts():
    scripts = [
        "tmartin_get_csv.py",
        "tmartin_get_excel.py",
        "tmartin_get_json.py",
        "tmartin_get_text.py",        
        "tmartin_process_csv.py",
        "tmartin_process_excel.py",
        "tmartin_process_json.py",
        "tmartin_process_text.py"     
    ]

    # Run each script one by one
    for script in scripts:
        logger.info(f"Running {script}...")
        try:
            # Use sys.executable so subprocess uses the SAME Python as this venv
            subprocess.run([sys.executable, script], check=True)
            logger.info(f"✅ {script} completed successfully.")
        except subprocess.CalledProcessError as e:
            logger.error(f"❌ Error running {script}: {e}")

# --------------------------------------------
# Main Execution
# --------------------------------------------
if __name__ == "__main__":
    logger.info("Starting main script execution...")
    run_scripts()
    logger.info("All scripts processed.")
