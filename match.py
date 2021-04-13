from player import Player
from deathtypes import deathtypes

class Match:

    def __init__(self):
        self.total_kills = 0
        self.players = {} 
        self.kills = {}
        self.deaths_by_type = {}

    
    def insert_new_player(self, new_player_id):
        if not new_player_id in self.players.keys():
            self.players[new_player_id] = Player(new_player_id)


    def change_player_name(self, player_id, new_name):
        if player_id in self.players.keys():
            self.players[player_id].name = new_name


    def change_player_frag(self, player_id, score): 
        if player_id in self.players.keys():
            self.players[player_id].frags = self.players[player_id].frags + score


    def increment_total_kills(self):
        self.total_kills += 1
