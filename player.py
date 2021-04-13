class Player(object):

    def __init__(self, id):
        self._id = id
        self._name = '' 
        self._frags = 0
        self._inventory = []

    @property
    def id(self):
        return self._id

    @property
    def name(self): 
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name 

    @property
    def frags(self):
        return self._frags

    @frags.setter
    def frags(self, new_frags):
        self._frags = new_frags 
