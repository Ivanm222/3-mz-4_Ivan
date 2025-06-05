    def update(self):
        if self.game_state == "game":
            keys = pygame.key.get_pressed()
            if keys[K_LEFT]:
                self.cowboy.x = max(0, self.cowboy.x - self.cowboy.speed)
            if keys[K_RIGHT]:
                self.cowboy.x = min(self.width - self.cowboy.width, self.cowboy.x + self.cowboy.speed)
            
            # Спавн врагов
            current_time = pygame.time.get_ticks()
            if current_time - self.enemy_spawn_timer > self.enemy_spawn_interval:
                self.enemy_spawn_timer = current_time
                self.spawn_enemy()
            
            # Обновление пуль
            for bullet in self.bullets[:]:
                bullet.y -= bullet.speed
                if bullet.y < 0:
                    self.bullets.remove(bullet)
            
            # Обновление врагов
            for enemy in self.enemies[:]:
                enemy.y += enemy.speed
                if enemy.y > self.height:
                    self.enemies.remove(enemy)
            
            # Проверка столкновений
            self.check_collisions()
            
            # Проверка условий завершения
            if self.princess_hits >= self.max_princess_hits:
                self.game_state = "game_over"
            elif self.score >= self.victory_score:
                self.game_state = "victory"

    def spawn_enemy(self):
        x = random.randint(0, self.width - self.WITCH_SIZE[0])
        y = -self.WITCH_SIZE[1]
        
        if random.random() < 0.888:  # 8/9 chance
            witch_img = random.choice([img for img in [self.witch_img1, self.witch_img2] if img is not None])
            if witch_img is None:
                witch_img = pygame.Surface(self.WITCH_SIZE, pygame.SRCALPHA)
                witch_img.fill(RED)
            enemy = Enemy(x, y, witch_img, "witch", 10)
        else:
            enemy = Enemy(x, y, self.princess_img, "princess", -100)
        
        self.enemies.append(enemy)

    def check_collisions(self):
        for bullet in self.bullets[:]:
            for enemy in self.enemies[:]:
                if (bullet.x < enemy.x + enemy.width and
                    bullet.x + bullet.width > enemy.x and
                    bullet.y < enemy.y + enemy.height and
                    bullet.y + bullet.height > enemy.y):
                    
                    if enemy.type == "witch":
                        self.score += enemy.points
                    else:
                        self.score += enemy.points
                        self.princess_hits += 1
                    
                    if bullet in self.bullets:
                        self.bullets.remove(bullet)
                    if enemy in self.enemies:
                        self.enemies.remove(enemy)
                    break