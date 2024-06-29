import subprocess
import sys

# List of required libraries
required_libraries = [
    "wikipedia-api", "pyjokes", "beautifulsoup4", "pywikihow", "pywhatkit", 
    "pillow", "py-cpuinfo", "psutil", "newsapi-python", "speedtest-cli", "requests", "PyPDF2"
]

# Function to check if a library is installed
def is_installed(library):
    try:
        __import__(library)
        return True
    except ImportError:
        return False

# Mapping for libraries with different import names
import_name_mapping = {
    "wikipedia-api": "wikipedia",
    "beautifulsoup4": "bs4",
    "newsapi-python": "newsapi",
    "py-cpuinfo": "cpuinfo"
}

# Install missing libraries
for library in required_libraries:
    import_name = import_name_mapping.get(library, library)
    if not is_installed(import_name):
        print(f"Installing {library}...")
        result = subprocess.run([sys.executable, "-m", "pip", "install", library], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Failed to install {library}. Error: {result.stderr}")
        else:
            print(f"Successfully installed {library}.")
