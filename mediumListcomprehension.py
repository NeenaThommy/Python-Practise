#MEDIUM (11–20)

#Convert all strings in a list to uppercase using list comprehension.
#Example: ["apple", "banana"] → ["APPLE", "BANANA"]

fruits = ["apple", "banana","baa"]
fruits_upper = [w.upper() for w in fruits]
print(fruits_upper)


#Create a list of tuples (x, x²) for x in range 1–5:
#Output: [(1,1), (2,4), …]

tuples = [(x,x*x) for x in range(1,5)]
print(tuples)

#Filter out strings whose length is greater than 3 using list comprehension.

filter_out = [x for x in fruits if len(x)<=3]
print(filter_out)

#Replace all negative numbers in a list with 0 using list comprehension.
#Example: [3, -2, 5, -7] → [3, 0, 5, 0]
numbers = [3, -2, 5, -7]
result = [0 if x<0 else x for x in numbers]
print(result)

#Flatten this nested list:
#[[1, 2], [3, 4], [5, 6]] → [1, 2, 3, 4, 5, 6]

nested = [[1, 2], [3, 4], [5, 6]]
flat = [num for sublist in nested for num in sublist]
print(flat)

#From a list of numbers, create two separate lists:

#One for even numbers

#One for odd numbers

filter_even = [x for x in range(1,10)if x%2==0]
filter_odd = [x for x in range(1,10)if x%2 != 0]
print(filter_even)
print(filter_odd)

#Extract all numbers divisible by both 3 and 5 using list comprehension.

numbers = [10, 15, 30, 22, 45, 60, 7, 90]
result = [n for n in numbers if n % 3 == 0 and n % 5 == 0]
print(result)

#Slice the last 5 elements from a tuple.


tuple_num = (1,2,3,4,5,6,7,8,9,10)
slice_last = tuple_num[5:]
print(slice_last)

#Given a list, replace all odd numbers with "ODD" using list comprehension.

replace_odd = ["odd" if x%2 !=0 else x for x in range(1,10)]
print(replace_odd)

#Create a list of (number, "even"/"odd") for numbers 1–10.
#Example: [(1, "odd"), (2, "even")]


oddoreven = [(x,"even")if x%2==0  else (x,"odd") for x in range(1,10)]
print(oddoreven)

