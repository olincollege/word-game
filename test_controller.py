import pytest
import pygame
from word_controller import Controller
from word_game import Game
from word_view import WordGameView

class TestController:

    @pytest.fixture
    def controller_instance(self):
        game = Game()
        view = WordGameView()
        controller = Controller(game, view)
        return controller

    def test_init(self, controller_instance):
        assert controller_instance.game is not None
        assert controller_instance.view is not None
        assert controller_instance.running is True

