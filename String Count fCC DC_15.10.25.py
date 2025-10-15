def count(text, parameter):
    contains = 0
    lp = len(parameter)
    for i in range(len(text)):   
        txtsplt = text[0+i:lp+i]
        if txtsplt == parameter:
            contains += 1


    return contains

print(count("aaaa","aa"))