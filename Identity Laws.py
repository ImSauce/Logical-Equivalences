#logical Equivalence
#identity laws
#TODO--------------- [ VARIABLES ] --------------------#
p = True

#!------------------- [ METHODS ] ---------------------#
def identity_law1(p):
    return p and True

def identity_law2(p):
    return p or False

#?--------------------- [ MAIN ] ----------------------#

Identity_1 = identity_law1(p)
Identity_2 = identity_law2(p)

print(" ")
print(f"P and True [{Identity_1}] = p [{p}]")
print(f"P OR False [{Identity_2}] = p [{p}]")