class Gun:
    def __init__(self):
        self.n = 0

    def shoot(self):
        self.n += 1
        if self.n % 2 != 0:
            print('pif')
        else:
            print('paf')

    def shots_count(self):
        print(self.n)

    def shots_reset(self):
        self.n = 0
        return None

gun1 = Gun()

gun1.shoot()
gun1.shoot()
gun1.shots_count()
gun1.shots_reset()
gun1.shots_count()