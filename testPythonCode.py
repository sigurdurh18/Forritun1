class 
class Database:
    def __init__(self):
        with open(database.txt) as fil:
            self.data=set()
            for line in fil:
