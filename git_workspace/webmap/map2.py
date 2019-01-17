import folium

map = folium.Map(location = [27.652146, 85.327157], zoom_start = 6, tiles = 'Mapbox Bright')

for coordinates in [[27.4, 85.2], [29.5, 83.3]]:
    map.add_child(folium.Marker(location = coordinates, popup = 'Hey, I am a marker', icon = folium.Icon(color = 'blue')))

map.save('map3.html')
