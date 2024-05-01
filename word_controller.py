"""
Module for taking player inputs.
"""

import time
import pygame


class Controller:
    """
    Creates the class representing the Controller of the game.
    """
    def __init__(self):
        """
        Initialize the Controller class.
        """
        self.score = 0
        self.time_remaining = 0
        self.game_over = False
        self.won = False
        self.bubbles = []
        self.current_word = ""
        self.pointer = 0
        self.epoch = 0
        self.word_complete = False

    def reset_game(self):
        """
        Resets the time and game over state of the game.

        Args:
            None.
        
        Returns:
            None.
        """
        self.score = 0
        self.time_remaining = 60
        self.epoch = time.time()

        self.game_over = False
        self.won = False

    def next_word(self, new_word, bubbles):
        """
        Helper function that selects new word after previous word has been
        completed.

        Args:
            None.
        
        Returns:
            None.
        """
        self.bubbles = bubbles
        self.current_word = new_word
        self.pointer = 0

        self.word_complete = False

    def update(self, events):
        """
        Called per game loop iteration
        """

        self.get_click(events)
        now = time.time()
        self.time_remaining -= now - self.epoch
        self.epoch = now
        self.check_game_over()

    def get_click(self, events):
        """
        Handle the event of mouse button clicks from the player.

        Args:
            None.

        Returns:
            None.
        """
        mouse_position = None
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = event.pos
                self.handle_click(mouse_position)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.game_over:
                        self.reset_game()
                    else:
                        pygame.display.flip()

        return mouse_position

    def update_score(self):
        """
        Increases the score by 1.

        Args:
            None.

        Returns:
            None.
        """
        self.score += 1

    def handle_click(self, mouse_position):
        """
        Handle a mouse click, updating the game state or view.

        Args:
            None.

        Returns:
            None.
        """
        if self.is_correct_letter(mouse_position):
            self.pointer += 1
            self.update_score()
        else:
            self.time_penalty()

        self.check_word_complete()

    def time_penalty(self):
        """
        Apply a time penalty of 3 seconds to the remaining time.

        Args:
            None.

        Returns:
            None.
        """
        self.time_remaining -= 3

    def is_correct_letter(self, mouse_position):
        """
        Check if the clicked letter is correct.

        Args:
            clicked_letter: a string representing the letter just clicked by 
            the player.

        Returns:
            A boolean that represents True if the clicked letter is correct, 
            False otherwise.
        """
        correct_bubbles = [
            bubble
            for bubble in self.bubbles
            if bubble.letter == self.current_word[self.pointer]
        ]

        for bubble in correct_bubbles:
            correct_letter_position = bubble.pos  # get the letter pos
            distance = (
                (mouse_position[0] - correct_letter_position[0]) ** 2
                + (mouse_position[1] - correct_letter_position[1]) ** 2
            ) ** 0.5
            # distance formula from google
            if distance <= bubble.radius:  # then clicked in circle
                bubble.clicked = True
                return True

        return False

    def check_word_complete(self):
        """
        Checks if the player has completed spelling the target word.

        Args:
            None.
        
        Returns:
            None.
        """
        if self.pointer == len(self.current_word):
            print("complete!")
            self.word_complete = True
            self.score += 1

    def check_game_over(self):
        """
        Check if the game is over due to time running out.

        Args:
            None.

        Returns:
            None.
        """
        if self.time_remaining < 0:
            print("out of time!")
            self.game_over = True
