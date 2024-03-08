import json
from pathlib import Path

path = Path("eq_data/eq_data_1_day_m1.geojson")
contents = path.read_text()
all_eq_data = json.loads(contents)

# readable_contents = json.dumps(all_eq_data, indent=4)
# path = Path("eq_data/readable_eq_data.geojson")
# path.write_text(readable_contents)

# Extract magnitudes
all_eq_dicts = all_eq_data["features"]
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
print(mags[:10])
print(lons[:10])
print(lats[:10])