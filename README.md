# MatrixPortal-S3-Stock-Ticker

I used MarioCruz's MatrixPortal M4/CircuitPython 6.0x code (https://github.com/MarioCruz/MatrixPortalStockTicker) as a baseline and updated to get it working on MatrixPortal S3. Also I removed the scrolling feature as it didn't fit my use case for a single stock ticker. 

Choose three of the following to display: current price/$ change/% change/high price/low price/open price/prior day close price via Finnio API. 

Prerequisites to get your MatrixPortal S3 found on Adafruit Learn's site: https://learn.adafruit.com/adafruit-matrixportal-s3/overview

Instructions to get stock ticker working on MatrixPortal S3:

1) Extract the contents of the zip. This includes the code.py / lib / font files,
2) Copy and paste these files onto your MatrixPortal S3's 'CIRCUITPY (X:)' drive,
3) Signup for an account on https://finnhub.io/ and get your free API Key,
4) In MU, or some other editor, open the CODE.PY and:
   A) Change the Stock Ticker to your choice (default is 'BA"), and
   B) Copy your finnhub.io API key and paste it over the XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX in line 17 of the code,
   C) Choose how many seconds between pricing updates on Line 108; is set to 1min @ 60,
   D) Save and close CODE.PY.
6) In Notepad, open the settings.toml file and fill in the below, and then close and save.
   CIRCUITPY_WIFI_SSID = "WIFI_NAME"
   CIRCUITPY_WIFI_PASSWORD = "WIFI_PASSWORD"

Customize:
Lines 28 - 45 of Code.py allows you adjust how the API pulled figures are presented on your board.
Lines 60 - 95 of Code.py allows you adjust where the three of the five datapoints are presnted on the board. To keep things easy, for the two of the five data points that don't fit on the display - I've set them to vertical pixel 100 - a location off of the board.
  

Example 1:

![MatrixPortalS3 Ticker Ex1](https://github.com/user-attachments/assets/fea9fcbf-823d-41c3-b4c4-6420c2a6bb0e)

Example 2:

![MatrixPortalS3 Ticker Ex2](https://github.com/user-attachments/assets/aeb2fe75-f86b-4d49-84c1-8944ecde4b31)


