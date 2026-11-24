import json
import sys


FILENAME = 'YourSaveHere.save' 

def remove_collar(obj):
if isinstance(obj, dict):
if "neck" in obj and isinstance(obj["neck"], dict) and obj["neck"].get("id") == "inmatecollar":
obj["neck"] = None
for k, v in obj.items():
remove_collar(v)
elif isinstance(obj, list):
for item in obj:
remove_collar(item)

try:
with open(FILENAME, 'r', encoding='utf-8') as f:
data = json.load(f)
except Exception as e:
print(f"error: {e}")
sys.exit(1)

remove_collar(data)

with open(FILENAME, 'w', encoding='utf-8') as f:
json.dump(data, f, ensure_ascii=False)

print("all collars removed.")
