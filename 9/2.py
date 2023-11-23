import pygame
pygame.init()
pygame.mixer.init()
song_list = ['Ascension.mp3', 'Edward Maya & Vika Jigulina - Stereo Love.mp3']
current_song = 0
is_paused = False
screen = pygame.display.set_mode((320, 320))
pygame.display.set_caption("Music Player")
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GRAY = (100, 100, 100)
def draw_button(text, position, color):
    font = pygame.font.SysFont(None, 36)
    text_render = font.render(text, True, COLOR_BLACK)
    text_rect = text_render.get_rect(center=(position[0] + 50, position[1] + 25))
    pygame.draw.rect(screen, color, (*position, 100, 50))
    screen.blit(text_render, text_rect)
pygame.mixer.music.load(song_list[current_song])
pygame.mixer.music.play(-1)
game_running = True
while game_running:
    screen.fill(COLOR_BLACK)
    draw_button('Play', (30, 30), COLOR_GRAY)
    draw_button('Stop', (30, 90), COLOR_GRAY)
    draw_button('Next', (30, 150), COLOR_GRAY)
    draw_button('Prev', (30, 210), COLOR_GRAY)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if 30 <= mouse[0] <= 130 and 30 <= mouse[1] <= 80:  # Play button
                if is_paused:
                    pygame.mixer.music.unpause()
                    is_paused = False
                else:
                    pygame.mixer.music.play()
            elif 30 <= mouse[0] <= 130 and 90 <= mouse[1] <= 140:  # Stop button
                pygame.mixer.music.stop()
                is_paused = False
            elif 30 <= mouse[0] <= 130 and 150 <= mouse[1] <= 200:  # Next button
                current_song = (current_song + 1) % len(song_list)
                pygame.mixer.music.load(song_list[current_song])
                pygame.mixer.music.play(-1)
            elif 30 <= mouse[0] <= 130 and 210 <= mouse[1] <= 260:  # Previous button
                current_song = (current_song - 1) % len(song_list)
                pygame.mixer.music.load(song_list[current_song])
                pygame.mixer.music.play(-1)

    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()
