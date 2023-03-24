# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print("-----------------------------")
print(name1)
print(name2)
print("-----------------------------")

lower_case_name1 = name1.lower()
at = lower_case_name1.count("t")
#print(at)
al = lower_case_name1.count("l")
#print(al)
ar = lower_case_name1.count("r")
#print(ar)
ao = lower_case_name1.count("o")
#print(ao)
au = lower_case_name1.count("u")
#print(au)
av = lower_case_name1.count("v")
#print(av)
ae = lower_case_name1.count("e")
#print(ae)

#print("----------------------------")

lower_case_name2 = name2.lower()
bl = lower_case_name2.count("l")
#print(bl)
bt = lower_case_name2.count("t")
#print(bt)
bo = lower_case_name2.count("o")
#print(bo)
br = lower_case_name2.count("r")
#print(br)
bu = lower_case_name2.count("u")
#print(bu)
bv = lower_case_name2.count("v")
#print(bv)
be = lower_case_name2.count("e")
#print(be)

#print("----------------------------")

true = (at + ar + au + ae + bt + br + bu + be)
print(true)
love = al + ao + av + ae + bl + bo + bv + be
print(love)

score = int(str(true) + str(love))
print(score)

if score <10 or score >90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print (f"Your score is {score}, you are alright together.")
else:
    print (f"Your score is {score}.")

