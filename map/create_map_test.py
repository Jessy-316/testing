import folium
import webbrowser
import os

# Prompt the user to enter latitude and longitude
location_input = input("Enter your location's latitude and longitude (e.g., 35.6762, 139.6503): ")

try:
    # Split the input string into latitude and longitude
    latitude_str, longitude_str = location_input.split(',')
    latitude = float(latitude_str.strip())
    longitude = float(longitude_str.strip())
except ValueError:
    print("Invalid input. Please enter valid numerical values in the format 'latitude, longitude'.")
    exit()

# Create a map centered around the user's location
map_center = [latitude, longitude]
mymap = folium.Map(location=map_center, zoom_start=16)

# Add a marker at the user's location
folium.Marker(
    [latitude, longitude],
    popup="Your Location",
    icon=folium.Icon(color="blue", icon="info-sign")
).add_to(mymap)

# Save the map as an HTML file
mymap.save("user_location_map.html")

print("Map has been created and saved as 'user_location_map.html'.")

# Open the saved HTML file in the default web browser
file_path = os.path.abspath("user_location_map.html")
webbrowser.open(f"file://{file_path}")
