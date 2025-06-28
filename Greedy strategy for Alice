import numpy as np

payoff = [
    [(0.5, 0, 0.5), (7/10, 0, 3/10), (5/11, 0, 6/11)], 
    [(3/10, 0, 7/10), (1/3, 1/3, 1/3), (3/10, 1/2, 1/5)], 
    [(6/11, 0, 5/11), (1/5, 1/2, 3/10), (1/10, 4/5, 1/10)]
]


class Alice:
    def __init__(self):
        self.past_play_styles = np.array([1,1])  
        self.results = np.array([1,0])           
        self.opp_play_styles = np.array([1,1])  
        self.points = 1

    def play_move(self):
        """
        Decide Alice's play style for the current round. Implement your strategy for 2a here.
         
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
        if self.results[-1] == 1:#bob won last round -- play defence
            return 2
        elif self.results[-1] == 0.5:#last round was drawn -- play balanced
            return 1
        else:  #bob lost last round -- play attack
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
    
        alice_win = p < p_alice#boolean which stores whether alice wins or not
        alice.observe_result(alice_style, bob_style, int(alice_win))
        bob.observe_result(bob_style, alice_style, int(not alice_win))

    else:
        p_alice, p_draw, p_bob = payoff_matrix[alice_style][bob_style]
    
        if p < p_alice:
            result_alice, result_bob = 1, 0
        elif p < p_alice + p_draw:
            result_alice, result_bob = 0.5, 0.5
        else:
            result_alice, result_bob = 0, 1

        alice.observe_result(alice_style, bob_style, result_alice)
        bob.observe_result(bob_style, alice_style, result_bob)


    
    


def monte_carlo(num_rounds):
    """
    Runs a Monte Carlo simulation of the game for a specified number of rounds.
    
    Returns:
        None
    """
    alice = Alice()
    bob = Bob()
    for i in range(num_rounds):
        simulate_round(alice, bob, payoff)
    
    print(f"Alice's points: {alice.points}")
    print(f"Bob's points: {bob.points}")
    
 

# Run Monte Carlo simulation with a specified number of rounds
if __name__ == "__main__":
    monte_carlo(num_rounds=10**5)
