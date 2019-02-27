import json
import uuid
import datetime
import my_generator
from time import mktime, strftime, gmtime


class Player:
    def __init__(self, id, name, team):
        self.id = id
        self.name = name
        self.team = team


class Team:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.players = []


class Match:
    instances = []

    def __init__(self, team0, team1, id, date, location, result):
        self.__class__.instances.append(self)
        self.id = id
        self.date = date
        self.location = location
        self.result = result
        self.team0 = team0
        self.team1 = team1
        self.players = team0.players + team1.players

    def __str__(self):
        return "Date: {}\n" \
               "{} vs {} => {}\n" \
               "Players: {}".format(strftime("%d.%m.%Y", gmtime(self.date)),
                                    self.team0.name,
                                    self.team1.name,
                                    self.result,
                                    ", ".join([player.name for player in self.players]))


def init_instances():
    with open('teams.json', 'r')   as tm_fd, \
         open('players.json', 'r') as pl_fd, \
         open('matches.json', 'r') as mch_fd:

        teams = []
        for team in tm_fd:
            teams.append(Team(**json.loads(team)))

        players = []
        teams_cache = [item.id for item in teams]
        for player in pl_fd:
            player = json.loads(player)
            team = teams[teams_cache.index(player.pop('team'))]
            players.append(Player(team=team, **player))

        for team in teams:
            for player in players:
                if team is player.team:
                    team.players.append(player)

        matches = []
        for match in mch_fd:
            match = json.loads(match)
            team_1_2 = [teams[teams_cache.index(key)] for key in [match.pop(key) for key in ('team1', 'team2')]]
            matches.append(Match(*team_1_2, **match))
    return matches


def available_teams():
    with open('teams.json', 'r') as fd:
        teams = []
        for team in fd:
            team = json.loads(team)
            teams.append((team['id'], team['name']))
        return tuple(zip(*teams))


def add_player():
    teams = available_teams()
    print('\nAvailable teams:\n', ' | '.join(teams[1]), sep='')
    with open('players.json', 'a') as fd:
        while True:
            data = {
                'id':   str(uuid.uuid4())[:8],
                'name': input('Enter player name: ').strip(),
                'team': input('Enter player team: ').strip()
            }
            if not data['name'].isalpha() or data['team'] not in teams[1]:
                print('Wrong input')
                continue
            data['team'] = teams[0][teams[1].index(data['team'])]
            fd.write(json.dumps(data) + '\n')
            if input('Would you like to add another player? (Y/N): ') == 'N':
                print()
                break


def add_team():
    with open('teams.json', 'a') as fd:
        print()
        while True:
            data = {
                'id':   str(uuid.uuid4())[:8],
                'name': input('Enter player name: ').strip()
            }
            if not data['name'].isalpha():
                print('Wrong input')
                continue
            fd.write(json.dumps(data) + '\n')
            if input('Would you like to add another team? (Y/N): ') == 'N':
                print()
                break


def add_match():
    teams = available_teams()
    with open('matches.json', 'a') as fd:
        print('\nAvailable teams:\n', ' | '.join(teams[1]), sep='')
        while True:
            data = {
                'id':       str(uuid.uuid4())[:8],
                'date':     input('Enter match date (dd.mm.yyyy): ').strip(),
                'location': input('Enter match location: ').strip(),
                'result':   input('Enter match result (e.g. 1:0): ').strip(),
                'team1':    input('Enter match team1: ').strip(),
                'team2':    input('Enter match team2: ').strip(),
            }
            if not len([elem for elem in data.values() if elem]) == 6 \
                    or data['team1'] not in teams[1] \
                    or data['team2'] not in teams[1]\
                    or data['team1'] == data['team2']:
                print('Wrong input')
                continue
            data['team1'] = teams[0][teams[1].index(data['team1'])]
            data['team2'] = teams[0][teams[1].index(data['team2'])]
            try:
                data['date'] = mktime(
                    datetime.date(
                        *reversed([int(elem) for elem in data['date'].split('.')])
                    ).timetuple()
                )
            except Exception as err:
                print('Wrong date input:', err)
                continue
            fd.write(json.dumps(data) + '\n')
            if input('Would you like to add another match? (Y/N): ') == 'N':
                print()
                break


def search(matches):
    periods = [mch.date for mch in matches]
    while True:
        result = []
        print()
        data = input('Enter date or period (dd.mm.yyyy dd.mm.yyyy) or exit: ').strip().split()
        try:
            if data[0] == 'exit':
                break
            elif len(data) == 1:
                data = mktime(datetime.date(*reversed([int(elem) for elem in data[0].split('.')])).timetuple())
                for i, match_date in enumerate(periods):
                    if match_date == data:
                        result.append(matches[i])

            elif len(data) == 2:
                data = [mktime(datetime.date(*reversed([int(elem) for elem in date.split('.')])).timetuple())
                        for date in data]
                if data[0] > data[1]:
                    print('Wrong period: first date should be earlier then second one')
                    continue

                for i, match_date in enumerate(periods):
                    if match_date > data[0] and match_date < data[1]:
                        result.append(matches[i])
            else:
                print('Wrong period! Should one or two date string')
        except Exception as err:
            print('Wrong date input:', err)
            continue

        for i, match in enumerate(result):
            print(f'Match {i+1}\n'
                  f'{match}\n'
                  f'{"-"*80}')


def main():
    options = {
        'player': add_player,
        'team':   add_team,
        'match':  add_match
    }

    if input('Do you want to add initial data to database automatically? (Y/N): ') == 'Y':
        my_generator.main()

    while True:
        command = input('Do you want to add something to the Database?\n'
                        '( player | team | match | exit) -> ')
        if command == 'exit':
            break
        options.get(command, lambda: print('Wrong input!'))()
    matches = init_instances()
    search(matches)


if __name__ == '__main__':
    main()
