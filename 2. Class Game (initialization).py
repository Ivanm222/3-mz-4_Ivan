class Game:
    def __init__(self):
        self.width = DEFAULT_WIDTH
        self.height = DEFAULT_HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Ковбой и похищенная принцесса')
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_state = "menu"
        self.score = 0
        self.princess_hits = 0
        self.max_princess_hits = 3
        self.victory_score = 350
        
        # Размеры персонажей
        self.COWBOY_SIZE = (75, 115)
        self.WITCH_SIZE = (50, 75)
        self.PRINCESS_SIZE = (45, 70)
        self.BULLET_SIZE = (8, 20)
        
        self.load_images()
        self.reset_game()
        
        # Таймеры
        self.enemy_spawn_timer = 0
        self.enemy_spawn_interval = 2500
        
        # Шрифты
        self.font_large = pygame.font.SysFont('Arial', 50, bold=True)
        self.font_medium = pygame.font.SysFont('Arial', 30)
        self.font_small = pygame.font.SysFont('Arial', 20)
        
        # Настройки меню
        self.resolution_options = [
            {"width": 800, "height": 600, "label": "800x600"},
            {"width": 1024, "height": 768, "label": "1024x768"},
            {"width": 1280, "height": 720, "label": "1280x720"},
            {"width": 1920, "height": 1080, "label": "1920x1080"}
        ]
        self.selected_resolution = 0