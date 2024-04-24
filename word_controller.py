"""
Module for taking player inputs.
"""

import pygame


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.running = True

    def get_click():
        """Handle mouse events, like button clicks."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                # Process mouse click here
                # Example: self.view.handle_mouse_click(mouse_pos)

    def handle_click(self, mouse_pos):
        """Handle a mouse click, updating the game state or view."""
        letter = self.view.get_letter_at_position(
            mouse_pos
        )  # Determine if a letter was clicked
        if letter:
            if self.model.is_correct_letter(letter):
                self.model.add_letter(
                    letter
                )  # Add the letter to the game model
                self.model.set_correct_letter()  # Generate a new correct letter
            else:
                self.model.penalize()  # Penalize for incorrect click

    def get_key_input(self):
        """Handle keyboard events, like key presses."""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.running = False  # Quit the game
                elif event.key == pygame.K_ESCAPE:
                    # Handle pause or other logic
                    pass

    def restart():
        """Reset the game to its initial state."""
        self.model.reset()  # Reset the game logic
        self.view.update()  # Update the view


# specify: mouse controller and keyboard controller
# need keyboard controller too even though gameplay only uses mouse, (ie. q for quit, esc for pause...)
