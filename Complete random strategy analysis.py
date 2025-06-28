import random
#Bob plays uniformly randomly
# Reward matrix: Alice_action vs Bob_action
# Actions: 0 = Attack, 1 = Balanced, 2 = Defence
reward_matrix = [
    [0, 1, -1],   # Alice plays Attack
    [-1, 0, 1],   # Alice plays Balanced
    [1, -1, 0]    # Alice plays Defence
]

def optimal_strategy(na, nb, tot_rounds):
    """
    Calculate the optimal strategy for Alice to maximize her points in future rounds
    given current scores of Alice (na) and Bob (nb), and rounds left.
    
    Returns: 
        0 : Attack
        1 : Balanced
        2 : Defence
    """
    best_action = None
    best_expectation = float('-inf')

    for alice_action in range(3):
        expected_reward = 0
        for bob_action in range(3):
            expected_reward += (1/3) * reward_matrix[alice_action][bob_action]
        if expected_reward > best_expectation:
            best_expectation = expected_reward
            best_action = alice_action

    return best_action

def simulate_rounds(tot_rounds, alice_strategy):
    """
    Simulate 'tot_rounds' rounds where Bob plays randomly and Alice plays a fixed strategy.
    Returns the total score Alice gets.
    """
    score = 0
    for _ in range(tot_rounds):
        bob_action = random.choice([0, 1, 2])  # Bob plays uniformly
        score += reward_matrix[alice_strategy][bob_action]
    return score

if __name__ == "__main__":
    # Step 1: Get T = T3T4 from Entry Number (replace 0 with 9)
    T = 74  # From your input

    # Step 2: Initial scores (can be ignored for uniform Bob)
    na = 0
    nb = 0

    # Step 3: Compute best strategy for Alice
    strategy = optimal_strategy(na, nb, T)
    print(f"Optimal strategy for Alice: {['Attack', 'Balanced', 'Defence'][strategy]} ({strategy})")

    # Step 4: Monte Carlo simulation to validate expected outcome
    trials = 10000
    scores = [simulate_rounds(T, strategy) for _ in range(trials)]
    expected_score = sum(scores) / trials

    print(f"Expected total score after {T} rounds: {expected_score:.2f}")
