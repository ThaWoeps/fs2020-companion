print("Tool for calculating decent in MN\n")
print("      __|__")
print("*---o--(_)--o---*\n")

## Variables
current_Altitude = "NAN"
airport_Altitude = "NAN"
target_Altitude = "NAN"
current_Speed = "NAN"
quit_Program = "NO"

## Ask current_Altitude
while quit_Program == "NO":
  while current_Altitude == "NAN":
    try:
      current_Altitude = int(input("Current altitude: ft "))
    except ValueError as ve:
      print("please type a number")
      
  while airport_Altitude == "NAN":
    try:
      airport_Altitude = int(input("Airport altitude: ft "))
    except ValueError as ve:
      print("please type a number")

  while current_Speed == "NAN":
    try:
      current_Speed = int(input("Current speed: "))
    except ValueError as ve:
      print("please type a number")

  
  if current_Altitude != "NAN" and airport_Altitude != "NAN" and current_Speed != "NAN":
    quit_Program = "YES"


