# Difficulty levels for the chess engine

# This module defines functions to set the difficulty level of the chess engine.
# The difficulty levels (easy, hard, master) adjust the engine's behavior by modifying
# search depth or evaluation parameters.

def set_difficulty(level):
    """
    Set the difficulty level for the chess engine.

    Parameters:
    level (str): The difficulty level. Options are 'easy', 'hard', or 'master'.

    Returns:
    dict: A dictionary containing the parameters for the specified difficulty level.
    """
    if level == 'easy':
        return {
            'search_depth': 2,  # Shallow search depth for easy level
            'evaluation_factor': 0.5  # Weaker evaluation for easy level
        }
    elif level == 'hard':
        return {
            'search_depth': 4,  # Moderate search depth for hard level
            'evaluation_factor': 1.0  # Standard evaluation for hard level
        }
    elif level == 'master':
        return {
            'search_depth': 6,  # Deep search depth for master level
            'evaluation_factor': 1.5  # Stronger evaluation for master level
        }
    else:
        raise ValueError("Invalid difficulty level. Choose 'easy', 'hard', or 'master'.")