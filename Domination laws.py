#logical Equivalence
#domination laws
#TODO--------------- [ VARIABLES ] --------------------#
p = True

#!------------------- [ METHODS ] ---------------------#
def domination_law1(p):
    return p or True

def domination_law2(p):
    return p and False

#?--------------------- [ MAIN ] ----------------------#

domination_1 = domination_law1(p)
domination_2 = domination_law2(p)

print(" ")
print(f"P OR True [{domination_1}] = True")
print(f"P AND False [{domination_2}] = False")