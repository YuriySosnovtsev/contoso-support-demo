# Contoso Energy Home: knowledge articles (fictional)

All articles are invented for the demo. Paste Title, Keywords and Content into a new knowledge article (see [README](README.md)). Titles start with the words the case titles use (Wi-Fi, warranty, installation), so the `Search knowledge` macro, which searches by case title, finds them.

---

## 1. Thermostat will not connect to Wi-Fi
**Keywords:** wi-fi, thermostat, connect, router, pairing, 2.4 GHz

**Content:**
Applies to: Contoso Home Thermostat T2.

Symptoms: the thermostat shows "Wi-Fi not connected" or keeps looping on the pairing screen.

Steps:
1. Check that the router uses the 2.4 GHz band. The thermostat does not support 5 GHz.
2. Move the thermostat within 10 meters of the router for the first pairing.
3. Check the Wi-Fi network key. Special characters such as `&` or `"` can fail on older firmware; try a temporary simple key.
4. Hold the center button for 10 seconds to reset the network settings, then pair again from the Contoso Home app.
5. If it still fails, note the error code on the screen (see article 2) and open a case.

---

## 2. Inverter shows an error code
**Keywords:** inverter, error code, E01, E14, E27, fault

**Content:**
Applies to: Contoso SunBridge inverter.

| Code | Meaning | What the customer can do |
|---|---|---|
| E01 | Grid voltage out of range | Wait 5 minutes; the inverter restarts by itself. If it repeats, contact the installer. |
| E14 | Communication lost with the meter | Check the meter cable and the plug at the inverter; restart the inverter. |
| E27 | Insulation fault | Switch the inverter off and open a priority case. Do not touch the panels. |

Safety: never open the inverter housing. Codes E27 and above are treated as high priority.

---

## 3. Warranty replacement: what is covered
**Keywords:** warranty, replacement, coverage, invoice, purchase date

**Content:**
- Thermostat: 2 years from the purchase date.
- Inverter: 10 years from the installation date.
- Covered: manufacturing faults. Not covered: damage from water, moving or repair by a third party, wrong installation.

Needed from the customer: purchase invoice (or installation report), serial number, description of the fault and a photo.

Agent steps: confirm the dates, compare with the warranty period, approve or explain the options, create the follow-up task for the replacement shipment.

---

## 4. Installation complaint: how to handle it
**Keywords:** installation, complaint, installer, partner, escalation

**Content:**
1. Listen without interrupting, apologise, confirm the contact details.
2. Collect the facts: installer, date, site, what was done wrongly.
3. Ask for photos or the installation report and attach them to the case.
4. If the device is unsafe or not working, set the case priority to High.
5. Route the case to the Partner Desk queue and tell the customer the response time of their service tier.

---

## 5. Reset the thermostat to factory settings
**Keywords:** reset, factory, thermostat, button, restore

**Content:**
1. Open the Contoso Home app and remove the device from the account (optional but recommended).
2. Hold the center button for 15 seconds until the display shows "Reset".
3. Release the button and wait for the restart (about one minute).
4. Pair the thermostat again (article 1).

A factory reset deletes schedules and network settings; it does not change the warranty.
