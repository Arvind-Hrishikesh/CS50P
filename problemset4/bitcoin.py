import requests
import sys

def main():
    if len(sys.argv)<2:
        sys.exit("Missing command-line argument")
    try:
        n=float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    try:
        response=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit()
    else:
        btc_dict=response.json()["bpi"]
        btc_price=btc_dict["USD"]["rate"].replace(",","")
        Total="{:,}".format((n*float(btc_price)))
        print(f"${Total}")


if __name__=="__main__":
    main()