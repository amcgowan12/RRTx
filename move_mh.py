#!/usr/bin/env python3
"""Move Malignant Hyperthermia from Endocrine/Metabolic to Toxicology."""

import json, sys

PATH = "/Users/andrewmcgowan/Desktop/Residency/Rapid response -planning/Rapid response -planning/Rapid response 2026/Rapid Response/Data/content.json"

with open(PATH, "r") as f:
    data = json.load(f)

# Find and remove MH from its current system
mh_topic = None
for system in data:
    for i, topic in enumerate(system["topics"]):
        if topic["title"] == "Malignant Hyperthermia":
            mh_topic = system["topics"].pop(i)
            print(f"✅ Removed '{mh_topic['title']}' from '{system['name']}' ({len(system['topics'])} topics remaining)")
            break
    if mh_topic:
        break

if not mh_topic:
    print("❌ Malignant Hyperthermia topic not found!")
    sys.exit(1)

# Add to Toxicology
for system in data:
    if system["name"] == "Toxicology":
        system["topics"].insert(1, mh_topic)  # After Baclofen, before toxidromes
        print(f"✅ Added '{mh_topic['title']}' to Toxicology ({len(system['topics'])} topics now)")
        for t in system["topics"]:
            print(f"   - {t['title']}")
        break

with open(PATH, "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ content.json written successfully")

with open(PATH, "r") as f:
    json.load(f)
print("✅ JSON validation passed")
