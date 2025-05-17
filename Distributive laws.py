#logical Equivalence
#Distributive laws
#TODO--------------- [ VARIABLES ] --------------------#
p = False
q = False
r = False
#!------------------- [ METHODS ] ---------------------#

def Distributive_or(p, q, r):
    return  p or (q and r),  (p or q) and (p or r)

def Distributive_and(p, q, r):
    return p and (q or r) ,  (p and q) or (p and r)

 
#?--------------------- [ MAIN ] ----------------------#
_or1, _or2 = Distributive_or(p, q, r)
_and1, _and2 = Distributive_and(p, q, r)

result1 = _or1 == _or2
result2 = _and1 == _and2


print(" ")
print(" ")
print("Distributive Law of OR:")
print(f"p OR (q AND r) <{_or1}> == (p OR q) AND (p OR r) <{_or2}>     result = {result1}")

print("\nDistributive Law of AND:")
print(f"p AND (q OR r) <{_and1}> == (p AND q) OR (p AND r) <{_and2}>  result = {result2}")