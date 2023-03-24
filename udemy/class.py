# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

x = year / 4 
#y = year / 100
z = year / 400


if x % 1 == 0:
    if z % 1 == 0 or float:
      print("Leap year.")
    else:
      print("Not leap year.")
else:
  print("Not leap year.")

