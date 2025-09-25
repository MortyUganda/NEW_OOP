def get_last_index(data: list, value: str):
    lst = [i for i in range(len(data)) if data[i] == value]
    
    if lst: 
        return lst[-1]
    return 'ERROR!'

data = eval(input())
value = eval(input())


print(get_last_index(data, value))