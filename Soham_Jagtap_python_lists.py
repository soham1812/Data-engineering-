"""
   Python Lists Assessment
   
   Name: Soham Jagtap G1 - DE  """

# PART A 

print("PART A")

# Task 1

print("\nTask 1")
cities = ["Bhopal", "Mumbai", "Pune", "Indore", "Delhi"]
print(cities)
print(type(cities))
print(len(cities))

# Task 2
print("\nTask 2")

"""
# Index starts from 0.
# So first city is 0, third city is 2 and -1 means last city."""

print(cities[0])
print(cities[-1])
print(cities[2])

# Task 3
print("\nTask 3")
numbers = [10, 20, 30, 40, 50]
print(numbers)

"""""

# My prediction:
# len(numbers) = 5
# numbers[0] = 10
# numbers[-1] = 50
# numbers[len(numbers) - 1] = 50  """
                               
print(len(numbers))
print(numbers[0])
print(numbers[-1])
print(numbers[len(numbers) - 1])

"""
# My prediction was correct for all four expressions.
# len(numbers) gives 5, numbers[0] gives the first number and
# numbers[-1] gives the last number. The last expression also gives 50
# because len(numbers) - 1 is 4. """

# Task 4
print("\nTask 4")
for city in cities:
    print(city)

for i in range(len(cities)):
    print(cities[i])

"""
# Both loops print every city one by one.
# The first loop directly gives the city name.
# The second loop gives the index first, then we use that index to get the city. """

# Task 5
print("\nTask 5")
for i, city in enumerate(cities, start=1):
    print(i, city)

# Task 6
print("\nTask 6")
cities.append("Jaipur")
print(cities)

cities[1] = "Chennai"
print(cities)

cities.remove("Indore")
print(cities)


# PART B

print("\nPART B")

# B2 - Student marks
print("\nB2")
marks = [78, 85, 69, 92, 74, 88]
print(marks)

for i in range(len(marks)):
    print("Student", i + 1, ":", marks[i])

average = sum(marks) / len(marks)
print("Average mark:", average)

# I5 - Duplicate registrations
print("\nI5")
names = ["Soham", "Aarav", "Meera", "Soham", "Riya", "Aarav", "Kabir", "Meera"]
print(names)

unique_names = []

for name in names:
    if name not in unique_names:
        unique_names.append(name)

print(unique_names)

# C2 - Delivery time analysis
print("\nC2")
times = [32, 45, 28, 50, 36, 41, 25, 39, 47, 30]
print(times)

average_time = sum(times) / len(times)
fastest = min(times)
slowest = max(times)

print("Average delivery time:", average_time)
print("Fastest delivery time:", fastest)
print("Slowest delivery time:", slowest)
