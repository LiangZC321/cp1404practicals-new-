MENU = """
Menu:
(G)et a valid score
(P)rint result
(S)how stars
(Q)uit
"""

def evaluate_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"
