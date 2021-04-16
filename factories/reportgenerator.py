import os

from utils.html_snippets import HEAD, LOGO, THEAD

class ReportGenerator:

    def __init__(self):
        pass

    def generate(self, matches_info):
        file = open('index.html', 'w')
        file.write(HEAD)
        file.write('<body>\n')
        file.write('<div class="container">\n')
        file.write(LOGO)
        count = 0
        for match in matches_info:
            count += 1
            file.write('<hr />')
            file.write('<div class="row">')
            file.write('<h3>Match #' + str(count) + ' Results</h3>')
            file.write('<table class="u-full-width">')
            file.write(THEAD)
            file.write('<tbody>')            
            for player_id, player_data in sorted(match.players.items(), key = lambda kv: kv[1].frags, reverse=True):
                file.write('<tr>')
                file.write('<td>' + player_data.name + '</td>')
                file.write('<td>' + str(player_data.frags) + '</td>')
                file.write('<td>' + str(player_data.deaths) + '</td>')
                if player_data.frags + player_data.deaths > 0 and player_data.frags > 0:
                    file.write('<td>' + "{:.1f}".format((player_data.frags / (player_data.frags + player_data.deaths)) * 100) + ' %</td>')
                else:
                    file.write('<td> 0.0 %</td>')
                file.write('</tr>')            
            file.write('</tbody>')
            file.write('</table>')            
            file.write('<h5>Statistics</h5>')
            file.write('<ul>')
            file.write('<li>Total Kills: ' + str(match.total_kills) + '</li>')
            file.write('<li>Death by means:</li>')
            file.write('<ul>')
            for death_key, death_score in match.deaths_by_type.items():
                file.write('<li>' + death_key + ': ' + str(death_score) + '</li>')
            file.write('</ul>')
            file.write('</ul>')
            file.write('</div>\n')

        file.write('</div>\n')
        file.write('</body>\n')
        file.write('</html>\n')
        file.close()

        os.system('echo Please open your browse into the address http://localhost:8000')
        os.system('python3 -m http.server')        