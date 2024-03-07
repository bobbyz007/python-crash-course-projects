class Settings:
    """A class to store all settings for Alien Invasion"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_limit = 3

        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 20

        # aliens settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_incr = 1

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        self.ship_speed = 5
        self.bullet_speed = 4
        self.alien_speed = 1
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # how many points a player gets each time they shoot down an alien
        self.alien_points = 10;

    def increase_speed(self):
        self.ship_speed += self.speedup_incr
        self.bullet_speed += self.speedup_incr
        self.alien_speed += self.speedup_incr
        self.alien_points = int(self.alien_points * self.score_scale)
