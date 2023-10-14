#!/usr/bin/env python3

import subprocess
import argparse
from time import time
from urllib.parse import urlparse

timestamp = int(time())
parser = argparse.ArgumentParser(description="scans for directories on a host")
parser.add_argument(
    "-w",
    "--wordlist",
    default="/opt/wordlists/data/automated/httparchive_directories_1m_2023_08_28.txt",
)
parser.add_argument(
    "-f", "--format", default="html", choices=["html", "json", "md", "csv"]
)
parser.add_argument("url")
args = parser.parse_args()
url = urlparse(args.url)

dirsearch_args = [
    "ffuf",
    "-recursion",
    # wordlist
    "-w",
    args.wordlist,
    # target url
    "-u",
    f"{args.url}/FUZZ",
    # output
    "-o",
    f"dirs_{timestamp}_{url.netloc}.{args.format}",
    "-of",
    args.format,
]

subprocess.run(dirsearch_args)
