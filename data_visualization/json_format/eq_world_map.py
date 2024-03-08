import json
from pathlib import Path
import plotly.express as px

path = Path("eq_data/eq_data_30_day_m1.geojson")
contents = path.read_text()
all_eq_data = json.loads(contents)

# readable_contents = json.dumps(all_eq_data, indent=4)
# path = Path("eq_data/readable_eq_data.geojson")
# path.write_text(readable_contents)

# Extract magnitudes
all_eq_dicts = all_eq_data["features"]
mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    eq_title = eq_dict["properties"]["title"]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)

fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title="Global Earthquakes",
                     color=mags,  # Use the mags list to determine the color for each point
                     # Which color scale to use, Viridis is a color scale that ranges from dark blue to bright yellow
                     # available color scales: px.colors.named_colorscales()
                     color_continuous_scale="reds", #"viridis",
                     labels={"color":"Magnitude"},
                     projection="natural earth", # Rounds the ends of the map
                     hover_name=eq_titles,
                     )
fig.show()