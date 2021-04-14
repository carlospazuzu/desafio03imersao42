from player import Player
from deathtypes import deathtypes

class Match:

    def __init__(self):
        self._total_kills = 0
        self.players = {} 
        self.kills = {}
        self._deaths_by_type = {}

    
    def insert_new_player(self, new_player_id):
        if not new_player_id in self.players.keys():
            self.players[new_player_id] = Player(new_player_id)


    def change_player_name(self, player_id, new_name):
        if player_id in self.players.keys():
            self.players[player_id].name = new_name


    def change_player_frag(self, player_id, score): 
        if player_id in self.players.keys():
            self.players[player_id].frags = self.players[player_id].frags + score

    def increase_player_deaths(self, player_id): 
        if player_id in self.players.keys():
            self.players[player_id].increase_deaths()

    
    def increase_death_by_type(self, death_type):
        if death_type >= len(deathtypes):
            return
        if not deathtypes[death_type] in self.deaths_by_type:
            self.deaths_by_type[deathtypes[death_type]] = 1
        else:
            self.deaths_by_type[deathtypes[death_type]] += 1


    def increment_total_kills(self):
        self._total_kills += 1

    @property
    def total_kills(self):
        return self._total_kills

    @property
    def deaths_by_type(self):
        return self._deaths_by_type

    """
    def get_results(self):
        print('Players: ', self.players)
        print('Deaths by type: ', self.deaths_by_type)
        print('Total Kills: ', self.total_kills)
    """


    def get_players_amount(self):
        return len(self.players.keys())
