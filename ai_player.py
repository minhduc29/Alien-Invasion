import pygame
from alien_invasion import AlienInvasion

class AIPlayer:
    def __init__(self, ai_game):
        """Automatic player for Alien Invasion"""
        self.ai_game = ai_game

    def run_game(self):
        """Replace the original run_game()"""
        self.ai_game.stats.game_active = True
        pygame.mouse.set_visible(False)

        while True:
            self.ai_game._check_events()
            self._implement_strategy()

            if self.ai_game.stats.game_active:
                self.ai_game.ship.update()
                self.ai_game._update_bullets()
                self.ai_game._update_aliens()

            self.ai_game._update_screen()

    def _implement_strategy(self):
        """Implement an automated strategy for AI player"""
        self._sweep_right_left()
        self.ai_game._fire_bullet()

    def _sweep_right_left(self):
        """Move the ship right and left continuously"""
        ship = self.ai_game.ship
        screen_rect = self.ai_game.screen.get_rect()

        if not ship.moving_right and not ship.moving_left:
            ship.moving_right = True
        elif ship.moving_right and ship.rect.right > screen_rect.right - 10:
            ship.moving_right = False
            ship.moving_left = True
        elif ship.moving_left and ship.rect.left < 10:
            ship.moving_left = False
            ship.moving_right = True

if __name__ == '__main__':
    ai_game = AlienInvasion()
    ai_player = AIPlayer(ai_game)
    ai_player.run_game()