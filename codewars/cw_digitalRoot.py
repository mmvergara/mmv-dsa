# recursion approach
def digital_root(n):
    
    # if n len == 1 then we reach the root
    if len(str(n)) == 1:
        return n
    
    total = 0
    # add all of the numbers in the integer
    for i in list(str(n)):
        total+=int(i)

    return digital_root(total)

print(digital_root(132189))