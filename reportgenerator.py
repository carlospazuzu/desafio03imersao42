import os
import webbrowser

class ReportGenerator:

    def __init__(self):
        pass

    def generate(self, matches_info):
        file = open('index.html', 'w')
        file.write('<!DOCTYPE html>\n')
        file.write('<html lang="en">\n')
        file.write('<head>\n')
        file.write('<meta charset="UTF-8">\n')
        file.write('<title>Quake Log Results</title>\n')
        file.write('''
                        <style>\n
                            h3 {\n
                                text-align: center;\n
                            }\n
                                \n
                            .gameLogo {\n
                                margin: 0 auto;\n
                                text-align: center;v
                                margin: 10px;\n
                            }\n
                        </style>\n
                   '''
        )
        file.write('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css" />')
        file.write('</head>\n')
        file.write('<body>\n')
        file.write('<div class="container">\n')
        file.write('''
                        <div class="row">\n
                            <div class="gameLogo">\n
                                <img width="35%" src="https://images.launchbox-app.com/c40ede74-dcb7-4f81-b197-967e3599df16.png" alt="">\n
                            </div>\n
                        </div>\n
                   '''
                   )
        count = 0
        for match in matches_info:
            count += 1
            file.write('<hr />')
            file.write('<div class="row">')
            file.write('<h3>Match #' + str(count) + ' Results</h3>')
            file.write('<table class="u-full-width">')
            file.write('''
                            <thead>
                                <tr>
                                    <th>Player Name</th>
                                    <th>Kills</th>
                                    <th>Deaths</th>
                                    <th>WR</th>
                                </tr>
                            </thead>
                       ''')
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

        os.system('python3 -m http.server')
        webbrowser.open('http://0.0.0.0:8000')