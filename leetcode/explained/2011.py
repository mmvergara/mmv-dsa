from randoms.dsa import *
def finalValueAfterOperations(self, operations: List[str]) -> int:

    val = 0

    for o in operations:
        if o[1] == "+":
            val+=1
        elif o[1] == "-":
            val-=1
    print(val)
    return val


