import phonenumbers
from phonenumbers import geocoder
phone_number = phonenumbers.parse(//enter phone number with country code in double codes)
print("\nphone number location is\n")
print(geocoder.description_for_number(phone_number, "en"))
