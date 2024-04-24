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

class WordGameView:
    """
    A visual representation of the word game.

    Attributes:
        model: a WordGameModel instance representing the game state.
    """

    def __init__(self, model):
        self.model = model
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Word Game')
        self.font = pygame.font.Font(None, 36)
        self.clock = pygame.time.Clock()

    def draw(self):
        self.screen.fill((255, 255, 255))
        
        # Display the target word
        target_word_text = self.font.render("Target Word: " + self.model.current_word, True, (0, 0, 0))
        self.screen.blit(target_word_text, (50, 50))
        
        # Display the letter bubbles
        for bubble in self.model.letter_bubbles:
            pygame.draw.circle(self.screen, (0, 0, 255), (bubble.x, bubble.y), bubble.radius)
            letter_text = self.font.render(bubble.letter, True, (255, 255, 255))
            self.screen.blit(letter_text, (bubble.x - bubble.radius // 2, bubble.y - bubble.radius // 2))
        
        pygame.display.update()

# Example usage:
# Assuming WordGameModel is defined with appropriate attributes
# model = WordGameModel()
# view = WordGameView(model)

# Main game loop
# while True:
#     view.draw()
#     pygame.display.update()
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()