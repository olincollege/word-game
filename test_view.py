import pytest
from word_game import WordGameView

class TestWordGameView:
    def test_draw_board(self):
        view = WordGameView(800, 600, [])
        view.draw_board("test", [(100, 100, 20)])

    def test_draw_target_word(self):
        view = WordGameView(800, 600, [])
        view.draw_target_word("test")

    def test_draw_letter_bubbles(self):
        view = WordGameView(800, 600, [])
        view.draw_letter_bubbles([(100, 100, 20)])

    def test_update_display(self):
        view = WordGameView(800, 600, [])
        view.update_display()

    def test_handle_events(self):
        view = WordGameView(800, 600, [])

    def test_get_click_position(self):
        view = WordGameView(800, 600, [])
        click_pos = view.get_click_position()
        assert isinstance(click_pos, tuple)
        assert len(click_pos) == 2

    def test_close(self):
        view = WordGameView(800, 600, [])
        # This would terminate the test run