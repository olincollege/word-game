"""
Module for unit testing game model.
"""
from word_game import Game
from word_view import View
from word_controller import Controller


def test_type():
    """
    Tests the type of given variable. Assert is true if variable and 
    type matches.
    """
    controller = Controller()
    view = View()
    game = Game(controller, view)
    assert isinstance(game.word_list, list) is True


def test_generate_word():
    """
    Tests that the generated word is in the word list.
    """
    controller = Controller()
    view = View()
    game = Game(controller, view)
    game.load_word_list()
    game.generate_word()
    assert game.current_word in game.word_list


def test_bubble_list():
    """
    Tests that correct letters are properly placed in the list.
    """
    controller = Controller()
    view = View()
    game = Game(controller, view)
    assert isinstance(game.generate_letters(), list) is True


def test_generate_letters():
    """
    Tests that the function generates a list that has expected number of 
    letters. Since there will always be seven incorrect letters, we expect 
    to have a greater amount of letters than seven.
    """
    controller = Controller()
    view = View()
    game = Game(controller, view)
    game.load_word_list()
    game.generate_word()
    assert len(game.generate_letters()) > 7
