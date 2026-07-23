# day08/main.py


import random



# 1. Recursive Sum and Count Down


def total(nums):

    if len(nums) == 0:
        return 0

    return nums[0] + total(nums[1:])



def count_down(n):

    if n == 0:
        return

    print(n)

    count_down(n - 1)



print("\n1. Recursive Examples")


numbers = [10, 20, 30, 40]

print(
    "Total:",
    total(numbers)
)


count_down(5)




# 2. Binary Search


def binary_search(items, target):

    left = 0
    right = len(items) - 1


    while left <= right:

        middle = (left + right) // 2


        if items[middle] == target:

            return middle


        elif items[middle] < target:

            left = middle + 1


        else:

            right = middle - 1


    return -1



print("\n2. Binary Search")


balances = [
    500,
    1000,
    2500,
    5000,
    8000,
    12000
]


print(
    binary_search(balances, 5000)
)


print(
    binary_search(balances, 9000)
)




# 3. Merge Sort


def merge(left, right):

    result = []

    i = 0
    j = 0


    while i < len(left) and j < len(right):

        if left[i] <= right[j]:

            result.append(left[i])

            i += 1


        else:

            result.append(right[j])

            j += 1



    result.extend(left[i:])

    result.extend(right[j:])


    return result



def merge_sort(items):

    if len(items) <= 1:

        return items


    middle = len(items) // 2


    left = merge_sort(
        items[:middle]
    )


    right = merge_sort(
        items[middle:]
    )


    return merge(left, right)



print("\n3. Merge Sort")


random_numbers = [
    random.randint(1, 100)
    for _ in range(10)
]


print(
    "Original:",
    random_numbers
)


print(
    "Merge sort:",
    merge_sort(random_numbers)
)


print(
    "sorted():",
    sorted(random_numbers)
)




# 4. Sort With Key


print("\n4. Sort By Balance")


accounts = [
    ("Eyasu", 5000),
    ("Almaz", 8000),
    ("Dawit", 3000),
    ("Sara", 12000)
]


sorted_accounts = sorted(
    accounts,
    key=lambda account: account[1],
    reverse=True
)


print(sorted_accounts)




# 5. Two Pointer Algorithm


def has_pair(nums, target):

    left = 0

    right = len(nums) - 1


    while left < right:


        total = nums[left] + nums[right]


        if total == target:

            return True


        elif total < target:

            left += 1


        else:

            right -= 1


    return False



print("\n5. Two Pointer")


values = [
    1,
    3,
    5,
    7,
    9,
    12
]


print(
    has_pair(values, 16)
)


print(
    has_pair(values, 20)
)