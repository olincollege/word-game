"""
Module for game's visualization
"""
#class Board:
#    def __init__():
        #board
        #display time
        #display target word
        #display letter bubbles
#        pass

import pygame
import sys
import random

class WordGameView:
    def __init__(self, screen_width, screen_height, word_list):
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
        self.screen.fill((255, 255, 255))  
        self.draw_target_word(target_word)
        self.draw_letter_bubbles(letter_bubbles)
        pygame.display.flip()

    def draw_target_word(self, target_word):
        text = self.font.render("Target Word: " + target_word, True, (0, 0, 0))
        self.screen.blit(text, (20, 20))

    def draw_letter_bubbles(self, letter_bubbles):
        for bubble in letter_bubbles:
            pygame.draw.circle(self.screen, self.bubble_colors[random.randint(0, 2)], bubble[0], bubble[1])

    def update_display(self):
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def get_click_position(self):
        mouse_pos = pygame.mouse.get_pos()
        return mouse_pos

    def close(self):
        pygame.quit()