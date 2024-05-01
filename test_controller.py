"""
Unit tests for the Controller class.
"""
from word_controller import Controller

def test_update_score():
    """
    Tests that the score correctly adds one to current score.
    """
    controller = Controller()
    controller.score = 10
    controller.update_score()
    assert controller.score == 11
def test_time_penalty():
    """
    Tests that the time correctly subtracts three from the current time 
    remaining.
    """
    controller = Controller()
    controller.time_remaining = 10
    controller.time_penalty()
    assert controller.time_remaining == 7
