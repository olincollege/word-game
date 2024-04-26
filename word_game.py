"""
Module for calculations and gameplay.
"""
import random
import time
import sys
import pygame

class Game:
    def __init__(self):
        """
        Initialize the Game class.
        """
        self.SCREEN_WIDTH = 300
        self.SCREEN_HEIGHT = 150
        self.time_remaining = 60
        self.clock = pygame.time.Clock()
        self.word_list = ["apple", "banana", "cat"]
        self.letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                        "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                        "w", "x", "y", "z"]
        self.current_word = ""
        self.bubbles = []
        self.score = 0

        #added so we can check each letter while game is going
        self.pointer = 0

    def generate_word(self):
        """
        Selects a word from the word list as the given word that the player
        has to spell.

        Args:
            self:
        
        Returns:
            The selected word.

        """
        self.current_word = random.choice(self.word_list)
        self.pointer = 0

        self.letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                        "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                        "w", "x", "y", "z"] #reset when generating new word

        return self.current_word

    def generate_letters(self):
        """
        Generates bubbles of letters, including all of the correct letters to 
        spell the given word and additional incorrect letters

        Args:
            self:
        
        Returns:
            None.
        """
        self.bubbles.clear()

        for letter in self.current_word:
            if letter in self.bubbles:
                continue
            else:
                self.bubbles.append(letter)
                self.letters.remove(letter)

        for i in range(3):
            random_letter = random.choice(self.letters)
            self.letters.remove(random_letter)
            self.bubbles.append(random_letter)

        return self.bubbles

    def countdown(self):
        """
        Runs timer for the duration of the game.

        Args:
            self:
        
        Returns:
            None.
        """
        while self.time_remaining > 0:
            time.sleep(1)
            self.time_remaining -= 1
        print("time up")

        def is_correct_letter(self, clicked_letter):
            """
            Check if the clicked letter is correct.

            Args:
                clicked_letter (str): The letter just clicked by the player.

            Returns:
                bool: True if the clicked letter is correct, False otherwise.
            """
            if 0 <= self.pointer < len(self.current_word): #within range
                current_letter = self.current_word[self.pointer]
                self.pointer += 1 #update if found
                return clicked_letter == current_letter
            else:
                return False

    def update_score(self):
        self.score += 1

    def time_penalty(self):
        self.time_remaining -= 3
        
    def game_over(self):
        if self.time_remaining == 0:
            print("out of time!")
            background = pygame.image.load()

    def quit_game():
        """
        Exits the game.

        Args: 
            None.

        Returns:
            None.
        """
        pygame.quit()
        sys.exit(0)


#start button
#credit inspiration (looks, concept)
#credit word list