"""Generate fully synthetic Contoso Support demo data (deterministic).

Usage:  python generate_data.py
Writes accounts.csv, contacts.csv, cases.csv next to this script.
All names are invented; emails use the reserved example.com domain;
phone numbers use the fictional 555-01xx range.
"""
import csv
import random
from datetime import date, timedelta
from pathlib import Path

SEED = 42
OUT = Path(__file__).parent
rnd = random.Random(SEED)

TIERS = ["Standard", "Premium", "Partner"]
FIRST = ["Alex", "Maria", "Jon", "Priya", "Lena", "Omar", "Sofia", "Ken", "Ana", "Tomas"]
LAST = ["Reed", "Novak", "Hale", "Patel", "Brandt", "Idris", "Moreau", "Sato", "Silva", "Kovac"]
ACCOUNT_NAMES = [
    "Northwind Homes", "Fabrikam Installers", "Adventure Lofts", "Tailspin Solar",
    "Lucerne Estates", "Woodgrove Retrofit", "Litware Properties", "Proseware Energy",
    "Alpine Ski House", "Coho Apartments", "Wingtip Builders", "Fourth Coffee Chain",
    "Graphic Design Studio", "Blue Yonder Flats", "VanArsdel Towers",
]
SUBJECTS = [
    ("Thermostat will not connect to Wi-Fi", "Standard"),
    ("Inverter shows error code E-21", "Partner"),
    ("Warranty replacement request", "Premium"),
    ("Complaint about installation", "Partner"),
    ("App cannot pair with device", "Standard"),
    ("Firmware update stuck at 80%", "Premium"),
]
ORIGINS = ["Email", "Web", "Phone"]
PRIORITIES = ["Low", "Normal", "High"]


def write(name, header, rows):
    with open(OUT / name, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


accounts = []
for i, n in enumerate(ACCOUNT_NAMES, 1):
    accounts.append([f"ACC{i:03d}", n, TIERS[i % 3], rnd.choice(["Consumer group", "Installer", "Enterprise"])])
write("accounts.csv", ["accountnumber", "name", "service_tier", "segment"], accounts)

contacts = []
cid = 1
for acc in accounts:
    for _ in range(rnd.randint(2, 4)):
        fn, ln = rnd.choice(FIRST), rnd.choice(LAST)
        contacts.append([
            f"CON{cid:03d}", acc[0], fn, ln,
            f"{fn.lower()}.{ln.lower()}{cid}@example.com", f"555-01{rnd.randint(0, 99):02d}",
        ])
        cid += 1
write("contacts.csv", ["contactnumber", "accountnumber", "firstname", "lastname", "email", "phone"], contacts)

cases = []
start = date(2026, 9, 1)
for k in range(1, 61):
    subj, _ = rnd.choice(SUBJECTS)
    con = rnd.choice(contacts)
    cases.append([
        f"CAS-{k:04d}", subj, con[1], con[0], rnd.choice(ORIGINS), rnd.choice(PRIORITIES),
        (start + timedelta(days=rnd.randint(0, 60))).isoformat(),
    ])
write("cases.csv", ["ticketnumber", "title", "accountnumber", "contactnumber", "origin", "priority", "created"], cases)

print(f"accounts={len(accounts)} contacts={len(contacts)} cases={len(cases)}")
