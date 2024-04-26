"""
Module for game's visualization
"""
import sys
import random
import pygame

class WordGameView:
    def __init__(self, screen_width, screen_height, word_list):
        """
        Initialize the View class.
        """
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Word Bubble Game")
        self.clock = pygame.time.Clock()
        self.word_list = word_list
        self.font = pygame.font.Font(None, 36)
        self.bubble_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  

    def draw_board(self, target_word, letter_bubbles):
        """
        Draws the game board on the screen.

        This function clears the screen, draws the target word at the top, 
        and the letter bubbles below it. After drawing everything, it updates 
        the display to show the changes.

        Args:
            - target_word (str): The word that the player needs to guess.
            - letter_bubbles (list): A list of letter bubbles to display on the screen. 
            Each letter bubble is represented as a tuple containing the letter and its position.

        Returns:
            None
        """
        self.screen.fill((255, 255, 255))  
        self.draw_target_word(target_word)
        self.draw_letter_bubbles(letter_bubbles)
        pygame.display.flip()

    def draw_target_word(self, target_word):
        """
        Draws the target word at the top of the screen with a specific font 

        Args:
            - target_word (str): The word that the player needs to guess.

        Returns:
            None
        """
        text = self.font.render("Target Word: " + target_word, True, (0, 0, 0))
        self.screen.blit(text, (20, 20))

    def draw_letter_bubbles(self, letter_bubbles):
        """
        Draws letter bubbles on the screen, from a list of letter bubbles that are shown as a tuple.

        Args:
            - letter_bubbles (list): A list of letter bubbles to draw.
            Each letter bubble is represented as a tuple containing the position (x, y) 
            and the radius of the bubble.

        Returns:
            None
        """
        for bubble in letter_bubbles:
            pygame.draw.circle(self.screen, self.bubble_colors[random.randint(0, 2)], bubble[0], bubble[1])

    def update_display(self):
        """
        Updates the display to show any changes made to the screen.

        Args:
            None

        Returns:
            None
        """
        pygame.display.flip()

    def handle_events(self):
        """
        Checks for events in event queue and handles events such as quitting the game.

        Args:
            None

        Returns:
            None
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def get_click_position(self):
        """
        Get the current position of the mouse cursor.

        Args:
            None

        Returns:
            tuple: A tuple containing the x and y coordinates of the mouse cursor.
           The first element represents the x-coordinate, and the second
           element represents the y-coordinate.
        """
        mouse_pos = pygame.mouse.get_pos()
        return mouse_pos

    def close(self):
        """
        Closes the Pygame application.

        Args:
            None

        Returns:
            None
        """
        pygame.quit()