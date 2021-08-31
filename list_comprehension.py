temps = [221, 234, 340, 230]

new_temps = [temp / 10 for temp in temps]
print(new_temps)

temps = [221, 234, 340, -9999, 230]
new_temps = [temp / 10 for temp in temps if temp != -9999]
print(new_temps)

# [i*2 for i in [1, -2, 10] if i>0]


def foo(my_list):
    return [item if type(item) != str else 0 for item in my_list]
