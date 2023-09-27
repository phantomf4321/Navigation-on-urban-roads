import openrouteservice as ors
import folium
import operator
from functools import reduce

client = ors.Client(key='')

m = folium.Map(location=list(reversed([59.51120108401389, 36.31167174706367])), tiles="Cartodb dark_matter", zoom_start=13)
# white house to the pentagon
coords = [[59.51120108401389, 36.31167174706367], [59.61310468013571, 36.291125254657985]]

route = client.directions(coordinates=coords,
                          profile='foot-walking',
                          format='geojson')

waypoints = list(dict.fromkeys(reduce(operator.concat, list(map(lambda step: step['way_points'], route['features'][0]['properties']['segments'][0]['steps'])))))
folium.PolyLine(locations=[list(reversed(coord)) for coord in route['features'][0]['geometry']['coordinates']], color="blue").add_to(m)
folium.PolyLine(locations=[list(reversed(route['features'][0]['geometry']['coordinates'][index])) for index in waypoints], color="red").add_to(m)

m
