import os
import sys
import subprocess

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Run the Streamlit app
if __name__ == "__main__":
    # Use the current Python interpreter to run Streamlit
    subprocess.run([sys.executable, "-m", "streamlit", "run", "src/app.py"])
