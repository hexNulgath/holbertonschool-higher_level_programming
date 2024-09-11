#!/usr/bin/python3
def best_score(a_dictionary):
    score = None
    if a_dictionary:
        score = 0
        for key in a_dictionary:
            if a_dictionary[key] > score:
                score = a_dictionary[key]
    return score
