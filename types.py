# a = 2
# b = 0.5
# print(a + b)
# name = 'ВСТАВЬТЕ ВАШЕ ИМЯ'
# c = name .replace(name, 'Руслан')
# print('Привет', c,'!') 
# print(f'Привет {c}!')
# v = input('Введидте число от 1 до 10: ')
# d = int(v)
# g = d+10
# print(g)
# name = input('Введите ваше имя: ')
# t = str(name)
# print(f'Привет, {t}! Как дела?')

# print(float('1')) 
# print(int(float('2.5')))
# print(1) 
# print('')
# print(0)

# numbers = [3,5,7,9,10.5]
# numbers.append('Python')
# print(len(numbers))
# print(numbers[0])
# print(numbers[-1])
# print(numbers[1:4])
# numbers.remove('Python')

temper = {"city": "Москва", "temperature": "20"}
print(temper["city"])
temper['temperature'] = int(temper['temperature']) - 5
print(temper)
print(temper.get('country', 'Россия'))
temper['date'] = '27.05.2019'
print(temper)