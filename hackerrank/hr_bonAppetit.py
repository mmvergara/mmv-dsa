import math

def bonAppetit(bill, k, b):
    totalBill = sum(bill)
    ab = math.trunc((totalBill-bill[k])/2)
    if ab == b:
        print("Bon Appetit")
    else:
        print(b - ab)






bonAppetit([3,10,2,9],1,7)
