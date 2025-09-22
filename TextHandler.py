# Класс TextHandler

class TextHandler:
    def __init__(self, lst = []):
        self.lst = lst
    
    def add_words(self, text):
        for i in text.split():
            self.lst.append(i)

    def get_shortest_words(self):
        if self.lst:
            a = list(map(len, self.lst))
            mn, mx = min(a), max(a)
            return list(filter(lambda x: len(x) == mn, self.lst))
        else: return []
    
    def get_longest_words(self):
        if self.lst:
            a = list(map(len, self.lst))
            mn, mx = min(a), max(a)
            return list(filter(lambda x: len(x) == mx, self.lst))
        else: return []


texthandler = TextHandler()

texthandler.add_words('The world will hold my trial for your sins')
texthandler.add_words('Never meant to see the sky never meant to live')

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())