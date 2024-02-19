import pygame
from pygame import *
import time
import random

SIZE = 20


class Food():
    def __init__(self, background):
        self.background = background
        self.food = pygame.image.load("data\\green_apple_1.png")
        self.food = pygame.transform.scale(self.food,(SIZE, SIZE))
        self.location_x = random.randint(0, 63) * SIZE
        self.location_y = random.randint(0, 35) * SIZE

    def draw(self):
        self.background.blit(self.food,(self.location_x, self.location_y))



    def random(self):
        self.location_x = random.randint(0, 63) * SIZE
        self.location_y = random.randint(0, 35) * SIZE



class Snake():
    def __init__(self, background, length):
        self.length =  length
        self.background = background
        self.snake_1 = pygame.image.load("data\\snake_1.jpg")
        self.snake_1 = pygame.transform.scale(self.snake_1,(20, 20))
        self.location_x = [120] * length
        self.location_y = [80] * length
        self.direction = "down"
        

    def draw(self):
         for i in range(self.length):
            self.background.blit(self.snake_1,(self.location_x[i], self.location_y[i]))

    
    
    def move_left(self):
        self.direction = "left"

    def move_right(self):
        self.direction = "right"

    def move_up(self):
        self.direction = "up"


    def move_down(self):
        self.direction = "down"



    def movement(self):

        for f in range(self.length - 1, 0, - 1):
            self.location_x[f] = self.location_x[f - 1]
            self.location_y[f] = self.location_y[f - 1]

        if self.direction == "down":
            self.location_y[0] += SIZE
        if self.direction == "up":
            self.location_y[0] -= SIZE
        if self.direction == "left":
            self.location_x[0] -= SIZE
        if self.direction == "right":
            self.location_x[0] += SIZE

        


    def increment(self):
        self.length += 1
        self.location_x.append(self.location_x[-1])
        self.location_y.append(self.location_y[-1])

            

class Snake_2():
    def __init__(self, background, length):
        self.length =  length
        self.background = background
        self.snake_1 = pygame.image.load("data\\snake_2.jpg")
        self.snake_1 = pygame.transform.scale(self.snake_1,(20, 20))
        self.location_x = [1060] * length
        self.location_y = [80] * length
        self.direction = "down"
        

    def draw(self):
         for i in range(self.length):
            self.background.blit(self.snake_1,(self.location_x[i], self.location_y[i]))

    
    
    def move_left(self):
        self.direction = "left"

    def move_right(self):
        self.direction = "right"

    def move_up(self):
        self.direction = "up"


    def move_down(self):
        self.direction = "down"



    def movement(self):

        for f in range(self.length - 1, 0, - 1):
            self.location_x[f] = self.location_x[f - 1]
            self.location_y[f] = self.location_y[f - 1]

        if self.direction == "down":
            self.location_y[0] += SIZE
        if self.direction == "up":
            self.location_y[0] -= SIZE
        if self.direction == "left":
            self.location_x[0] -= SIZE
        if self.direction == "right":
            self.location_x[0] += SIZE

        


    def increment(self):
        self.length += 1
        self.location_x.append(self.location_x[-1])
        self.location_y.append(self.location_y[-1])





