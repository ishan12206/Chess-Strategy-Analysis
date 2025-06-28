# Chess-Strategy-Analysis


This project simulates and analyzes strategic decision-making in a probabilistic multi-round game between two agents—**Alice** and **Bob**—who can adopt various playing styles: aggressive, balanced, or defensive. It computes optimal strategies and evaluates expected outcomes using Monte Carlo simulations across various probabilistic configurations.

---

## 📌 Problem Overview

- **Players**: Alice and Bob  
- **Actions**: Attack (0), Balanced (1), Defence (2)  
- **Outcomes**: Win (+1), Draw (0), Loss (–1)  
- **Payoff**: Defined by a probabilistic matrix based on both players' actions.

---

## 🧠 Payoff Matrix

The result of a match between Alice and Bob is determined by the following probabilistic matrix:

| **Alice / Bob** | **Attack**          | **Balanced**       | **Defence**         |
|------------------|----------------------|---------------------|----------------------|
| **Attack**       | (0.5, 0, 0.5)         | (0.7, 0, 0.3)        | (5/11, 0, 6/11)       |
| **Balanced**     | (0.3, 0, 0.7)         | (1/3, 1/3, 1/3)      | (0.3, 0.5, 0.2)       |
| **Defence**      | (6/11, 0, 5/11)       | (0.2, 0.5, 0.3)      | (0.1, 0.8, 0.1)       |

Each tuple corresponds to **(P_win, P_draw, P_lose)** from **Alice’s perspective**.

---

## 🔍 Key Features

- **Custom Probabilistic Payoff Modeling**  
  Encodes game outcomes using rich stochastic distributions per action pair.

- **Optimal Strategy Computation**  
  Calculates expected reward for each of Alice’s strategies assuming Bob plays uniformly at random.

- **Monte Carlo Evaluation**  
  Uses repeated random simulations to validate the theoretical optimal strategy over multiple rounds.

- **Statistical Outcome Estimation**  
  Computes long-term performance metrics such as expected score and win rate distribution.

---

## 📊 Applications

- Strategy benchmarking in stochastic environments  
- Decision-making under uncertainty  
- Modeling behavior in adversarial game theory  
- Applied reinforcement learning simulations
