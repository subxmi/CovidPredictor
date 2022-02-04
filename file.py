# This program is a simulation of the spread of Covid-19 in a country.
print("This Program is dedicated to a project i did back in 2020 for a Challenge called the 300 Innovation Challenge")
# Asking the user to input the number of people who have Covid in their country.
cases=int(input("How many people have Covid in your country"))
# Creating a list of the number of cases for each day.
future=[cases]
# This code is taking the number of cases on a given day and multiplying it by a factor of 2.5.
if cases<30000:
    for x in range(0,50):
        print("day",x,"cases",future[x])

# Creating a list of future values based on the previous value.
        future.append(future[x]*1.5)
elif cases > 29999 and cases:
    for x in range(0,100):
        print("day",x,"cases",future[x])
        future.append(future[x]*1.2)
print("This is How Many People will have Coronavirus if there is no Social Distancing Please stay safe!")
print("This is my Final Project for Codefest")                

# First Thing i did that made me love Ai And How machines can think for themselves