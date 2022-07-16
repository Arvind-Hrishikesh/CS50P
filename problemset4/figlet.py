from pyfiglet import Figlet
import random
import sys
figlet=Figlet()

list_of_fonts=figlet.getFonts()

if len(sys.argv)>1:
    if sys.argv[1]=="-f" or sys.argv[1]=="--font":
        if sys.argv[2] in list_of_fonts:
            figlet.setFont(font=sys.argv[2])
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
else:
    f=random.choice(list_of_fonts)
    figlet.setFont(font=f)

x=input("Input: ")
print(figlet.renderText(x))

