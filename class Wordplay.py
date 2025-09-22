class Wordplay:
    def __init__(self, words=[]):
        self.words = words.copy()

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, length):
        return [el for el in self.words if len(el) == length]
    
    def only(self, *args):
        return [el for el in self.words if set(el).issubset(args)]

    def avoid(self, *args):
        return [el for el in self.words if set(el).isdisjoint(args)]


wordplay = Wordplay(['o', 'to', 'otto', 'top', 't'])

print(wordplay.only('o', 't'))


wordplay = Wordplay(['a', 'arthur', 'timur', 'bee', 'geek', 'python', 'stepik'])

print(wordplay.avoid('a', 'b', 'c'))

wordplay = Wordplay()
print(wordplay.words)

wordplay = Wordplay(['Тьюринг', 'Торвальдс', 'Россум', 'Гейтс', 'Гамильтон', 'Бэкус', 'Кнут'])

print(wordplay.words_with_length(6))
print(wordplay.avoid('ь'))


words = ['Лейбниц', 'Бэббидж', 'Нейман', 'Джобс', 'да_Винчи', 'Касперский']
wordplay = Wordplay(words)

words.extend(['Гуев', 'Харисов', 'Светкин'])
print(words)
print(wordplay.words)