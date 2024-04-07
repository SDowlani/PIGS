class Player:
    def __init__(self, name, id):
        self.name = name
        self._points = 0
        self.id = id
    def __str__(self):
        return f"Player {self.id}\n     Name: {self.name}\n     Points: {self.points}\n"
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Invalid Name")

        self._name = name
    
    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, amount : int):
        self._points = amount

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id