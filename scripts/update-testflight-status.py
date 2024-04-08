import re
from urllib.parse import quote

import bs4
import requests

ASTRODX_TESTFLIGHT = "https://testflight.apple.com/join/rACTLjPL"
ASTRODX_TESTFLIGHTS = {
    "Group A": "https://testflight.apple.com/join/rACTLjPL",
    "Group B": "https://testflight.apple.com/join/ocj3yptn",
    "Group C": "https://testflight.apple.com/join/CuMxZE2M",
}
STATUS_URLS = {
    "full": "https://img.shields.io/badge/{name}-full-red",
    "closed": "https://img.shields.io/badge/{name}-closed-yellow",
    "open": "https://img.shields.io/badge/{name}-open-green"
}


def main():
    with open("README.md", newline="\n") as f:
        readme = f.read()

    statuses = {}
    for name, link in ASTRODX_TESTFLIGHTS.items():
        page = requests.get(
            link,
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

        statuses[name] = status

        status_url = STATUS_URLS[status].format(name=quote(name))

        regex = re.compile(f"!\\[AstroDX {name} TestFlight status\\]\\(https://img.shields.io/badge/.+?\\)")
        readme = regex.sub(f"![AstroDX {name} TestFlight status]({status_url})", readme)

    with open("README.md", "w", newline="\n") as f:
        f.write(readme)

    str_status = ", ".join([f"{name}: {value}" for name, value in statuses.items()])
    print(f"status={str_status}")


if __name__ == "__main__":
    main()


