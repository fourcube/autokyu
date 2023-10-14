#!/usr/bin/env python3

import subprocess
import argparse

parser = argparse.ArgumentParser(description="scans for directories on a host")
parser.add_argument(
    "-w",
    "--wordlist",
    default="/opt/wordlists/data/automated/httparchive_directories_1m_2023_08_28.txt",
)
parser.add_argument("domain")
args = parser.parse_args()

subprocess.run(
    [
        "ffuf",
        "-recursion",
        # wordlist
        "-w",
        args.wordlist,
        # target url
        "-u",
        f"{args.domain}/FUZZ",
        # output
        "-o",
        "html",
    ]
)
