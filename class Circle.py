# объявление функции
def get_last_index(data: list, value: str):
    data = data[::-1]
    for i in range(len(data)):
        if data[i] == value:
            return i
        else: return 'ERROR!'
# считываем данные
value = eval(input())
data = eval(input())


# вызываем функцию
print(get_last_index(data, value))