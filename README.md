# ThompsonSampling
Implementation of Thompson Sampling in Python 
Thompson Sampling is a method of solving the exploration-exploitation dilemma in a multi-armed bandit problem by building up a probability model from previously obtained rewards, and then sampling from this to determine an action.

Model implements ***Bayesian Inference,*** where the level of confidence (of obtaining the estimated reward) provided by the model increases as more samples are collected.

Procedure:
1. For each available option, take a random draw from a *beta distribution* whose shape is determined by 2 parameters (initially set to 1.0) :
 ‘*α*’ (alpha) - How many times that option DID yield a reward ✅ 
‘*β*’ (beta) - How many times that option DID NOT yield a reward ❌ 
2. Pursue option with highest beta value
3. Record whether a reward was obtained or not
