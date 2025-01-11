import itertools
import csv

def traverse_strategies(initial_scores, num_rounds, players, player_strategies, score_changes, output_file="strategies_results.csv"):
    def update_scores(scores, strategies):
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

    def calculate_ranking(scores):
        return sorted(scores.items(), key=lambda x: x[1], reverse=True)

    all_combinations = list(itertools.product(*player_strategies.values()))
    results = []

    for combination in all_combinations:
        strategies_combination = {players[i]: combination[i] for i in range(len(players))}
        scores = initial_scores.copy()

        for _ in range(num_rounds):
            scores = update_scores(scores, strategies_combination)

        ranking = calculate_ranking(scores)
        results.append({
            'combination': strategies_combination,
            'scores': scores,
            'ranking': ranking
        })

    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Strategy Combination", "Final Scores", "Final Ranking"])
        for result in results:
            writer.writerow([
                result['combination'],
                result['scores'],
                result['ranking']
            ])

    return results
