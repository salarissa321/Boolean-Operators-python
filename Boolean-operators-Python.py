



#----------------------------
#----Boolean Operators-----
#----------------------------
# and
# or
#-----------------------------

# and

age = 27
country = "Deutschalnd"
rank = 10

print(age > 20) # True
print(country == "Deutschland") # True

print(age > 20 and country == "Deutschland" and rank > 10) # True
print(age > 20 and country == "Polen" and rank > 10) # False


print("-" * 50) # --------------------------------------------------

# or

print(age > 20 or country == "Deutschland") # True
print(age > 40 or country == "USA" or rank > 20) # False
print(age > 40 or country == "Deutschland" or rank > 20) # True

print("-" * 50) # --------------------------------------------------

# not

print(age > 16) # True  
print( not age > 16) # Not True = False