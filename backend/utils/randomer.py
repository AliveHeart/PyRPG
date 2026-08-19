import random

def weighted_choice(weightage_dict):
 
    total = sum(weightage_dict.values())
    roll = random.uniform(0, total)
    cumulative = 0

    for action, weight in weightage_dict.items():
        cumulative += weight
        if roll <= cumulative:
            return action