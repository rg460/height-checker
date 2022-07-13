print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age?"))
if height >= 120:
  print("You can ride the rollercoaster")
  if age >= 18:
        print("The price of the rollercoaster will be £12")
  else:
        print("The price of the rollercoaster will be £7")
else:
  print("You are too short , you  cannot ride the rollercoster")
  