#!/usr/bin/env python3

import requests
import sys
import urllib3
import time

urllib3.disable_warnings()

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <domain>")
    sys.exit(1)

domain = sys.argv[1]
all_subs = set()


def query_crt(exclude_expired=False):
    if exclude_expired:
        print(f"[+] Querying crt.sh (excluding expired certificates)...")
        url = f"https://crt.sh/?q={domain}&exclude=expired&output=json"
    else:
        print(f"[+] Querying crt.sh (all certificates)...")
        url = f"https://crt.sh/?q={domain}&output=json"

    while True:
        try:
            r = requests.get(
                url,
                verify=False,
                timeout=30,
                headers={"User-Agent": "Mozilla/5.0"},
            )

            if r.status_code != 200:
                print("[!] crt.sh returned non-200, retrying in 15 seconds...")
                time.sleep(15)
                continue

            data = r.json()

            for entry in data:
                names = entry.get("name_value", "").split("\n")

                for name in names:
                    name = name.replace("*.", "").strip()

                    if name.endswith(domain):
                        all_subs.add(name)

            break

        except Exception as e:
            print(f"[!] Error: {e}")
            print("[!] Retrying in 15 seconds...")
            time.sleep(15)


query_crt(exclude_expired=True)
query_crt(exclude_expired=False)

outfile = f"subs-{domain}.txt"

with open(outfile, "w") as f:
    for sub in sorted(all_subs):
        f.write(sub + "\n")

print(f"\n[+] Found {len(all_subs)} unique subdomains.")
print(f"[+] Output written to {outfile}")
