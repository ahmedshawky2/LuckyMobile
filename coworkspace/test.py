from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="specify_your_app_name_here")
location = geolocator.reverse("29.9889823,31.1337527")
print(location.raw['place_id'])