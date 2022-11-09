from math import sqrt


def max_length(length, heigths):
    if 1 < length < 100 and len(heigths) < 50:
        if len(heigths) == 1:
            return 0 
        first_number = heigths[0]
        heigths.pop(0)
        return sqrt(((first_number - heigths[0]) * (-1)) * ((first_number - heigths[0]) * (-1)) + length ** 2) + max_length(length, heigths)


print("{:.2f}".format(max_length(2, [3, 1 , 3])))