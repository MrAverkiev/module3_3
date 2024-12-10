#1 Функция с параметрами по умолчанию
def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
print_params()
print_params(23)
print_params([5,6,7],'cat')
print_params(123,True,(1,5,6,7))
print_params(b = 25)
print_params(c = [1,2,3])

#2 Распаковка параметров
values_list=['night',55,False]
values_dict={'a':3,'b':'food','c':True}
print_params(*values_list)
print_params(**values_dict)

#3 Распаковка + отдельные параметры
values_list_2=[33,'winter']
print_params(*values_list_2, 42)