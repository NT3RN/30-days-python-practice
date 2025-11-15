numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
print([n for n in numbers if n < 0])

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
print([i for array in list_of_lists for j in array for i in j])

print([(n, 1, n, n*n, n*n*n, n*n*n*n) for n in range(0,11)])

def m(x1, y1, x2, y2): return (y2-y1)/(x2-x1)
print(m(2, 2, 4, 8))
