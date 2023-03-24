programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
    }
    

#retriving item from dictionary
print(programming_dictionary["Bug"])

#adding new item for dictionary 
programming_dictionary["Loop"] = "lol, new item" 
print(programming_dictionary)

#creating empty dictionary
programming_dictionary = {}
print(programming_dictionary)


#edit item in a dictionary
programming_dictionary["Bug"] = "editing bug item"
print(programming_dictionary)


#loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

