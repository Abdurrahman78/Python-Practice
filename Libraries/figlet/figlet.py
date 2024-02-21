# implement a program that:

# Expects zero or two command-line arguments:
            # Zero if the user would like to output text in a random font.
            # Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.

# Prompts the user for a str of text.
# Outputs that text in the desired font.

import sys
from pyfiglet import Figlet
import random

figlet=Figlet()

list=figlet.getFonts()

if len(sys.argv) == 1:
    answer=input("Input: ")
    randomFonts=figlet.getFonts()
    choices=random.choice(randomFonts)
    figlet.setFont(font=choices)
    print(figlet.renderText(answer))

elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and (sys.argv[2] in list):
    answer=input("Input: ")
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(answer))

else:
    sys.exit("Invalid usage")



