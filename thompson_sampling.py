# IMPORT LIBRARIES
# ================
import numpy as np

# DEFINE ENVIRONMENT 
# ==================
# set quantity of limited resource (time, money, turns)
number_of_rounds = 1000  

# set quantity of available options to choose from
number_of_options = 5  

# empty arrays to track each option's :
# number of wins (times reward obtained) 
# losses (times reward NOT obtained) 
total_wins = np.zeros(number_of_options)
total_losses = np.zeros(number_of_options)
# format:
#    option1(0)      option2(1)    ...        
# [option1 wins,   option2 wins,   ... ]
# [option1 losses, option2 losses, ... ]

# randomly generate each option's win probability between a range
# these theoretical conversion rates will be used to generate dataset
conversion_rates = np.random.uniform(0.01, 0.15, number_of_options) 
# example:      o1      o2     o3
#             [0.147, 0,138, 0.099, ...]

# showcase conversion rates for each available option
# note this information is not known to the learner in a real-world scenario
for i in range(number_of_options):
  print('Conversion rate for option ' + str(i) + ": " + str((conversion_rates[i] * 100))[:5] + "%") 
print("\n")

# CREATE DATASET
# ==============
# data set is a matrix: each row represents a round, each column represents an option
# Each matrix element represents the outcome of what would happen if a specific option was selected
# "1" indicates a win, "0" indicates a lose. 

# create 2D numpy array, filled with zeros
outcomes = np.zeros((number_of_rounds, number_of_options)) 
for round in range(number_of_rounds): 
    for option in range(number_of_options): 
        # Generate random number between 0.0 and 1.0
        # random number <= option conversion rate means outcome is "1", otherwise "0"
        if np.random.rand() <= conversion_rates[option]:
            outcomes[round][option] = 1

# display the first 15 rows of data
print(outcomes[0:15, 0:6]) 
print("\n")

# calculate actual conversion rates for each option in current simulation
for i in range(number_of_options):
  print('Mean for option {0}: {1:.2%}'.format(i, np.mean(outcomes[:, i])))
print("\n")

# RUN SIMULATION
# ==============
# constaints: only select 1 option per round
for round in range(number_of_rounds):
    selected_option_index = -1
    max_beta = -1

    # determine which option to select this round
    for option_index in range(number_of_options): 
        # define parameters for beta distribution
        a = total_wins[option_index] + 1
        b = total_losses[option_index] + 1

        # sample random value from the beta distribution
        random_beta = np.random.beta(a, b)

        # compare random_beta with largest beta value observbed thus far 
        if random_beta > max_beta:
            max_beta = random_beta 
            selected_option_index = option_index 
    
    # select appropriate option and record outcome
    if outcomes[round][selected_option_index] == 1:
        total_wins[selected_option_index] += 1
    else:
        total_losses[selected_option_index] += 1

# compute and display the total number of times each option was selected
total_rounds_playee = total_wins + total_losses 
for option_index in range(number_of_options): 
    print('Option {0} was selected {1} times'.format(option_index, total_rounds_playee[option_index]))

# identify and display the best option
print('\nConclusion: The best option was {}!'.format(np.argmax(total_rounds_playee)))