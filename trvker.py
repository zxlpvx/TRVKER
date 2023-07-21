import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileNo = input("ENTER MOBILE NUMBER WITH COUNTRY CODE: ")
mobileNo = phonenumbers.parse(mobileNo)

print(timezone.time_zones_for_number(mobileNo))

print(carrier.name_for_number(mobileNo, "en"))

print(geocoder.description_for_number(mobileNo, "en"))

print("VALID MOBILE NUMBER: ", phonenumbers.is_valid_number(mobileNo))

print("Checking possibility of number{}...",
      phonenumbers.is_possible_number(mobileNo))
print(" TRVKER created by sloppy")
print("https://wanted.lol/z")
