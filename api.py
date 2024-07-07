import requests
import subprocess
import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
response=requests.get('https://api.sportmonks.com/v3/football/fixtures?api_token=OLYEPNcms2LkmVGa9BQe80wxFRyDrNsBh5nwVE6oJqla3eZdJJAQnCSNRINy')
json_data=response.text

# Sample JSON data
data = json.loads(json_data)["data"]

# Create a PDF
pdf_filename = "matches_report.pdf"
c = canvas.Canvas(pdf_filename, pagesize=letter)
width, height = letter

# Add title
c.setFont("Helvetica-Bold", 16)
c.drawString(100, height - 50, "Matches Report")

# Set starting position for content
y = height - 80
c.setFont("Helvetica", 12)

for match in data:
    # Extract information
    name = match["name"]
    starting_at = datetime.strptime(match["starting_at"], '%Y-%m-%d %H:%M:%S').strftime('%B %d, %Y %H:%M')
    result_info = match["result_info"]

    # Write information to the PDF
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, y, name)
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(100, y, f"Date & Time: {starting_at}")
    y -= 20
    c.drawString(100, y, f"Result: {result_info}")
    y -= 40

    # Check if we need to add a new page
    if y < 50:
        c.showPage()
        y = height - 50

# Save the PDF
c.save()

print(f"PDF generated: {pdf_filename}")
subprocess.run(['python3', 'move.py'])