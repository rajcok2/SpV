RUBBER = 'icons/rubber.png'
LOGO = 'icons/logo.ico'

############ APP PROPERTIES ############

APP_NAME = "Kombinatorika hrou"
BACKGROUND_COLOR = "#B0C4DE"
HEAD_ICON = 'icons/codeSQL_icon.ico'
MIN_WIDTH = 650
MIN_HEIGHT = 600
INITIAL_SIZE_AND_POSITION = "650x600+200+50"
INITIAL_STATE = 'zoomed'

############ APP MENU ############

START = 'Začať'
MINIMIZE = 'Minimalizovať'
EXIT = 'Skončíť'

############ APP TOOLS ############

ACTIVE_TOOL_COLOR = 'red'

############ APP ASSIGNMENT ############

ASSIGNMENT = 'Najviac koľko rôznych {} vieš vytvoriť tak, že ani {} rovnako ako ostatné? ' \
             'Použi všetky farby na palete vpravo.'
BALL = 'loptičiek'
HOUSE = 'domčekov'
FLAG = 'vlajočiek'
MASCULINE = 'jeden nebude vyfarbený'
FEMININE = 'jedna nebude vyfarbená'


def get_spaced_colors(n): # funkcia na generovanie dakych farieb
    max_value = 16581375  # 255**3
    interval = int(max_value / n)
    colors = [hex(I)[2:].zfill(6) for I in range(0, max_value, interval)]
    done_colors = [(int(i[:2], 16), int(i[2:4], 16), int(i[4:], 16)) for i in colors]
    return "#%02x%02x%02x" % (done_colors[0]), "#%02x%02x%02x" % done_colors[1], "#%02x%02x%02x" % done_colors[2]


print(get_spaced_colors(5))

# otvorenie suboru a precitanie riadok po riadku
f = open("level.txt", "r")
for x in f:
  print(x.split())
