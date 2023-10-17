def premier_league_standings(teams: dict) -> dict:
    first = teams.pop(1)
    sort_teams = sorted(teams.values())
    sort_teams.insert(0, first)
    places_list = [i for i in range(1, len(sort_teams) + 1)]
    new_dict = dict(zip(places_list, sort_teams))
    return new_dict






print(premier_league_standings({2: 'Arsenal', 3: 'Accrington Stanley', 1: 'Leeds United'}))