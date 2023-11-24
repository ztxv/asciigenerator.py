import pyfiglet

def ascii_art(text, font):
    ascii_art = pyfiglet.figlet_format(text, font=font)
    print(ascii_art)
    again()

def caligraphy():
    text = input("Enter Text for Caligraphy ASCII art: ")
    ascii_art(text, font='caligraphy')

def ogre():
    text = input("Enter Text for Ogre ASCII art: ")
    ascii_art(text, font='ogre')
    again()

def pawp():
    text = input("Enter Text for Pawp ASCII art: ")
    ascii_art(text, font='pawp')
    again()

def rectangles():
    text = input("Enter Text for Rectangles ASCII art: ")
    ascii_art(text, font='rectangles')
    again()




def amcaaa01():
    text = input("Enter Text for AMC AAA01 ASCII art: ")
    ascii_art(text, font='amcaaa01')
    again()

def amcblock():
    text = input("Enter Text for AMC Block ASCII art: ")
    ascii_art(text, font='amcblock')
    again()

def amcneko():
    text = input("Enter Text for AMC Neko ASCII art: ")
    ascii_art(text, font='amcneko')
    again()

def banner():
    text = input("Enter Text for Banner ASCII art: ")
    ascii_art(text, font='banner')
    again()

def slant():
    text = input("Enter Text for Slant ASCII art: ")
    ascii_art(text, font='slant')
    again()

def block():
    text = input("Enter Text for Block ASCII art: ")
    ascii_art(text, font='block')
    again()

def script():
    text = input("Enter Text for Script ASCII art: ")
    ascii_art(text, font='script')
    again()

def bubble():
    text = input("Enter Text for Bubble ASCII art: ")
    ascii_art(text, font='bubble')
    again()

def digital():
    text = input("Enter Text for Digital ASCII art: ")
    ascii_art(text, font='digital')
    again()

def mini():
    text = input("Enter Text for Mini ASCII art: ")
    ascii_art(text, font='mini')
    again()

def alligator():
    text = input("Enter Text for Alligator ASCII art: ")
    ascii_art(text, font='alligator')
    again()

def graffiti():
    text = input("Enter Text for Graffiti ASCII art: ")
    ascii_art(text, font='graffiti')
    again()

def rowancap():
    text = input("Enter Text for Rowan Cap ASCII art: ")
    ascii_art(text, font='rowancap')
    again()


def larry3d():
    text = input("Enter Text for Larry 3D ASCII art: ")
    ascii_art(text, font='larry3d')
    again()

def speed():
    text = input("Enter Text for Speed ASCII art: ")
    ascii_art(text, font='speed')
    again()

def stellar():
    text = input("Enter Text for Stellar ASCII art: ")
    ascii_art(text, font='stellar')
    again()

def big():
    text = input("Enter Text for Big ASCII art: ")
    ascii_art(text, font='big')
    again()

def weird():
    text = input("Enter Text for Weird ASCII art: ")
    ascii_art(text, font='weird')
    again()

def alphabet():
    text = input("Enter Text for Alphabet ASCII art: ")
    ascii_art(text, font='alphabet')
    again()

def isometric():
    text = input("Enter Text for Isometric ASCII art: ")
    ascii_art(text, font='isometric1')
    again()

def nancyj():
    text = input("Enter Text for Nancyj ASCII art: ")
    ascii_art(text, font='nancyj')
    again()

def poison():
    text = input("Enter Text for Poison ASCII art: ")
    ascii_art(text, font='poison')
    again()

def rammstein():
    text = input("Enter Text for Rammstein ASCII art: ")
    ascii_art(text, font='rammstein')
    again()

def s_relief():
    text = input("Enter Text for S-Relief ASCII art: ")
    ascii_art(text, font='s-relief')
    again()

def santaclara():
    text = input("Enter Text for Santa Clara ASCII art: ")
    ascii_art(text, font='santaclara')
    again()

def speed():
    text = input("Enter Text for Speed ASCII art: ")
    ascii_art(text, font='speed')
    again()

def spliff():
    text = input("Enter Text for Spliff ASCII art: ")
    ascii_art(text, font='spliff')
    again()

def term():
    text = input("Enter Text for Term ASCII art: ")
    ascii_art(text, font='term')
    again()

def thick():
    text = input("Enter Text for Thick ASCII art: ")
    ascii_art(text, font='thick')
    again()

def usfl01():
    text = input("Enter Text for USFL01 ASCII art: ")
    ascii_art(text, font='usfl01')
    again()


def again():
    print("\nY | N ")
    yorn = input("Go Again?: ")
    if yorn.lower() == "y":
        ask()
    elif yorn.lower() == "n":
        exit()
    else:
        again()


def ask():
    available_fonts = [
        "caligraphy", "ogre", "pawp", "rectangles","banner", "slant", "block",
        "script", "bubble", "digital", "mini", "alligator",
        "graffiti", "rowancap", "larry3d", "speed",
        "stellar", "big", "weird", "alphabet", "digital", "isometric",
        "nancyj", "poison", "rammstein", "s-relief", "santaclara",
        "speed", "spliff", "term", "thick", "usfl01", "usaflag",
        "weird",
    ]

    print("\nAvailable Fonts:")
    for font in available_fonts:
        print(font, end=", ")

    which_font = input("\n\nWhat ASCII font would you like to use?: ")

    if which_font.lower() in available_fonts:
        globals()[which_font.lower()]()
    else:
        print("Not a valid option.")
        ask()

ask()
