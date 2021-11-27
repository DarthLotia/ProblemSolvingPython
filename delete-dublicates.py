# input (1,2,1,4,5,6,6) ---- output([1, 2, 4, 5, 6])

def remove_dublicates(l):
    result = []
    for val in l:
        if not val in result:
            result.append(val)

    return result

print(remove_dublicates([1, 2, 1, 4, 5, 6, 6]))