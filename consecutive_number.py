# Your task is to find the first element of an array that is not consecutive.
# By not consecutive we mean not exactly 1 larger than the previous element of the array.
# E.g. If we have an array [1,2,3,4,6,7,8] then 1 then 2 then 3 then 4 are all consecutive but 6 is not,
# so that's the first non-consecutive number.


def first_non_consecutive(arr):
    x = 0
    for num in arr:
        if arr[x] + 1 == arr[x + 1]:
            x += 1
            if x == (len(arr) - 1):
                return None
        else:
            return arr[x + 1]


print(first_non_consecutive([1, 2, 3, 4, 6, 7, 8]))
print(first_non_consecutive([-3, -2, 0, 1]))
print(first_non_consecutive([1, 2, 3, 4, 5, 6, 7, 8]))
print(first_non_consecutive([31, 32]))
print(first_non_consecutive([4, 6, 7, 8, 9, 11]))
