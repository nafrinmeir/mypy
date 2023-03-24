# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

place = int(position)

#print(place)

if place == 11:
    row1 = ["❌","️⬜️","️⬜️"]
    row2 = ["⬜️","⬜️","️⬜️"]
    row3 = ["⬜️️","⬜️️","⬜️️"]
elif place == 21:
    row1 = ["⬜️","️❌","️⬜️"]
    row2 = ["⬜️","⬜️","️⬜️"]
    row3 = ["⬜️️","⬜️️","⬜️️"]
elif place == 31:
    row1 = ["⬜️","️⬜️","️❌"]
    row2 = ["⬜️","⬜️","️⬜️"]
    row3 = ["⬜️️","⬜️️","⬜️️"]
#else:
#    print("error")

if place == 12:
    row1 = ["⬜️","️⬜️","️⬜️"]
    row2 = ["❌","⬜️","️⬜️"]
    row3 = ["⬜️️","⬜️️","⬜️️"]
elif place == 22:
    row1 = ["⬜️","⬜️","️⬜️"]
    row2 = ["⬜️","❌","️⬜️"]
    row3 = ["⬜️️","⬜️️","⬜️️"]
elif place == 32:
    row1 = ["⬜️","️⬜️","⬜️"]
    row2 = ["⬜️","⬜️","️❌"]
    row3 = ["⬜️️","⬜️️","⬜️️"]
#else:
#    print("error")

if place == 13:
    row1 = ["⬜️","️⬜️","️⬜️"]
    row2 = ["⬜️","⬜️","️⬜️"]
    row3 = ["❌","⬜️️","⬜️️"]
elif place == 23:
    row1 = ["⬜️","⬜️","️⬜️"]
    row2 = ["⬜️","⬜️","️⬜️"]
    row3 = ["⬜️️","❌","⬜️️"]
elif place == 33:
    row1 = ["⬜️","️⬜️","⬜️"]
    row2 = ["⬜️","⬜️","⬜️"]
    row3 = ["⬜️️","⬜️️","❌"]
#else:
#    print("error")

map = [row1, row2, row3]
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

