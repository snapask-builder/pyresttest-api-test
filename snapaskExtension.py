def decrease(compare_num, target_num):
    return target_num == (compare_num - 1)
    
def increase(compare_num, target_num):
    return target_num == (compare_num + 1)
 
COMPARATORS = {'dec': decrease}
COMPARATORS = {'inc': increase}
