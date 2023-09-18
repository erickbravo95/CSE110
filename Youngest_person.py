
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

lowest_age = 200
name_youngest = ""

for line in people:
    line2 = line.split(" ")
    name = line2[0]
    ages = int(line2[1])
    if ages < lowest_age:
        lowest_age = ages
        name_youngest = name

print(f"The lowest age is: {lowest_age}")
print(f"The name of the youngest person is: {name_youngest}")