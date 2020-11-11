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

        self.fleet_size = len(self.ai_game.aliens)

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
        if len(self.ai_game.aliens) >= 1/4 * self.fleet_size:
            self._sweep_right_left()
        else:
            self._move_with_target()

        self.ai_game._fire_bullet()

    def _get_target_alien(self):
        """Get a specific alien to target"""
        target_alien = self.ai_game.aliens.sprites()[0]
        for alien in self.ai_game.aliens.sprites():
            if alien.rect.y > target_alien.rect.y:
                target_alien = alien
            elif alien.rect.x > target_alien.rect.x:
                target_alien = alien

        return target_alien

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

    def _move_with_target(self):
        """Move the ship according to targeted alien"""
        target_alien = self._get_target_alien()

        ship = self.ai_game.ship
        if self.ai_game.settings.fleet_direction == 1 and ship.rect.x < target_alien.rect.x + 50:
            ship.moving_right = True
            ship.moving_left = False
        elif self.ai_game.settings.fleet_direction == -1 and ship.rect.x > target_alien.rect.x - 50:
            ship.moving_right = False
            ship.moving_left = True

if __name__ == '__main__':
    ai_game = AlienInvasion()
    ai_player = AIPlayer(ai_game)
    ai_player.run_game()