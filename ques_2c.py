import numpy as np

class Alice:
    def __init__(self):
        self.past_play_styles = np.array([1,1])  
        self.results = np.array([1,0])           
        self.opp_play_styles = np.array([1,1])  
        self.points = 1

    def play_move(self):
        """
        Decide Alice's play style for the current round.
        
        Returns: 
            0 : attack
            1 : balanced
            2 : defence

        """
        if self.results[-1] == 0:
            return 1 # last round was drawn so play balanced
        elif self.results[-1] == 1:
            if (1-(self.points)/len(self.results))>= 6/11:#attack strategy is better
                return 0 
            else:
                return 2 #defence strategy is better
        else:
            return 0
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Alice's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
        self.results = np.append(self.results,result)
        self.past_play_styles = np.append(self.past_play_styles,own_style)
        self.opp_play_styles = np.append(self.opp_play_styles,opp_style)
        self.points += result
       

class Bob:
    def __init__(self):
        # Initialize numpy arrays to store Bob's past play styles, results, and opponent's play styles
        self.past_play_styles = np.array([1,1]) 
        self.results = np.array([0,1])          
        self.opp_play_styles = np.array([1,1])   
        self.points = 1

    def play_move(self):
        """
        Decide Bob's play style for the current round.

        Returns: 
            0 : attack
            1 : balanced
            2 : defence
        
        """
        if self.results[-1] == 1:
            return 2
        elif self.results[-1] == 0.5:
            return 1
        else:  
            return 0
        
        
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Bob's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
        self.past_play_styles = np.append(self.past_play_styles,own_style)
        self.results = np.append(self.results,result)
        self.opp_play_styles =  np.append(self.opp_play_styles,opp_style)
        self.points += result
 

def simulate_round(alice, bob, payoff_matrix):
    """
    Simulates a single round of the game between Alice and Bob.
    
    Returns:
        None
    """
    alice_style = alice.play_move()
    bob_style = bob.play_move()
    p = np.random.rand()

    if alice_style == 0 and bob_style == 0:
        p_alice = bob.points / (alice.points + bob.points)
    
        alice_win = p < p_alice #boolean which stores whether alice wins or not

        #record the results for alice and bob
        #if alice loses then int(alice_win) = 0 and 1 otherwise
        alice.observe_result(alice_style, bob_style, int(alice_win))
        bob.observe_result(bob_style, alice_style, int(not alice_win))

    else:
        p_alice, p_draw, p_bob = payoff_matrix[alice_style][bob_style]
    
        if p < p_alice:
            result_alice, result_bob = 1, 0 #alice wins 
        elif p < p_alice + p_draw:
            result_alice, result_bob = 0.5, 0.5 #draw
        else:
            result_alice, result_bob = 0, 1 #bob wins

        alice.observe_result(alice_style, bob_style, result_alice)
        bob.observe_result(bob_style, alice_style, result_bob)

def estimate_tau(T):
    """
    Estimate the expected value of the number of rounds taken for Alice to win 'T' rounds.
    Your total number of simulations must not exceed 10^5.

    Returns:
        Float: estimated value of E[tau]
    """
    tau_total = 0  # Sum of total rounds played across all simulations
    num_simulations = 0
    max_rounds = 10**3

    payoff_matrix = [
        [(0.5, 0, 0.5), (7/10, 0, 3/10), (5/11, 0, 6/11)], 
        [(3/10, 0, 7/10), (1/3, 1/3, 1/3), (3/10, 1/2, 1/5)], 
        [(6/11, 0, 5/11), (1/5, 1/2, 3/10), (1/10, 4/5, 1/10)]
    ]

    # Loop through multiple simulations
    for _ in range(max_rounds):
        alice = Alice()
        bob = Bob()
        num_wins = 0
        round_count = 0 

        while num_wins < T:
            simulate_round(alice, bob, payoff_matrix)
            round_count += 1  # Increment round count
            
            if alice.results[-1] == 1:
                num_wins += 1  # Increment win count for Alice

        
        tau_total += round_count
        num_simulations += 1

    # Estimate tau by averaging total rounds across all simulations
    estimate_tau = tau_total / num_simulations
    return estimate_tau
            
#T = 74 
print(f"Estimated value of tau after 10^3 interations of monte carlo simulations",estimate_tau(74))


        
    
        
    