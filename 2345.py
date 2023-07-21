team = list(map(int, input().split(" ")))

equipe1 = min(team) + max(team)

team.remove(min(team))
team.remove(max(team))

equipe2 = team[0] + team[1]

difference = max(equipe1, equipe2) - min(equipe1, equipe2)

print(difference)