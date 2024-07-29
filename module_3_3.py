def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params()
print_params('Test')
print_params(2, 'Test')
print_params(False, 2, 'Test')
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [11, 'list', True]
values_dict = {'a': 12, 'b': 'dict', 'c': False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [13, 'list2']
print_params(*values_list_2, 0.1)