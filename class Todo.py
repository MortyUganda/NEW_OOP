class Todo:
    def __init__(self):
        self.things = []
        
    def add(self, th, prior):
        self.things.append((th, prior))

    def get_by_priority(self, n):
        lst = list(filter(lambda x: x[1] == n, self.things))
        return [el[0] for el in lst]
    
    def get_low_priority(self):
        if self.things:
            low = min(self.things, key=lambda x: x[1])[1]
            return [el[0] for el in list(filter(lambda x: x[1] == low, self.things))]
        else: return []
            
    def get_high_priority(self):
        if self.things:
            high = max(self.things, key=lambda x: x[1])[1]
            return [el[0] for el in list(filter(lambda x: x[1] == high, self.things))]
        else: return []



todo = Todo()

print(todo.things)
print(todo.get_by_priority(1))
print(todo.get_low_priority())
print(todo.get_high_priority())