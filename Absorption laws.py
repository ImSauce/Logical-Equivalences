#logical Equivalence
#Absorption laws
#TODO--------------- [ VARIABLES ] --------------------#
p = True
q = False
#!------------------- [ METHODS ] ---------------------#


def absorption(p, q):
    return p or (p and q), p and (p or q)


#?--------------------- [ MAIN ] ----------------------#
absorb1, absorb2 = absorption(p, q)



result1 = absorb1 == p
result2 = absorb2 == p


print(" ")
print("------------OUTPUT------------")
print(f"p OR (p AND q) [{absorb1}]  == p [{p}]      >{result1}")
print(f"p AND (p OR q) [{absorb2}]  == p [{p}]      >{result2}")












