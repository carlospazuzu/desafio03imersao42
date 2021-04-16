from entities.match import Match
import sys

from .reportgenerator import ReportGenerator

class Orchestrator:

    def __init__(self):
        self.matches = []
        self.current_match_id = -1 


    def get_current_match(self):
        return self.matches[self.current_match_id]


    def get_player_id(self, log_line):
        colon_position = log_line.find('ClientUserinfoChanged:')
        player_id = int(log_line[colon_position + 23])
        return player_id

    
    def create_new_match(self):
        self.matches.append(Match())
        self.current_match_id = len(self.matches) - 1

    
    def handle_new_player_connection(self, current_line):
        player_id = self.get_player_id(current_line) 
        self.get_current_match().insert_new_player(player_id)


    def player_name_change_request(self, current_line):
        player_id = self.get_player_id(current_line) 
        name_starting_position = current_line.find('n\\') 
        player_name = ''
        for letter in current_line[name_starting_position + 2:]:
            if letter == '\\':
                break
            player_name += letter
        self.get_current_match().change_player_name(player_id, player_name)


    def handle_kill_routines(self, current_line):
        first_colon = current_line.find('Kill:')
        count = 0
        for letter in current_line[first_colon + 6:]:
            if letter == ':':
                break
            count += 1
        death_info_excerpt = current_line[first_colon + 6:first_colon + 6 + count]
        killer, victim, killing_method = [int(num) for num in death_info_excerpt.split(' ')]
        # if killer id is 1022, it means the player was "killed" by the world
        if killer == 1022:
            self.get_current_match().change_player_frag(victim, -1)
        else:
            self.get_current_match().change_player_frag(killer, 1)
            self.get_current_match().increase_player_deaths(victim)

        self.get_current_match().increase_death_by_type(killing_method)
        self.get_current_match().increment_total_kills()

    
    def parse_quake_log(self, quake_log_filename):
        quake_log_file = open(quake_log_filename, 'r') 
        file_lines = quake_log_file.readlines() 
        quake_log_file.close()
        line_counter = 0
        for current_line in file_lines:            
            line_counter += 1

            # forces the exit of latest match and start logging info of a new one
            if current_line.find('InitGame') != -1:                
                self.create_new_match()
            # insert a new player into the match and ignores if it is already on the list
            if current_line.find('ClientConnect') != -1:
                self.handle_new_player_connection(current_line)
            # change player name keeping the score and frags
            if current_line.find('ClientUserinfoChanged') != -1:                
                self.player_name_change_request(current_line)
            # handle kill routines as frags addition or removal and death by means couting
            if current_line.find('Kill') != -1:     
                self.handle_kill_routines(current_line)            
                

        report_generator = ReportGenerator()
        report_generator.generate(self.matches)        

