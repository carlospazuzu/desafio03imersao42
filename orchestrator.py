from match import Match
import sys


class Orchestrator:

    def __init__(self):
        self.matches = []
        self.current_match_id = -1 


    def get_current_match(self):
        return self.matches[self.current_match_id]


    def get_player_id(self, log_line):
        colon_position = log_line.find(':')
        player_id = int(log_line[colon_position + 2])
        return player_id

    
    def parse_quake_log(self, quake_log_filename):
       quake_log_file = open(quake_log_filename, 'r') 
       file_lines = quake_log_file.readlines() 
       quake_log_file.close()
       for current_line in file_lines:

            # print(current_line)

            # forces the exit of latest match and start logging info of a new one
            if current_line.find('InitGame'):
                self.matches.append(Match())
                self.current_match_id = len(self.matches) - 1
            # 
            if current_line.find('ClientConnect') != -1:
                player_id = self.get_player_id(current_line) 
                self.get_current_match().insert_new_player(player_id)
            #
            if current_line.find('ClientUserinfoChanged') != -1:
                player_id = self.get_player_id(current_line) 
                name_starting_position = current_line.find('n\\') 
                player_name = ''
                for letter in current_line[name_starting_position + 2:]:
                    if letter == '\\':
                        break
                    player_name += letter
                self.get_current_match().change_player_name(player_id, player_name)

            if current_line.find('Kill') != -1: 
                first_colon = current_line.find('Kill:')
                count = 0
                for letter in current_line[first_colon + 6:]:
                    if letter == ':':
                        break
                    count += 1
                death_info_excerpt = current_line[first_colon + 6:first_colon + 6 + count]
                killer, victim, killing_method = [int(num) for num in death_info_excerpt.split(' ')]
                if killer == 1022:
                    pass
                else:
                    pass
                self.get_current_match().increment_total_kills()
                return




