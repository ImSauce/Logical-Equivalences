#logical Equivalence
#Commutative laws
#TODO--------------- [ VARIABLES ] --------------------#
p = False
q = False
#!------------------- [ METHODS ] ---------------------#
def commutative_or(p, q):
    return p or q, q or p

def commutative_and(p, q):
    return p and q, q and p

#?--------------------- [ MAIN ] ----------------------#

or1, or2 = commutative_or(p, q)
and1, and2 = commutative_and(p, q)

print(" ")
print(f"p OR q [{or1}] = q OR p [{or2}]       > {or1 == or2}")
print(f"p AND q [{and1}] = q AND p [{and2}]   > {and1 == and2}")