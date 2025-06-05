    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            
            if self.game_state == "menu":
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.selected_resolution = (self.selected_resolution - 1) % len(self.resolution_options)
                    elif event.key == K_DOWN:
                        self.selected_resolution = (self.selected_resolution + 1) % len(self.resolution_options)
                    elif event.key == K_RETURN:
                        res = self.resolution_options[self.selected_resolution]
                        self.width = res["width"]
                        self.height = res["height"]
                        self.screen = pygame.display.set_mode((self.width, self.height))
                        self.load_images()
                        self.game_state = "game"
                        self.reset_game()
            
            elif self.game_state == "game":
                if event.type == KEYDOWN and event.key == K_SPACE:
                    self.bullets.append(Bullet(
                        self.cowboy.x + self.cowboy.width // 2 - self.bullet_img.get_width() // 2,
                        self.cowboy.y,
                        self.bullet_img
                    ))
            
            elif self.game_state in ["game_over", "victory"]:
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        self.game_state = "menu"
                    elif event.key == K_ESCAPE:
                        self.running = False