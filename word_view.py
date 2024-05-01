"""
Module for game's visualization
"""

import pygame

class View:
    """
    Creates class representing the view of the game state.
    """
    def __init__(self):
        """
        Initialize the View class.
        """
        pygame.init()

        self.screen_width = 700
        self.screen_height = 500
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        pygame.display.set_caption("Word Bubble Game")
        self.clock = pygame.time.Clock()
        self.big_font = pygame.font.Font(None, 60)
        self.font = pygame.font.Font(None, 48)
        self.medium_font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 28)
        self.color = (240, 84, 89)
    
    def draw_intro(self):
        self.screen.fill((255 , 255, 255))
        text = self.medium_font.render(
                    "Enter to Start", 
                    True, (0, 0, 0))
        self.screen.blit(text, ((self.screen_width / 2) - 150,
                                self.screen_height / 1.8))

    def draw_game_over(self):
        """
        Runs the screen when player hits game over state.

        Args:
            None.

        Returns:
            None.
        """
        self.screen.fill((255, 255, 255))
        text = self.medium_font.render(
            "Hit Enter to Restart", 
            True, (0, 0, 0))
        self.screen.blit(text, ((self.screen_width / 2) - 150,
                                self.screen_height / 1.8))
        text_2 = self.small_font.render(
            "Credits to Xethron on Github for the word list!", 
            True, (0, 0, 0))
        self.screen.blit(text_2, (
            (self.screen_width / 2) - 200,
            (self.screen_height / 2) + 100))
        text_3 = self.big_font.render(
            "Game Over!",
            True, (0, 0, 0))
        self.screen.blit(text_3, (
            (self.screen_width / 2) - 170,
            (self.screen_height /2) - 150))
        pygame.display.flip()


    def draw_board(self, target_word, letter_bubbles, score, time_remaining):
        """
        Draws the game board on the screen.

        This function clears the screen, draws the target word at the top, 
        and the letter bubbles below it. After drawing everything, it updates 
        the display to show the changes.

        Args:
            target_word: a string representing the word that the player needs 
                         to guess.
            letter_bubbles: a list of letter bubbles to display on the screen. 

        Returns:
            None
        """
        self.screen.fill((255, 255, 255))  
        self.draw_target_word(target_word)
        self.draw_letter_bubbles(letter_bubbles)
        self.draw_score(score)
        self.draw_time_remaining(time_remaining)
        pygame.display.flip()

    def draw_score(self, score):
        """
        Draws the player's score that is displayed during the game.

        Args:
            score: an integer representing the player's current score.
        
        Returns:
            None.
        """
        text = self.font.render(str(score), True, (0, 0, 0))
        self.screen.blit(text,
                         (self.screen_width - (text.get_width() + 10), 
                          self.screen_height - (text.get_height() + 10)))
        text_2 = self.font.render("Score: ", True, (0, 0, 0))
        self.screen.blit(text_2, (self.screen_width - (text_2.get_width() + text.get_width() + 10),
                         self.screen_height - (text.get_height() + 10)))

    def draw_time_remaining(self, time_remaining):
        """
        Draws the remaining time of the current game.

        Args:
            time_remaining: a float representing the amound of time remaining
            on the player's timer for the current game run.
        
        Returns:
            None.
        """
        text = self.font.render(str(round(time_remaining)), True, (0, 0, 0))
        self.screen.blit(text, (self.screen_width - (text.get_width() + 50) , 50))

    def draw_target_word(self, target_word):
        """
        Draws the target word at the top of the screen with a specific font 

        Args:
            target_word: a string representing the word that the player needs 
            to spell with the bubbles.

        Returns:
            None
        """
        text = self.font.render("Target Word: " + target_word, True, (0, 0, 0))
        self.screen.blit(text, (20, 20))

    def draw_letter_bubbles(self, bubbles):
        """
        Draws letter bubbles on the screen, from a list of letter bubbles that 
        are shown as a tuple.

        Args:
            bubbles: a list of letter bubbles, which is a circle with a given 
            letter.

        Returns:
            None
        """
        for bubble in bubbles:
            if not bubble.clicked:
                pygame.draw.circle(self.screen, self.color, 
                                   bubble.pos, bubble.radius)
                text = self.font.render(bubble.letter, True, (0, 0, 0))
                self.screen.blit(text, (bubble.x - 9, bubble.y - 9))

class Bubble():
    """
    Class respresenting the circle with proper letters that players click on. 
    """
    def __init__(self, index, letter):
        """
        Initializes the Bubble class.
        """
        x_index = index % 5
        self.x = (x_index * 100) + 100
        y_index = int(index / 5)
        self.y = (y_index * 100) + 100
        self.pos = (self.x, self.y)
        self.radius = 30
        self.letter = letter

        self.clicked = False