class snake_game():
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1280, 720))
        self.background = pygame.image.load("data\\background.jpg")
        self.surface.blit(self.background,(0, 0))
        self.font = pygame.font.SysFont("arial", 30)


        self.snake_2 = Snake_2(self.surface, 4)
        self.snake_1 = Snake(self.surface, 4)
        self.food = Food(self.surface)
        self.snake_2.draw()
        self.snake_1.draw()
        self.food.draw()
        self.result = "player 1"


    def collision_2(self):
        for i in range(2 ,self.snake_2.length):
            if self.snake_2.location_y[0] == self.snake_2.location_y[i] and self.snake_2.location_x[0] == self.snake_2.location_x[i]:
                self.result = "Player 1"
                raise "Game over"
            if self.snake_2.location_x[0] < 0 or self.snake_2.location_x[0] > 1280 or self.snake_2.location_y[0] < 0 or self.snake_2.location_y[0] > 719:
                self.result = "Player 1"
                raise "Game over"
            

    def collision_1(self):
        for z in range(2 ,self.snake_1.length):
            if self.snake_1.location_y[0] == self.snake_1.location_y[z] and self.snake_1.location_x[0] == self.snake_1.location_x[z]:
                self.result = "Player 2"
                raise "Game over"
            if self.snake_1.location_x[0] < 0 or self.snake_1.location_x[0] > 1280 or self.snake_1.location_y[0] < 0 or self.snake_1.location_y[0] > 719:
                self.result = "Player 2"
                raise "Game over"



    def reset(self):
        self.snake_2 = Snake_2(self.surface, 4)
        self.snake_1 = Snake(self.surface, 4)
        self.food = Food(self.surface)
        self.snake_1.draw()
        self.snake_2.draw()
        self.food.draw()
        


    def eating(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                sound = pygame.mixer.Sound("data\\eating_sound.mp3")
                pygame.mixer.Sound.play(sound)
                return True
            

    def losing(self):
        for a in range(self.snake_1.length):
            if self.snake_1.location_x[a] == self.snake_2.location_x[0] and self.snake_1.location_y[a] == self.snake_2.location_y[0]:
                self.result = "Player 1"
                raise "Game Over"
        for b in range(self.snake_2.length):
            if self.snake_2.location_x[b] == self.snake_1.location_x[0] and self.snake_2.location_y[b] == self.snake_1.location_y[0]:
                self.result = "Player 2"
                raise "Game Over"
            

    def score_1(self):
        score_1 = self.font.render(f"Score: {self.snake_1.length - 4}", True, (0, 0, 255))
        self.surface.blit(score_1, (20, 10))


    def score_2(self):
        score_2 = self.font.render(f"Score: {self.snake_2.length - 4}", True, (255, 20, 147))
        self.surface.blit(score_2, (1150, 10))



    def game_over(self):
        self.surface.fill((171, 171, 171))
        pygame.display.flip()


    def play(self):
        self.snake_2.movement()
        self.snake_1.movement()
        self.surface.blit(self.background, (0, 0))
        self.snake_2.draw()
        self.snake_1.draw()
        self.food.draw()
        self.losing()

        if self.eating(self.snake_1.location_x[0], self.snake_1.location_y[0], self.food.location_x, self.food.location_y):
            self.food.random()
            self.snake_1.increment()
        if self.eating(self.snake_2.location_x[0], self.snake_2.location_y[0], self.food.location_x, self.food.location_y):
            self.food.random()
            self.snake_2.increment()
        self.score_1()
        self.score_2()

        self.collision_2()
        self.collision_1()
        

        
        pygame.display.flip()
        time.sleep(0.1)


    def show_game_over(self):
        self.surface.fill((185, 185, 185))
        if self.result == "Player 1":
            game_over_message = self.font.render(f"{self.result} Wins", True, (0, 0, 255))
            self.surface.blit(game_over_message, (560, 300))
        if self.result == "Player 2":
            game_over_message = self.font.render(f"{self.result} Wins", True, (255, 20, 147))
            self.surface.blit(game_over_message, (560, 300))
        game_over_message_1 = self.font.render(f"Press ""SPACE"" to play again ", True, (255, 255, 255))
        self.surface.blit(game_over_message_1, (500, 340))
        
        pygame.display.flip()
    

    def run(self):
        pause = False
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        pause = False
                        self.reset()
                        
                    if not pause:
                        if event.key == K_a and self.snake_1.direction != "right":
                            self.snake_1.move_left()

                        if event.key == K_d and self.snake_1.direction != "left":
                            self.snake_1.move_right()

                        if event.key == K_w and self.snake_1.direction != "down":
                            self.snake_1.move_up()
                        
                        if event.key == K_s and self.snake_1.direction != "up":
                            self.snake_1.move_down()
                    if not pause:
                        if event.key == K_LEFT and self.snake_2.direction != "right":
                            self.snake_2.move_left()

                        if event.key == K_RIGHT and self.snake_2.direction != "left":
                            self.snake_2.move_right()

                        if event.key == K_UP and self.snake_2.direction != "down":
                            self.snake_2.move_up()
                        
                        if event.key == K_DOWN and self.snake_2.direction != "up":
                            self.snake_2.move_down()
                if event.type == QUIT:
                    running = False

            try:
                if not pause:
                    self.play()
            except:
                self.show_game_over()
                pause = True



if __name__ == "__main__":


    game = snake_game()
    game.run()