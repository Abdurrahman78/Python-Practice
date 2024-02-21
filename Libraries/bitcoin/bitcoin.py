

import sys
import json
import requests

try:

    if len(sys.argv)==1:
        sys.exit("Missing command-line argument")
    elif len(sys.argv)==2:
       try:
           value=float(sys.argv[1])
       except ValueError:
           sys.exit("Command-line argument is not a number")
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    object=response.json()
    currentPrice=object["bpi"]["USD"]["rate_float"]
    print(f"${currentPrice*value:,.4f}")


except requests.RequestException:
    pass

