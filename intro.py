from pygameSetup import *
import menu

FPS = 60

pygame.init()
# clock = pygame.time.Clock()
pygame.mixer.quit()
movie = pygame.movie.Movie('credits/workingintro.MPG')
# screen = pygame.display.set_mode(movie.get_size())

movie_rect = pygame.Rect((0, 0), (640, 384))

# movie.get_size()
movie_screen = pygame.Surface((640, 384)).convert()

movie.set_display(movie_screen, movie_rect)
movie.play()

menu.fillBackground(0, 0, 16, 12)

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            movie.stop()
            playing = False

    # menu.fillBackground(0, 0, 16, 12)

    screen.blit(movie_screen, (192, 192))

    pygame.display.update()
    # clock.tick(FPS)

pygame.quit()