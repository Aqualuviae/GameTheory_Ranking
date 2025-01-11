from dynamic_strategy import dynamic_strategy_simulation

# Initial setup
initial_scores = {"A": 10, "B": 8, "C": 6, "D": 4}
players = list(initial_scores.keys())

# Score change rules
score_changes = {
    'attack': {'lose': 2, 'gain': 1},
    'protect': {'lose': 0, 'gain': 1},
    'ignore': {'lose': 0, 'gain': 0}
}

def main():
    print("Dynamic Strategy Simulation")
    num_rounds = int(input("Enter the number of steps for the dynamic strategy simulation: "))
    print(f"Running dynamic strategy simulation for {num_rounds} steps...")
    dynamic_results = dynamic_strategy_simulation(initial_scores, num_rounds, players, score_changes)
    print(f"Simulation complete. Results saved to dynamic_strategy.csv")

if __name__ == "__main__":
    main()
