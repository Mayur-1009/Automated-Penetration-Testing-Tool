from reportlab.pdfgen import canvas

def generate_report(filename, results):
    c = canvas.Canvas(filename)
    c.drawString(100, 750, "Automated Penetration Testing Report")
    
    y = 700
    for category, data in results.items():
        c.drawString(100, y, f"{category}: {data}")
        y -= 30

    c.save()
