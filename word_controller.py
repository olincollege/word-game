"""
Module for taking player inputs.
"""

import pygame
from word_game import Game
from word_view import WordGameView


class Controller:
    def __init__(self, game, view):
        """
        Initialize the Controller class.
        """
        self.game = game
        self.view = view
        self.running = True

    def get_click(self):
        """
        Handle the event of mouse button clicks from the player.

        Args:
            None.

        Returns:
            None.
        """
        mouse_position = None 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = event.pos
                self.handle_click(mouse_position)
            elif event.type == pygame.KEYDOWN:
                key = event.key
                self.handle_key_input(key) 
        return
    
    def handle_click(self, mouse_position):
        """
        Handle a mouse click, updating the game state or view.
        
        Args:
            None.
        
        Returns:
            None.
        """
        if self.is_correct_letter(mouse_position):
            self.game.pointer += 1
            self.game.update_score()
        else:
            self.game.time_penalty()
        return

    def is_correct_letter(self, mouse_position):
        """
        Check if the clicked letter is correct.

        Args:
            clicked_letter (str): The letter just clicked by the player.

        Returns:
            A boolean that represents True if the clicked letter is correct, False otherwise.
        """
        correct_letter_position = self.view.get_letter_position(self.game.current_word[self.game.pointer]) #get the letter pos
        radius = self.view.get_bubble_radius()
        distance = ((mouse_position[0] - correct_letter_position[0]) ** 2 
            + (mouse_position[1] - correct_letter_position[1]) ** 2) ** 0.5
        #distance formula from google
        if distance <= radius: #then clicked in circle
            return True
        else:
            return False

    def handle_key_input(self, key):
        """
        Handle keyboard events by takinf in key inputs.
    
        Args:
            key (int): The key code corresponding to the pressed key.

        Returns:
            None.
        """
        if key == pygame.K_q:
            self.game.quit_game()
        elif key == pygame.K_ESCAPE:
            self.game.pause() #not implemented yet
 
    def restart(self):
        """
        Restart the game.

        Args:
            None.

        Returns:
            None.
        """
        self.game.reset()  
        self.view.update()  