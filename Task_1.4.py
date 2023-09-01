import random

class ChessPlayer:
    def __init__(self, name, age, elo, tenacity, is_boring):
        self.name = name
        self.age = age
        self.elo = elo
        self.tenacity = tenacity
        self.is_boring = is_boring
        self.tournament_score = 0

    def simulate_match(self, opponent):
        elo_difference = abs(self.elo - opponent.elo)
        
        if elo_difference > 100:
            if self.elo > opponent.elo:
                self.tournament_score += 1
            else:
                opponent.tournament_score += 1
        elif 50 <= elo_difference <= 100:
            lower_elo_player = self if self.elo < opponent.elo else opponent
            higher_elo_player = opponent if self.elo < opponent.elo else self
            random_factor = random.randint(1, 10)
            if (random_factor * lower_elo_player.tenacity) > higher_elo_player.elo:
                lower_elo_player.tournament_score += 1
            else:
                higher_elo_player.tournament_score += 1
        else:
            if self.tenacity > opponent.tenacity:
                self.tournament_score += 1
            elif self.tenacity < opponent.tenacity:
                opponent.tournament_score += 1
            elif self.is_boring or opponent.is_boring:
                # If one player is boring, the match ends in a draw
                self.tournament_score += 0.5
                opponent.tournament_score += 0.5

# Example usage:
player1 = ChessPlayer("Alice", 30, 1500, 8, False)
player2 = ChessPlayer("Bob", 28, 1400, 7, True)
player3 = ChessPlayer("Charlie", 35, 1600, 9, False)

players = [player1, player2, player3]

for player in players:
    for opponent in players:
        if player != opponent:
            player.simulate_match(opponent)

# Print the tournament results
print("Tournament Results:")
for player in players:
    print(f"{player.name}: {player.tournament_score} points")
