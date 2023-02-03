import re

import requests
import bs4

ASTRODX_TESTFLIGHT = "https://testflight.apple.com/join/rACTLjPL"
STATUS_REGEX = re.compile(r"!\[AstroDX TestFlight status\]\(https://img.shields.io/badge/.+\)")
STATUS_URLS = {
    "full": "https://img.shields.io/badge/testflight-full-red",
    "closed": "https://img.shields.io/badge/testflight-closed-yellow",
    "open": "https://img.shields.io/badge/testflight-open-green"
}


def main():
    page = requests.get(
        ASTRODX_TESTFLIGHT, 
        headers={
            "Accept-Language": "en-us"
        }
    ).text

    soup = bs4.BeautifulSoup(page, 'html.parser')
    status_text = soup.select(".beta-status span")[0].get_text()
    if "This beta is full." in status_text:
        status = "full"
    elif "This beta isn't accepting" in status_text:
        status = "closed"
    else:
        status = "open"
    
    with open("README.md", newline="\n") as f:
        readme = f.read()
    readme = STATUS_REGEX.sub(f"![AstroDX TestFlight status]({STATUS_URLS[status]})", readme)
    with open("README.md", "w", newline="\n") as f:
        f.write(readme)
    

if __name__ == "__main__":
    main()

    
