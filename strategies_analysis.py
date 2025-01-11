import csv
from collections import defaultdict

def strategies_analysis(results, players, output_file="player_strategies_rankings.csv"):
    data = {player: defaultdict(lambda: {'rankings': defaultdict(list), 'scores': defaultdict(list)}) for player in players}

    for result in results:
        combination = result['combination']
        scores = result['scores']
        ranking = result['ranking']

        for i, (player, _) in enumerate(ranking):
            rank = i + 1
            for p in players:
                data[p][combination[p]]['rankings'][player].append(rank)
                data[p][combination[p]]['scores'][player].append(scores[player])

    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Player", "Strategy", "Avg Ranking of A", "Avg Ranking of B", "Avg Ranking of C", "Avg Ranking of D",
                         "Avg Score of A", "Avg Score of B", "Avg Score of C", "Avg Score of D"])

        for player in players:
            for strategy, details in data[player].items():
                avg_rankings = {p: sum(details['rankings'][p]) / len(details['rankings'][p]) for p in players}
                avg_scores = {p: sum(details['scores'][p]) / len(details['scores'][p]) for p in players}
                writer.writerow([
                    player, strategy,
                    avg_rankings["A"], avg_rankings["B"], avg_rankings["C"], avg_rankings["D"],
                    avg_scores["A"], avg_scores["B"], avg_scores["C"], avg_scores["D"]
                ])

    return data
