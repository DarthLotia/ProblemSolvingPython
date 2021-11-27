# [1, 2, 4, 7, "a"], ["a", "b", 1, 3, 2, 7, 4] = true

def is_subset(L1, L2): 
    for e in L1: 
        if not e in L2:
            return False
    return True

print(is_subset([1, 2, 4, 7, "a"], ["a", "b", 1, 3, 2, 7, 4]))            

