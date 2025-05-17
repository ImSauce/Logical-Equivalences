#logical Equivalence
#Associative laws
#TODO--------------- [ VARIABLES ] --------------------#
p = False
q = True
r = True
#!------------------- [ METHODS ] ---------------------#
def Associative_or(p, q,r):
    return p or q, q or r

def Associative_and(p, q,r):
    return p and q, q and r


def ass_or(p, q, r):
    return (p or q) or r, p or (q or r)

def ass_and(p, q, r):
    return (p and q) and r, p and (q and r)

 
#?--------------------- [ MAIN ] ----------------------#

or1, or2 = Associative_or(p, q,r)
and1, and2 = Associative_and(p, q,r)

_or1, _or2 = ass_or(p, q, r)
_and1, _and2 = ass_and(p, q, r)

result1 = _or1 == _or2
result2 = _and1 == _and2


print(" ")
print(f"(p OR q [{or1}]) OR r [{r}] <{_or1}>= p [{p}] OR (q OR r [{or2}]) <{_or2}>               result= {result1}")
print(f"(p AND q [{and1}]) AND r [{r}] <{_and1}>= p [{p}] AND (q AND r [{and2}]) <{_and2}>        result= {result2}")