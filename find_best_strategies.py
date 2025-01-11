import csv

def find_best_strategies(data, players, output_file="best_strategies.csv"):
    best_strategies = {}

    for player in players:
        best_strategy = None
        best_rank = float('inf')
        best_score = float('-inf')
        min_opponent_score = float('inf')

        for strategy, details in data[player].items():
            avg_rank = sum(details['rankings'][player]) / len(details['rankings'][player])
            avg_score = sum(details['scores'][player]) / len(details['scores'][player])

            opponent_scores = [
                sum(details['scores'][opponent]) / len(details['scores'][opponent])
                for opponent in players if opponent != player
            ]
            total_opponent_score = sum(opponent_scores)

            if (avg_rank < best_rank or
                (avg_rank == best_rank and avg_score > best_score) or
                (avg_rank == best_rank and avg_score == best_score and total_opponent_score < min_opponent_score)):
                best_rank = avg_rank
                best_score = avg_score
                best_strategy = strategy
                min_opponent_score = total_opponent_score

        best_strategies[player] = (best_strategy, best_rank, best_score)

    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Player", "Best Strategy", "Avg Ranking", "Avg Score"])
        for player, (strategy, rank, score) in best_strategies.items():
            writer.writerow([player, strategy, rank, score])

    return best_strategies
