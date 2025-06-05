    def run(self):
        """Главный игровой цикл"""
        while self.running:
            self.clock.tick(FPS)
            self.handle_events()
            self.update()
            self.draw()
        pygame.quit()
        sys.exit()