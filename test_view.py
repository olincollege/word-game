"""
Module for unit testing View class.
"""
from word_view import View

def test_draw_target_word():
    """
    Tests that the function properly draws text.
    """
    view = View()
    view.draw_target_word("test")
