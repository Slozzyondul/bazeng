import phonenumbers 
import opencage
from numbertracker1 import number

from phonenumbers import gecoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")

print(location) 

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))


from opencage.geocoder import OpenCageGeocode




