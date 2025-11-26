# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "beautifulsoup4==4.11.2",
#     "requests==2.31.0",
# ]
# ///
import re
from urllib.parse import quote

import bs4
import requests

ASTRODX_TESTFLIGHT = "https://testflight.apple.com/join/rACTLjPL"
ASTRODX_TESTFLIGHTS = {
    # "Group A (Kumoumi)": "https://testflight.apple.com/join/d7rx8Gce",
    # "Group B (Kumoumi)": "https://testflight.apple.com/join/vZkqCBaW",
    # "Group C (Kumoumi)": "https://testflight.apple.com/join/6ySgqPyW",
    # "Group D (Kumoumi)": "https://testflight.apple.com/join/71vbKTKq",
    # "Group E (Kumoumi)": "https://testflight.apple.com/join/AYFe4Qyh",
    # "Group F (Kumoumi)": "https://testflight.apple.com/join/yFhEejR9",
    # "Group G (Kumoumi)": "https://testflight.apple.com/join/d67RmvFG",
    # "Group H (Kumoumi)": "https://testflight.apple.com/join/taNXJKTM",
    "Group A (JiNALE)": "https://testflight.apple.com/join/rACTLjPL",
    "Group B (JiNALE)": "https://testflight.apple.com/join/ocj3yptn",
    "Group C (JiNALE)": "https://testflight.apple.com/join/CuMxZE2M",
    "Group D (JiNALE)": "https://testflight.apple.com/join/T6qKfV6f",
    "Group E (JiNALE)": "https://testflight.apple.com/join/sMm1MCYc",
}
STATUS_URLS = {
    "full": "https://img.shields.io/badge/{name}-full-red",
    "closed": "https://img.shields.io/badge/{name}-closed-yellow",
    "open": "https://img.shields.io/badge/{name}-open-green",
}
STATUS_TEXT_RE = re.compile(
    r"(<!-- testflight-status -->).+(<!-- /testflight-status -->)", re.MULTILINE
)


def main():
    with open("README.md", newline="\n") as f:
        readme = f.read()

    statuses = {}
    groups_text = []

    for name, link in ASTRODX_TESTFLIGHTS.items():
        resp = requests.get(link, headers={"Accept-Language": "en-us"})

        if not resp.ok:
            statuses[name] = "unknown"
            continue

        page = resp.text

        soup = bs4.BeautifulSoup(page, "html.parser")
        status_text = soup.select(".beta-status span")[0].get_text()

        if "This beta is full." in status_text:
            status = "full"
        elif "This beta isn't accepting" in status_text:
            status = "closed"
        else:
            status = "open"

        statuses[name] = status

        status_url = STATUS_URLS[status].format(name=quote(name))

        groups_text.append(
            f"[![AstroDX {name} TestFlight status]({status_url})]({link})"
        )

    with open("README.md", "w", newline="\n") as f:
        f.write(
            STATUS_TEXT_RE.sub(
                lambda m: f"{m.group(1)} {' '.join(groups_text)} {m.group(2)}", readme
            )
        )

    str_status = ", ".join([f"{name}: {value}" for name, value in statuses.items()])
    print(f"status={str_status}")


if __name__ == "__main__":
    main()
