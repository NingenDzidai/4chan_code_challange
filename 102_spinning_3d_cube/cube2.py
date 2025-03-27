import numpy as np
import pygame
import math as m

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 800, 600
# XY plane projection
projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
])

scale = 100
circle_pos = [WIDTH//2, HEIGHT//2]  # Corrected center position

angle = 0

# Define the cube vertices
points = [
    np.matrix([-1, -1, 1]), np.matrix([1, -1, 1]), 
    np.matrix([1, 1, 1]), np.matrix([-1, 1, 1]),
    np.matrix([-1, -1, -1]), np.matrix([1, -1, -1]), 
    np.matrix([1, 1, -1]), np.matrix([-1, 1, -1])
]

pygame.display.set_caption('3D spinning cube!')
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
    
    screen.fill(WHITE)

    # Rotation matrices
    rotation_matrix_z = np.matrix([
        [m.cos(angle), -m.sin(angle), 0],
        [m.sin(angle), m.cos(angle), 0],
        [0, 0, 1]
    ])

    rotation_matrix_x = np.matrix([
        [1, 0, 0],
        [0, m.cos(angle), -m.sin(angle)],
        [0, m.sin(angle), m.cos(angle)]
    ])

    angle += 0.02  # Speed up rotation a little

    projected_points = []
    
    for point in points:
        rotated2d = np.dot(rotation_matrix_z, point.reshape((3,1)))
        projected2d = np.dot(projection_matrix, rotated2d)
        
        x = int(projected2d[0][0] * scale + circle_pos[0])
        y = int(projected2d[1][0] * scale + circle_pos[1])
        
        pygame.draw.circle(screen, BLACK, (x, y), 5)

    pygame.display.update()