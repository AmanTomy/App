import shutil
import os

# Current directory where your script is located
current_directory = os.getcwd()

# Source path (path to the PDF file)
source_path = os.path.join(current_directory,'matches_report.pdf')

# Destination path (where you want to move the PDF)
destination_path = os.path.join(current_directory,'data')

# Move the file
shutil.move(source_path, destination_path)