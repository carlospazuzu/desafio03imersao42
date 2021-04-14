class Player(object):

    def __init__(self, id):
        self._id = id
        self._name = '' 
        self._frags = 0
        self._deaths = 0
        self._inventory = []

    """
    def __repr__(self):
        return '<Player: ' + self._name + ', kills: ' + str(self.frags) + ' >'
    """

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
    def deaths(self): 
        return self._deaths

    
    def increase_deaths(self):
        self._deaths += 1


    @property
    def frags(self):
        return self._frags


    @frags.setter
    def frags(self, new_frags):
        self._frags = new_frags 
