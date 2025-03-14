# задача про участок (выбрать максимальный квадрат)
def f(x, y):
    if max(x, y) % min(x, y) == 0:
        return min(x, y)
    return f(max(x, y) % min(x, y), min(x, y))


def max(lst, num=0):
    if len(lst) == 0:
        return num
    if lst[0] > num:
        return max(lst[1:], lst[0])
    return max(lst[1:], num)


print(max([1, 2, 9, 4, 5, 6]))

def quick_sort(lst):
    if len(lst) < 2:
        return lst
    op = lst[0]
    left = [x for x in lst[1:] if x <= op]
    right = [x for x in lst[1:] if x > op]
    return quick_sort(left) + [op] + quick_sort[right]


print(quick_sort([4, 2, 1, 6, 67, 8, 5, 4]))


