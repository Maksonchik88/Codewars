def positive_sum(arr):
    return sum(num for num in arr if num > 0)


print(positive_sum(input().split()))
