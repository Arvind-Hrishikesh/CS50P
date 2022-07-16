from fpdf import FPDF,YPos,XPos

pdf = FPDF(orientation="portrait", format="A4")
pdf.add_page(format=(210,297))
pdf.set_font("helvetica", "B", 16)
pdf.image("shirtificate.png", h=pdf.eph, w=pdf.epw)
pdf.cell(w=0,h=16,new_x=XPos.RIGHT,new_y=YPos.TOP)
pdf.cell(w=0,h=16,txt="Arvind took CS50")
##pdf.cell(210, 297, "CS50 Shirtificate")
pdf.output("shirtificate.pdf")