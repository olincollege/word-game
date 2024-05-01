"""
Module for calculations and gameplay.
"""
import random
import pygame

from word_controller import Controller
from word_view import Bubble, View


class Game:
    """
    Creates class representing the model of MVC for the game.
    """

    def __init__(self, controller, view):
        """
        Initialize the Game class.
        """
        self.clock = pygame.time.Clock()
        self.word_list = []
        self.letters = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]
        self.current_word = ""
        self.bubbles: list[Bubble] = []
        self.controller: Controller = controller
        self.view: View = view

    def load_word_list(self):
        """
        Take in word list and read each line of list.

        Args:
            None.

        Returns:
            None.
        """
        new_list = []
        with open("word_list.txt", encoding="utf-8") as file:
            reader = file.readlines()

        for line in reader:
            new_list.append(line[:-1])
        self.word_list = new_list

    def new_word(self):
        """
        Helper function for main loop that chooses a new word when previous
        word is completed.

        Args:
            None.

        Returns:
            None.
        """
        self.generate_word()
        self.generate_letters()

        self.controller.next_word(self.current_word, self.bubbles)
        self.controller.current_word = self.current_word

    def new_game(self):
        """
        Creates first run of the game.

        Args:
            None.

        Returns:
            None.
        """
        self.view.draw_intro()
        self.controller.reset_game()
        self.load_word_list()
        self.new_word()

    def generate_word(self):
        """
        Generates a new word for the game by randomly selecting a word from
        word list.

        Args:
            None.

        Returns:
            A string that represents the newly generated word.
        """
        self.current_word = random.choice(self.word_list)
        self.controller.current_word = self.current_word

        self.letters = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]  # reset when generating new word

        return self.current_word

    def generate_letters(self):
        """
        Generates bubbles of letters, including all of the correct letters to
        spell the given word and additional incorrect letters.

        Args:
            None.

        Returns:
            None.
        """
        self.bubbles.clear()
        new_bubbles = []

        for letter in self.current_word:
            new_bubbles.append(letter)
            try:
                self.letters.remove(letter)
            except ValueError:
                print("Invalid")

        for i in range(7):
            random_letter = random.choice(self.letters)
            self.letters.remove(random_letter)
            new_bubbles.append(random_letter)

        random.shuffle(new_bubbles)
        self.bubbles = [
            Bubble(i, letter) for i, letter in enumerate(new_bubbles)
        ]
        return self.bubbles

    def try_again(self):
        """
        Resets previous game states for future runs after game over.
        """
        self.current_word = ""
        self.bubbles: list[Bubble] = []
        self.new_word()

    def update(self, events):
        """
        Called every iteration of the game loop and updates game state
        """
        if self.controller.game_over:
            # show game over screen
            self.try_again()
            self.view.draw_game_over()
        elif self.controller.word_complete:
            self.new_word()
        else:
            self.view.draw_board(
                self.current_word,
                self.bubbles,
                self.controller.score,
                self.controller.time_remaining,
            )
        self.controller.update(events)
