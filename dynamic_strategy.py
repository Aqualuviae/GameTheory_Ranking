import csv


def load_best_strategies (file_path="best_strategies.csv"):
    """Load the best strategies and convert player names to rankings."""
    best_strategies = {}
    player_to_rank = {'A': 1, 'B': 2, 'C': 3, 'D': 4}

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            player = row['Player']
            strategy = eval(row['Best Strategy'])
            best_strategies[player_to_rank[player]] = tuple(player_to_rank[p] for p in strategy)
    return best_strategies


def dynamic_strategy_simulation (initial_scores, num_rounds, players, score_changes,
                                 output_file="dynamic_strategy.csv"):
    def update_scores (scores, strategies):
        new_scores = scores.copy()
        actions = {}

        for player, strategy in strategies.items():
            actions[player] = {
                'attack': strategy[0],
                'protect': strategy[1],
                'ignore': strategy[2]
            }

        for player, action in actions.items():
            target = action['attack']
            new_scores[target] -= score_changes['attack']['lose']
            new_scores[player] += score_changes['attack']['gain']

            protect_target = action['protect']
            new_scores[protect_target] += score_changes['protect']['gain']

        return new_scores

    def calculate_ranking (scores):
        return sorted(scores.items(), key=lambda x: x[1], reverse=True)

    dynamic_strategies = load_best_strategies()

    def rank_to_player (rank, ranking):
        return ranking[rank - 1][0]

    scores = initial_scores.copy()
    results = []

    for round_num in range(num_rounds):
        ranking = calculate_ranking(scores)
        ranking_to_player = {i + 1: ranking[i][0] for i in range(len(ranking))}

        strategies_combination = {}
        for rank, player in ranking_to_player.items():
            dynamic_strategy = dynamic_strategies[rank]
            strategies_combination[player] = tuple(rank_to_player(pos, ranking) for pos in dynamic_strategy)

        scores = update_scores(scores, strategies_combination)
        results.append({'round': round_num + 1, 'scores': scores.copy(), 'ranking': calculate_ranking(scores)})

    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Round", "Final Scores", "Final Ranking"])
        for result in results:
            writer.writerow([
                result['round'],
                result['scores'],
                result['ranking']
            ])

    return results
