# Imports and Setup Pygame ----------------------------------------------------
import pygame , sys
pygame.init()
pygame.mixer.init()


# Setup Window ----------------------------------------------------
pygame.display.set_icon(pygame.image.load("assets/images/icon.png"))
pygame.display.set_caption('Az elzárt fájl DEMO')
screen = pygame.display.set_mode((1200, 720))
pygame.display.flip()


# Other ------------------------------------------------------------
clock = pygame.time.Clock()


# Import assets ----------------------------------------------------
# Images - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
background_surface = pygame.image.load('assets/images/background.png')
trash_surface = pygame.image.load('assets/images/trash.png')
txt1_surface = pygame.image.load('assets/images/txt1.png')
storytxt_surface = pygame.image.load('assets/images/story.png')
txt2_surface = pygame.image.load('assets/images/txt2.png')
howtoplaytxt_surface = pygame.image.load('assets/images/how-to-play.png')
txt3_surface = pygame.image.load('assets/images/txt3.png')
hintstxt_surface = pygame.image.load('assets/images/hints.png')
locked_txt_surface = pygame.image.load('assets/images/locked_txt.png')
folder1_surface = pygame.image.load('assets/images/folder1.png')
folder2_surface = pygame.image.load('assets/images/folder2.png')
folder3_surface = pygame.image.load('assets/images/folder3.png')
folder4_surface = pygame.image.load('assets/images/folder4.png')
# Hangok - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
click_sound = pygame.mixer.Sound('assets/sound/click.wav')


# Logical variables ------------------------------------------------
story = False
howtoplay = False
hints = False

# Other variables --------------------------------------------------
mx = int()
my = int()


# Loop -------------------------------------------------------------
while True:
    pygame.display.update()
    clock.tick(60)

    # Background ---------------------------------------------------
    screen.blit(background_surface, (0,0))

    # Icons --------------------------------------------------------
    screen.blit(trash_surface, (20,25))
    screen.blit(txt1_surface, (270,25))
    screen.blit(txt2_surface, (395,25))
    screen.blit(txt3_surface, (520,25))
    screen.blit(locked_txt_surface, (645,25))
    screen.blit(folder1_surface, (20,150))
    screen.blit(folder2_surface, (20,275))
    screen.blit(folder3_surface, (20,400))
    screen.blit(folder4_surface, (20,525))

    # Windows ------------------------------------------------------
    while story:
        screen.blit(storytxt_surface, (400,200))
        if 270 <= mx <= 370 and 25 <= my <= 125:
            story = False


    # Events -------------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            pygame.mixer.Sound.play(click_sound)
    if 270 <= mx <= 370 and 25 <= my <= 125:
        story = True
