import folium
import pandas
map = folium.Map(location = [27.652146, 85.327157], zoom_start = 6, tiles = 'Mapbox Bright')+

data = pandas.read_csv('volcano.txt')
lat = data['LAT']
lon = data['LON']
for lt, ln in zip(lat, lon):
    map.add_child(folium.Marker(location = [lt,ln], popup = 'Volcano area', icon = folium.Icon(color = 'blue')))
map.save('maps.html')
