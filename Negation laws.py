#logical Equivalence
#Negation laws
#TODO--------------- [ VARIABLES ] --------------------#
p = True
#!------------------- [ METHODS ] ---------------------#


def Negation(p):
    return p or not p, p and not p


#?--------------------- [ MAIN ] ----------------------#
Nega1, Nega2 = Negation(p)

print(" ")
print("------------OUTPUT------------")
print(f"p [{p}] OR -p [{not p}] [{Nega1}] == True")
print(f"p [{p}] AND -p [{not p}] [{Nega2}] == False")
