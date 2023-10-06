# Создаём переменную
input_string = input('Введите последовательность чисел: ')

# Создаём функцию которая принимает input_string
def find_min_max(input_string):
  # Преобразуем строку в список
  input_string = input_string.replace(',', '.')
  list_string = list(input_string.split(' '))
  # Создаём пустой список
  new_list = []

  # Если елемент состоит полностью из букв, мы удаляем его из списка
  for elem in list_string:
    if elem.isalpha() is True:
      list_string.remove(elem)

  # Преобразуем строки в числа
  for a in list_string:
    if '.' in a:
      a = float(a)
      new_list.append(a)
    else:
      a = int(a)
      new_list.append(a)

  # Находим и возвращаем максимальное и минимальное значение списка
  max_count = max(new_list)
  min_count = min(new_list)
  pr = print('Manimum: {}'.format(min_count))
  return 'Maximim: {}'.format(max_count)

print(find_min_max(input_string))