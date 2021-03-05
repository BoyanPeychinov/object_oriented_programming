from football_team_generator_03.player import Player
from football_team_generator_03.team import Team

player_1 = Player("p1", 5, 10, 2, 5, 6)
player_2 = Player("p2", 5, 10, 2, 1, 1)

t = Team("Team name", 5)
print(t.add_player(player_1))
print(t.add_player(player_1))
print(t.remove_player("p1"))
print(t.remove_player("p1"))
