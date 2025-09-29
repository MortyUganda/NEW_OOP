class Postman:
    def __init__(self):
        self.delivery_data = []

    def add_delivery(self, street, house, room):
        self.delivery_data.append((street, house, room))
        

    def get_houses_for_street(self, street):
        return list({el[1]:el for el in self.delivery_data if el[0] == street})
    
    def get_flats_for_house(self, street, house):
        return list({el[2]: el for el in self.delivery_data if el[0] == street and el[1] == house})

postman = Postman()

postman.add_delivery('SOvet', 151, 74)
postman.add_delivery('SOvet', 151, 75)
postman.add_delivery('SOvet', 90, 2)
postman.add_delivery('SOvet', 151, 74)

print(postman.get_houses_for_street('SOvet'))
print(postman.get_flats_for_house('SOvet', 151))





