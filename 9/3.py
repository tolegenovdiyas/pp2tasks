import pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
class Ball:
    def __init__(self, radius, color, initial_position):
        self.radius = radius
        self.color = color
        self.position = initial_position

    def move(self, dx, dy):
        # Check horizontal boundaries
        if self.position[0] + dx >= self.radius and self.position[0] + dx <= SCREEN_WIDTH - self.radius:
            self.position[0] += dx
        # Check vertical boundaries
        if self.position[1] + dy >= self.radius and self.position[1] + dy <= SCREEN_HEIGHT - self.radius:
            self.position[1] += dy

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)
ball = Ball(25, (255, 0, 0), [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2])  # Red ball
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moving Ball")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball.move(0, -20)
            elif event.key == pygame.K_DOWN:
                ball.move(0, 20)
            elif event.key == pygame.K_LEFT:
                ball.move(-20, 0)
            elif event.key == pygame.K_RIGHT:
                ball.move(20, 0)
    screen.fill((255, 255, 255))
    ball.draw(screen)
    pygame.display.flip()
    pygame.time.delay(100)
pygame.quit()
