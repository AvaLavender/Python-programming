lst = ['Apple', 'Guava', 'Mango', 'Banana', 'Kiwi' ]

print("Length of list:", len(lst))
print("First element:", lst[0])
print("Last element:", lst[-1])

lst.append('Papaya')
print("Upended list :", lst)

lst.remove('Guava')
print("Updated list:", lst)

lst.sort()
print("sorted list:", lst)

lst.pop(1)
print("Updated list:", lst)

lst.reverse()
print("reversed list:", lst)

print("multiplication on the list:", lst*2)

lst = lst[:4]
print("sliced list:", lst)

lst.clear()
print("Updated list:", lst)
