def check_nums(t):
    nums = list(range(1, 10))
    try:
        for i in t:
            for j in i:
                nums.remove(j)
    except ValueError:
        return False

    if len(nums) == 0:
        return True
    else:
        return False

def check_row(t, num):
    for x in t:
        if x[0] + x[1] + x[2] != num:
            return False

    return True

def check_cols(t, num):
    for i in range(0,3):
        if t[i][0] + t[i][1] + t[i][2] != num:
            return False

    return True

def check_diags(t, num):
    d1 = t[0][0] + t[1][1] + t[2][2]
    d2 = t[0][2] + t[1][1] + t[2][0]

    if d1 == num and d2 == num:
        return True
    else:
        return False

def is_magic(t):
    num = 0
    for x in t[0]:
        num += x

    nums = check_nums(t)
    rows = check_row(t, num)
    cols = check_cols(t, num)
    diag = check_diags(t, num)
	
    if nums and diag and rows and cols:
        print('True')
    else:
        print('False')

t1 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
t2 = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
t3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
t4 = [[4, 9, 2], [3, 5, 5], [8, 1, 6]]

print(t1)
is_magic(t1)

print(t2)
is_magic(t2)

print(t3)
is_magic(t3)

print(t4)
is_magic(t4)
