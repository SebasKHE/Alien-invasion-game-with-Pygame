class GameStats():
    """Track statistics for Alien invasion"""

    def __init__(self, ai_settings):
        """Initialize statitstics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        #high score should never be reset
        self.high_score = 0

    
    def reset_stats(self):
        """Initialize sattistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
