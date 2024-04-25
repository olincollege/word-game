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
        self.time = 60
        self.clock = pygame.time.Clock()
        self.word_list = ["apple", "banana", "cat"]
        self.letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                        "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                        "w", "x", "y", "z"]
        self.current_word = ""
        self.bubbles = []
        self.score = 0

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

        letters = [*self.current_word]

        for letters in self.current_word:
            self.bubbles.append(letters)

        for i in range(3):
            random_letter = random.choice(self.letters)
            self.bubbles.append(random_letter)

        return self.bubbles

    def countdown(self.time):
        """
        Runs timer for the duration of the game.

        Args:
            self:
        
        Returns:
            None.
        """
        seconds = self.time

        while seconds >= 0:
            print(seconds)
            time.sleep(1)
            seconds -= 1
            
    def is_correct(self):
        if 
        #if correct bubble
        #if incorrect bubble
        #if click not on bubble
        pass

    def update_score(self):
        action = is_correct()

        if action is True:
            self.score += len(self.current_word)

    def time_penalty(self):
        action = is_correct()

        if action is False:
            self.time -= 3
        else:
            pass

    def game_over(self):
        if self.time == 0:
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
