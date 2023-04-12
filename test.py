# Exercise #1:

# Given an array of positive integers nums, return a list of all of the negative integers.


nums1 = [1, 3, 5, 7, 8]
#Expected Output: [-1, -3, -5, -7, -8]
def integers(nums):
    output = []

    for num in nums:
        output.append(-num)
    return output

print(integers(nums1))




nums2 = [100, 534, 32, 15, 77, 222, 788, 345, 75645, 22]
#Expected Output: [-100, -534, -32, -15, -77, -222, -788, -345, -75645, -22]

def integers(nums2):
    output = []

    for num in nums2:
        output.append(-num)
    return output

print(integers(nums2))


# Exercise #2:

# Given a string, return a list of all of the digits in the string.

# address = "123 Real Street, Apt. 2, Springfield, OR 43498"
# Expected Output: ['1', '2', '3', '2', '4', '3', '4', '9', '8']


def output(string):

    digits = []
    address = "123 Real Street, Apt. 2, Springfield, OR 43498"

    for char in string:
        if char.isdigit():
            output.append(char)

    return digits

print(output(address))  


# sentence = "My phone number is (555) 555-4321"
# Expected Output: ['5', '5', '5', '5', '5', '5', '4', '3', '2', '1']

def output(string):
    digits = []
    sentence = "My phone number is (555) 555-4321"

    for char in string:
        if char.isdigit():
            output.append(char)

    return digits

print(output(sentence)) 



# Exercise #3:

# Given a string digits, return a string of the digits + 1

# Expected Output: '124'

def string(digits):
    digits = '123'
    num = int(digits) + 1

    return str(num)

print(string(digits))


# digits = '99'
# Expected Output: '100'

def string2(digits):
    digits = '99'
    num = int(digits) + 1

    return str(num)

print(string2(digits))