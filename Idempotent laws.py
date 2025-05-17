#logical Equivalence
#Idempotent laws
#TODO--------------- [ VARIABLES ] --------------------#
p = True

#!------------------- [ METHODS ] ---------------------#
def Idempotent_law1(p):
    return p or p

def Idempotent_law2(p):
    return p and p

#?--------------------- [ MAIN ] ----------------------#

Idempotent_1 = Idempotent_law1(p)
Idempotent_2 = Idempotent_law2(p)

print(" ")
print(f"p OR p [{Idempotent_1}] = p [{p}]")
print(f"p AND p [{Idempotent_2}] = p [{p}]")