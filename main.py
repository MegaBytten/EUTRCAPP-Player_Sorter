import random

players_unsorted = ["Lucas M", "Holly R", "Theo L", "Dan T", "Callum P", "Ethan D", "Fiona S", "Hadrien D", "Luke O",
                    "Annie L", "Ben L", "Emily S", "Quitterie D", "Tom L", "James M", "Jack G", "Fran W", "Amelia R",
                    "Philip S", "Will M", "James Y", "Hannah G", "Ryan B", "Roni R", "Will B", "Grace H", "Liam R",
                    "Garance R", 'Alex G', 'Ed H', 'Sophia J', "Charlotte F", 'Nicholas P', 'Ben M', 'Alex N',
                    'Simon G', 'Callum H', 'Felix D', 'Cole G']

teams = 3
teams_sorted = []

if __name__ == '__main__':
    # This loop adds empty lists to our list that contains ALL teams - DEPENDENT ON TEAMS VAR
    # These sub-lists will then be filled with their respective players
    for x in range(teams):
        teams_sorted.append([])

    # This shuffles the list randomly, mixing players/teams
    random.shuffle(players_unsorted)
    team_cycle = 0

    # This loop cycles through all players and adds them 1 by 1 to each team
    # Resets the "team" assignment based on how many teams there are
    for x in range(len(players_unsorted)):
        if team_cycle >= teams: team_cycle = 0
        teams_sorted[team_cycle].append(players_unsorted[x])
        team_cycle += 1

    # Lastly this is the export of all the sorted teams
    print(teams_sorted)
