import json
import uuid
import datetime
from random import sample
from time import mktime


def main():
    names = ['Fernanado', 'Pedro', 'Luchi', 'Balle', 'Gime', 'Menfo', 'Joei', 'Neqo', 'Li', 'Top']
    teams = ['team1', 'team2', 'team3', 'team4', 'team5']
    teams = [(str(uuid.uuid4())[:8], team) for team in teams]
    matches = [
        {'id': str(uuid.uuid4())[:8], 'date': mktime(datetime.date(2019, 6, 2).timetuple()), 'location': 'Minsk', 'result': '2:0'},
        {'id': str(uuid.uuid4())[:8], 'date': mktime(datetime.date(2019, 2, 5).timetuple()), 'location': 'Mogilev', 'result': '1:1'},
        {'id': str(uuid.uuid4())[:8], 'date': mktime(datetime.date(2019, 5, 13).timetuple()), 'location': 'Brest', 'result': '2:7'},
        {'id': str(uuid.uuid4())[:8], 'date': mktime(datetime.date(2019, 1, 26).timetuple()), 'location': 'Grodno', 'result': '4:1'},
        {'id': str(uuid.uuid4())[:8], 'date': mktime(datetime.date(2019, 3, 1).timetuple()), 'location': 'Vitebsk', 'result': '3:2'}
    ]

    with open('teams.json', 'w') as fd:
        for team in teams:
            fd.write(json.dumps({'id': team[0],
                                 'name': team[1]}) + '\n')

    with open('players.json', 'w') as fd:
        for player in zip(names, teams * 2):
            fd.write(json.dumps({'id': str(uuid.uuid4())[:8],
                                 'name': player[0],
                                 'team': player[1][0]}) + '\n')

    with open('matches.json', 'w') as fd:
        for match in matches:
            match.update((('team' + str(i+1), team[0]) for i, team in enumerate(sample(teams, 2))))
            fd.write(json.dumps(match) + '\n')

if __name__ == '__main__':
    main()
