"""
"""
import pytest
from word_game import Game

def test_type():
    game = Game()
    assert isinstance(game.word_list, list) is True

def test_generate_word():
    game = Game()
    game.generate_word()
    assert game.current_word in game.word_list

def test_bubble_list():
    game = Game()
    assert isinstance(game.generate_letters(), list) is True

def test_generate_letters():
    game = Game()
    game.generate_word()
    assert len(game.generate_letters()) > 3

def test_timer():
    game = Game()
    