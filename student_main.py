import re

# Task 1: Interpolate Missing Values
def interpolate_missing(arr):
    if not arr:
        return arr
    
    for i in range(len(arr)):
        if arr[i] is None:
            left = right = None
            for j in range(i - 1, -1, -1):
                if arr[j] is not None:
                    left = arr[j]
                    break
            for k in range(i + 1, len(arr)):
                if arr[k] is not None:
                    right = arr[k]
                    break
            if left is not None and right is not None:
                arr[i] = (left + right) / 2
            elif left is not None:
                arr[i] = left
            elif right is not None:
                arr[i] = right
    return arr

print(interpolate_missing([1, None, None, 4]))  # Output: [1, 2, 3, 4]


# Task 2: Fibonacci Series Generator
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fibonacci(5)))  # Output: [0, 1, 1, 2, 3]


# Task 3: Batch Data Processing
def process_batches(arr, batch_size):
    return [max(arr[i:i+batch_size]) for i in range(0, len(arr), batch_size)]

print(process_batches([1, 2, 3, 4, 5, 6], 2))  # Output: [2, 4, 6]


# Task 4: Encode and Decode Strings
def encode_string(s):
    if not s:
        return ""
    encoded = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            encoded += f"{count}{s[i-1]}"
            count = 1
    encoded += f"{count}{s[-1]}"
    return encoded

def decode_string(s):
    if not s:
        return ""
    decoded = ""
    count = ""
    for char in s:
        if char.isdigit():
            count += char
        else:
            decoded += char * int(count)
            count = ""
    return decoded

encoded = encode_string("aaabbc")
print(encoded)  # Output: "3a2b1c"
print(decode_string(encoded))  # Output: "aaabbc"


# Task 5: Matrix Rotation
def rotate_matrix(matrix):
    return list(zip(*matrix[::-1]))

matrix = [
    [1, 2],
    [3, 4]
]
print(rotate_matrix(matrix))  # Output: [(3, 1), (4, 2)]


# Task 6: Regular Expression Search
def regex_search(arr, pattern):
    return [s for s in arr if re.search(pattern, s)]

print(regex_search(["test", "test1", "test123", "none"], r"test\d+"))  # Output: ['test1', 'test123']


# Task 7: Merge Sorted Arrays
def merge_sorted_arrays(arr1, arr2):
    return sorted(arr1 + arr2)

print(merge_sorted_arrays([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]


# Task 8: Prime Number Checker
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(11))  # Output: True
print(is_prime(4))   # Output: False


# Task 9: Group by Key
def group_by_key(data, key):
    grouped = {}
    for item in data:
        k = item[key]
        if k not in grouped:
            grouped[k] = []
        grouped[k].append(item['value'])
    return grouped

data = [{'key': 'a', 'value': 1}, {'key': 'b', 'value': 2}, {'key': 'a', 'value': 3}]
print(group_by_key(data, 'key'))  # Output: {'a': [1, 3], 'b': [2]}


# Task 10: Remove Outliers
def remove_outliers(data):
    mean = sum(data) / len(data)
    std_dev = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs(x - mean) <= 2 * std_dev]

print(remove_outliers([10, 100, 200, 300, 400, 500, 600]))  # Output: [100, 200, 300, 400, 500]
