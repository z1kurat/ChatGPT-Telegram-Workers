class Reader():

    def __init__(self, filename):
        with open(filename, encoding='utf-8') as file:
            self.data = [el.strip() for el in file.readlines()]
            self.time_waiting = len(self.data) // 3