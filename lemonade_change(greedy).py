# several customers in an array, every bottle of lemonade is $five, judge if it can be charged.
def lemonade_charge(arr):
    five = 0
    ten = 0
    for i in arr:
        if i == 5:
            five += 1
        elif i == 10:
            ten += 1
            if five > 0:
                five -= 1
            else:
                return False
        elif i == 20:
            if ten > 0 and five > 0:
                ten -= 1
                five -= 2
            else:
                return False
    return True



test = [5, 10, 10, 20]
print(lemonade_charge(test))

