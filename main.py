import pygame

from word_game import Game
from word_view import View
from word_controller import Controller

def main():
    """
    Run main loop when gameplay.

    Args:
        None.

    Returns:
        None.
    """
    game_controller = Controller()
    game_view = View()
    game_model = Game(game_controller, game_view)
    
    pygame.init()

    running = True

    in_game = False

    while running:
        if not in_game:
            game_model.new_game()
            in_game = True

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                running = False

        game_model.update(events)


if __name__ == "__main__":
    main()
