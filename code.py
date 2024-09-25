#MATRIXPORTAL S3 with ADAFRUIT 64x32 with 3mm pitch RGB BOARD and CIRCUITPYTHON 9.0x
# SPDX-License-Identifier: MIT

import time
import board
import terminalio
from adafruit_matrixportal.matrixportal import MatrixPortal

#API DOC: https://finnhub.io/docs/api/quote
#API DOC Response Attributes: c Current price, d Change, dp Percent change, h High price of the day, l Low price of the day, o Open price of the day, pc Previous close price

# ------- INPUT INPUT INPUT INPUT INPUT INPUT ------ TICKER SYMBOL SELECTION
TICKER = "BA"


#FINNHUB API PULL INFORMATION
DATA_SOURCE = "https://finnhub.io/api/v1/quote?symbol=" + TICKER + "&token=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX "          #REPLACE XXXXXXXXXX with your TOKEN from FINNHUB

#DEFINE FINHUB API DATA POINTS
DATA_LOCATION1 = ["c"]   #See API DOC Response Attributes above
DATA_LOCATION2 = ["d"]   #See API DOC Response Attributes above
DATA_LOCATION3 = ["dp"]   #See API DOC Response Attributes above
DATA_LOCATION4 = ["h"]   #See API DOC Response Attributes above
DATA_LOCATION5 = ["l"]   #See API DOC Response Attributes above
DATA_LOCATION6 = ["o"]   #See API DOC Response Attributes above
DATA_LOCATION7 = ["pc"]   #See API DOC Response Attributes above

#Add info to the JSON Data for presentation on board
#%d represents a decimal integer, %f represents a floating-point number, and %c represents a character.
# .2 after % if number of decimals. "%g" will automatically choose either standard decimal notation or scientific notation (depending on the size of the number) to display the most compact form

def text_Current(val):                             # $DATA_LOCATION1 presentation on board
    return TICKER+" $%.1f" % val

def text_Change(val):                              # $DATA_LOCATION2 presentation on board
    return "Chng$ %.1f" % val

def text_PrcntChange(val):                         # $DATA_LOCATION3 presentation on board
    return "Chng% "+"%.1f" % val

def text_High(val):                                # $DATA_LOCATION4 presentation on board
    return "Hi $%.1f" % val

def text_Low(val):                                 # $DATA_LOCATION5 presentation on board
    return "Lo $%.1f" % val


# the current working directory (where this file is)
cwd = ("/" + __file__).rsplit("/", 1)[0]


matrixportal = MatrixPortal(
    url=DATA_SOURCE,
    json_path=(DATA_LOCATION1, DATA_LOCATION2,DATA_LOCATION3, DATA_LOCATION4,DATA_LOCATION5, DATA_LOCATION6,DATA_LOCATION7),
    status_neopixel=board.NEOPIXEL,
    debug=False,
)


#TEXT FONT and COLOR, AND POSITION ON BOARD

matrixportal.add_text(
    text_font=terminalio.FONT,              #Font Choice
    text_position=(1, 5),                   #Pixel position on display
    text_color=0x4b0082,
    text_transform=text_Current,          #Selected defined DATA_LOCATION from above
)

matrixportal.add_text(
    text_font=terminalio.FONT,              #Font Choice
    text_position=(1, 15),                   #Pixel position on display          #SET TO 100 - NOT ON SCREEN
    text_color=0x0000FF,
    text_transform=text_Change,          #Adds in the currency symbol
)

matrixportal.add_text(
    text_font=terminalio.FONT,              #Font Choice
    text_position=(1, 25),                   #Pixel position on display            #SET TO 100 - NOT ON SCREEN
    text_color=0xFF0000,
    text_transform=text_PrcntChange,          #Adds in the currency symbol
)

matrixportal.add_text(
    text_font=terminalio.FONT,              #Font Choice
    text_position=(100, 15),                   #Pixel position on display
    text_color=0x00FF00,
    text_transform=text_High,          #Adds in the currency symbol
)

matrixportal.add_text(
    text_font=terminalio.FONT,              #Font Choice
    text_position=(100, 25),                   #Pixel position on display
    text_color=0x0000FF,
    text_transform=text_Low,          #Adds in the currency symbol
)

matrixportal.preload_font(b"$012345789")  # preload numbers
matrixportal.preload_font((0x00A3, 0x20AC))  # preload gbp/euro symbol

while True:
    try:
        value = matrixportal.fetch()
        print("Response is", value)
    except (ValueError, RuntimeError) as e:
        print("Some error occured, retrying! -", e)

# ------- INPUT INPUT INPUT INPUT INPUT INPUT ------ SECONDS TO REFRESH
    time.sleep(60)
