import pygame
from pygame.locals import *


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from game import Game
from constant import *


def main():
    pygame.init()
    pygame.mixer.init() # for sound
    pygame.font.init() # for font
    
    # clock = pygame.time.Clock() # for fps
    
    # Set OpenGL attributes for a core OpenGL profile
    pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 3)
    pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 1)
    pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)


  

    pygame.display.set_caption("Mario Game")
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), DOUBLEBUF | OPENGL)
    
    # Set up OpenGL context
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glViewport(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
    
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT, -1, 1)
    # gluOrtho2D(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)

    game = Game()

    running = True
    while running:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    game.is_moving_right = True
                if event.key == K_LEFT:
                    game.is_moving_left = True
                if event.key == K_UP and not game.is_jumping:
                    game.is_jumping = True
                if event.key == K_DOWN:
                    pass
            elif event.type == KEYUP:
                if event.key == K_RIGHT:
                    game.is_moving_right = False
                if event.key == K_LEFT:
                    game.is_moving_left = False
                    
                # for closing game
                if event.key == K_q:
                    running = False
                # for restarting game
                if event.key == K_r:
                    game = Game()
     

        # for moving background
        if game.is_moving_right:
            game.pipe_speed = FAST_BACKGROUND_SPEED
        else:
            game.pipe_speed = BACKGROUND_SPEED

   

        
        # clock.tick(120)
        game.update()
        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()



if __name__ == "__main__":
    main()