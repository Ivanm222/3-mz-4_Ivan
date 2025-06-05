    def load_images(self):
        """Загрузка изображений с обработкой прозрачности"""
        if not os.path.exists('images'):
            os.makedirs('images')

        def load_transparent_image(name, size, default_color):
            try:
                path = os.path.join('images', name)
                surface = pygame.image.load(path).convert_alpha()
                temp_surface = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
                temp_surface.blit(surface, (0, 0))
                return pygame.transform.smoothscale(temp_surface, size)
            except:
                surf = pygame.Surface(size, pygame.SRCALPHA)
                surf.fill(default_color)
                return surf

        # Загрузка спрайтов
        self.cowboy_img = load_transparent_image('cowboy.png', self.COWBOY_SIZE, BLUE)
        self.witch_img1 = load_transparent_image('witch1.png', self.WITCH_SIZE, RED)
        self.witch_img2 = load_transparent_image('witch2.png', self.WITCH_SIZE, (150, 0, 0))
        self.princess_img = load_transparent_image('princess.png', self.PRINCESS_SIZE, PINK)
        self.bullet_img = load_transparent_image('bullet.png', self.BULLET_SIZE, YELLOW)
        
        # Загрузка фонов
        def load_background(name, size, default_color):
            try:
                path = os.path.join('images', name)
                img = pygame.image.load(path).convert()
                return pygame.transform.smoothscale(img, size)
            except:
                surf = pygame.Surface(size)
                surf.fill(default_color)
                return surf
                
        self.menu_bg = load_background('menu_bg.jpg', (self.width, self.height), DARK_BLUE)
        self.game_bg = load_background('forest_bg.jpg', (self.width, self.height), DARK_GREEN)
        self.game_over_bg = load_background('game_over_bg.jpg', (self.width, self.height), DARK_RED)
        self.victory_bg = pygame.Surface((self.width, self.height))
        self.victory_bg.fill((50, 50, 150))

    def reset_game(self):
        """Сброс состояния игры"""
        self.score = 0
        self.princess_hits = 0
        self.bullets = []
        self.enemies = []
        cowboy_x = self.width // 2 - self.cowboy_img.get_width() // 2
        cowboy_y = self.height - self.cowboy_img.get_height() - 20
        self.cowboy = Cowboy(cowboy_x, cowboy_y, self.cowboy_img)