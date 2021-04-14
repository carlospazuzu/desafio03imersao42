import unittest

from player import Player
from match import Match
from deathtypes import deathtypes

class TestPlayerClass(unittest.TestCase):

    def setUp(self):
        self.player = Player(1)
        self.player2 = Player(2)

    def test_change_name(self):
        self.player.name = 'Bernardo'
        self.player.name = 'Augusto'
        self.assertEqual(self.player.name, 'Augusto', 'Player name must be Augusto')

    def test_change_player_frags(self):
        self.player.frags = 9999
        self.assertEqual(self.player.frags, 9999, 'Player frags amount must be 9999')

    def test_player_id_getter(self):
        self.assertEqual(self.player2.id, 2, 'Player2 id must be 2')


class TestMatchClass(unittest.TestCase):

    def setUp(self):
        self.match = Match()

    def test_add_new_player(self):
        previous_amount = self.match.get_players_amount()
        self.match.insert_new_player(new_player_id=1)
        self.assertEqual(self.match.get_players_amount(), previous_amount + 1, 'Players amount must be ' + str(previous_amount + 1))

    def test_add_same_player_twice(self):        
        self.match.insert_new_player(new_player_id=1)
        previous_amount = self.match.get_players_amount()
        self.match.insert_new_player(new_player_id=1)
        self.assertEqual(self.match.get_players_amount(), previous_amount, 'Players amount must be ' + str(previous_amount))

    def test_change_player_name(self):        
        self.match.insert_new_player(new_player_id=2)
        self.match.change_player_name(player_id=2, new_name='Alberto')
        self.match.change_player_name(player_id=2, new_name='Josias')
        self.match.change_player_name(player_id=2, new_name='Alberto')
        self.assertEqual(self.match.players[2].name, 'Alberto', 'The Player with id 2 must be named Alberto')

    def test_change_name_of_non_existing_player(self):        
        self.match.change_player_name(99, 'Julio')
        self.assertEqual(self.match.get_players_amount(), 0, 'Players amount must be zero, as none got changed')

    def test_change_player_frag(self):
        self.match.insert_new_player(new_player_id=4)
        self.match.change_player_frag(player_id=4, score=10)
        self.match.change_player_frag(player_id=4, score=-4)
        self.match.change_player_frag(player_id=4, score=20)
        self.assertEqual(self.match.players[4].frags, 26, 'Player id 4 frags must be 26')

    def test_change_frag_of_non_existing_player(self):        
        self.match.change_player_frag(99, 99)
        self.assertEqual(self.match.get_players_amount(), 0, 'Players amount must be zero, as none got changed')

    def test_increase_death_by_type_code_bigger_than_amount_existent(self):
        self.match.increase_death_by_type(death_type=66)
        self.assertEqual(len(self.match.deaths_by_type.keys()), 0, 'Death by types dict number of keys must be equal zero after this method call')

    def test_increase_death_by_type(self):
        for i in range(99):
            self.match.increase_death_by_type(death_type=19)

        self.assertEqual(self.match.deaths_by_type[deathtypes[19]], 99, 'Death type code 19 amount must be 99')

    def test_increment_total_kills(self):
        for i in range(39):
            self.match.increment_total_kills()
        
        self.assertEqual(self.match.total_kills, 39, 'Match total amount of kills must be 39')


def suite():
        suite = unittest.TestSuite()
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestPlayerClass))
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMatchClass))
        return suite

if __name__ == '__main__':
    # unittest.main()
    unittest.TextTestRunner(verbosity=2).run(suite())
