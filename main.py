print("Tool for calculating decent\n")
print("      __|__")
print("*---o--(_)--o---*\n")

## Variables
current_Altitude = "NAN"
airport_Altitude = "NAN"
target_Altitude = "NAN"
current_Speed = "NAN"
quit_Program = "NO"
descent_Rate = 0.03 #default 3% decent rate

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
      current_Speed = int(input("Current speed: knots \n"))
    except ValueError as ve:
      print("please type a number")

  ## calculate Altitude_difference 
  altitude_Difference = current_Altitude - airport_Altitude
  ## calculate descent distance in feet (altitude_Difference / descent_Rate) (default 3%)
  descent_Distance_FT = float(altitude_Difference / descent_Rate)
  ## convert descent_Distance_FT to nm (miles,  there are 5280 ft in a mile)
  descent_Distance_NM = float(descent_Distance_FT / 5280)

  ## printing result and using "{:.2f}".format(x, 2) to round down to 2 numbers behind the comma
  print("\nStart descent at: " + str("{:.2f}".format(descent_Distance_NM, 2)) + " miles from destination")
  

  
  if current_Altitude != "NAN" and airport_Altitude != "NAN" and current_Speed != "NAN":
    quit_Program = "YES"


