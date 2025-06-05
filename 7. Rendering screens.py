    def draw(self):
        if self.game_state == "menu":
            self.screen.blit(self.menu_bg, (0, 0))
            self.draw_menu()
        elif self.game_state == "game":
            self.screen.blit(self.game_bg, (0, 0))
            self.draw_game()
        elif self.game_state == "game_over":
            self.screen.blit(self.game_over_bg, (0, 0))
            self.draw_game_over()
        elif self.game_state == "victory":
            self.screen.blit(self.victory_bg, (0, 0))
            self.draw_victory()
        pygame.display.flip()

    def draw_menu(self):
        title = self.font_large.render("Ковбой и похищенная принцесса", True, WHITE)
        self.screen.blit(title, (self.width//2 - title.get_width()//2, 100))
        
        subtitle = self.font_medium.render("Выберите разрешение экрана:", True, WHITE)
        self.screen.blit(subtitle, (self.width//2 - subtitle.get_width()//2, 200))
        
        for i, option in enumerate(self.resolution_options):
            color = GREEN if i == self.selected_resolution else WHITE
            text = self.font_medium.render(option["label"], True, color)
            self.screen.blit(text, (self.width//2 - text.get_width()//2, 250 + i*40))
        
        hint = self.font_small.render("Стрелки ВВЕРХ/ВНИЗ - выбор, ENTER - старт", True, WHITE)
        self.screen.blit(hint, (self.width//2 - hint.get_width()//2, self.height-50))

    def draw_game(self):
        # Рисуем ковбоя
        self.screen.blit(self.cowboy.img, (self.cowboy.x, self.cowboy.y))
        
        # Рисуем пули
        for bullet in self.bullets:
            self.screen.blit(bullet.img, (bullet.x, bullet.y))
        
        # Рисуем врагов
        for enemy in self.enemies:
            self.screen.blit(enemy.img, (enemy.x, enemy.y))
        
        # Рисуем UI
        score_text = self.font_medium.render(f"Очки: {self.score}/{self.victory_score}", True, WHITE)
        self.screen.blit(score_text, (20, 20))
        
        hits_text = self.font_medium.render(f"Ошибки: {self.princess_hits}/{self.max_princess_hits}", True, WHITE)
        self.screen.blit(hits_text, (20, 60))

    def draw_game_over(self):
        title = self.font_large.render("GAME OVER", True, WHITE)
        self.screen.blit(title, (self.width//2 - title.get_width()//2, self.height//2 - 100))
        
        score_text = self.font_medium.render(f"Финальный счет: {self.score}", True, WHITE)
        self.screen.blit(score_text, (self.width//2 - score_text.get_width()//2, self.height//2))
        
        hint = self.font_small.render("ENTER - меню, ESC - выход", True, WHITE)
        self.screen.blit(hint, (self.width//2 - hint.get_width()//2, self.height//2 + 100))

    def draw_victory(self):
        title = self.font_large.render("ПОБЕДА!", True, GOLD)
        self.screen.blit(title, (self.width//2 - title.get_width()//2, self.height//2 - 150))
        
        subtitle = self.font_medium.render("Вы спасли принцессу!", True, WHITE)
        self.screen.blit(subtitle, (self.width//2 - subtitle.get_width()//2, self.height//2 - 50))
        
        score_text = self.font_medium.render(f"Ваш счет: {self.score}", True, WHITE)
        self.screen.blit(score_text, (self.width//2 - score_text.get_width()//2, self.height//2 + 20))
        
        hint = self.font_small.render("ENTER - меню, ESC - выход", True, WHITE)
        self.screen.blit(hint, (self.width//2 - hint.get_width()//2, self.height//2 + 100))