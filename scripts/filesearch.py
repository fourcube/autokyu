#!/usr/bin/env python3

import subprocess
import argparse
from urllib.parse import urlparse
from time import time

timestamp = int(time())
wordlists = [
    ("txt", "/opt/wordlists/data/automated/httparchive_txt_2023_08_28.txt"),
    ("xml", "/opt/wordlists/data/automated/httparchive_xml_2023_08_28.txt"),
    ("html", "/opt/wordlists/data/automated/httparchive_html_htm_2023_08_28.txt"),
    ("php", "/opt/wordlists/data/automated/httparchive_php_2023_08_28.txt"),
]

parser = argparse.ArgumentParser(description="scans for directories on a host")
parser.add_argument(
    "-f", "--format", default="html", choices=["html", "json", "md", "csv"]
)

parser.add_argument("url")
args = parser.parse_args()
url = urlparse(args.url)

for wordlist_key, wordlist in wordlists:
    print(wordlist_key, wordlist)
    filesearch_args = [
        "ffuf",
        # wordlist
        "-w",
        wordlist,
        # target url
        "-u",
        f"{args.url}/FUZZ",
        # output
        "-o",
        f"files_{timestamp}_{url.netloc}_{wordlist_key}.{args.format}",
        "-of",
        args.format,
    ]

    subprocess.run(filesearch_args)
