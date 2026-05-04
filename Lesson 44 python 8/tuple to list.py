def test(tpl):
    result = ()
    for item in tpl:
        result += (item,)
    return result

my_tuple = ('p','e','r','m','i','t',)

print("\n Original tuple:")
print(my_tuple)     

print("\n Converted tuple to list:")
print(test(my_tuple))