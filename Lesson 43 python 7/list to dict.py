def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]
    return result

student = [[1, 'jean castro', 'V'], [2, 'Luke Castellan', 'V'], [3, 'Brian Howell', 'VI'], [4, 'lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]

print("\n Origina list of lists:")
print(student)

print("\n Converted list to dictionary:")
print(test(student))
