class HourClock:
    def __init__(self, hours) -> None:
        self.hours = hours
    def get_hours(self):
        return self._hours
    def set_hours(self, hours):
        if isinstance(hours, int) or hours in list(range(1, 13)):
            self._hours = hours
        else:
            raise ValueError('Неккоректное время')
    
    hours = property(get_hours, set_hours)
    

time = HourClock(7)

print(time.hours)
time.hours = 9
print(time.hours)