import numpy as np
import pygame
import math as m

def connect(i, j, points):
    pygame.draw.line(screen, BLACK, (points[i][0], points[i][1]), (points[j][0], points[j][1]))


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
circle_pos = [HEIGHT/2, WIDTH/2]

angle = 1

points = []
points.append(np.matrix([-1, -1, 1]))
points.append(np.matrix([1, -1, 1]))
points.append(np.matrix([1, 1, 1]))
points.append(np.matrix([-1, 1, 1]))
points.append(np.matrix([-1, -1, -1]))
points.append(np.matrix([1, -1, -1]))
points.append(np.matrix([1, 1, -1]))
points.append(np.matrix([-1, 1, -1]))

projection_points = [
    [n, n] for n in range(len(points))
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

    # rotation over Z plane
    rotation_matrix_z = np.matrix([
        [m.cos(angle), -1*m.sin(angle), 0],
        [m.sin(angle), m.cos(angle), 0],
        [0, 0, 1]
        ])
    
    # rotation over X plane
    rotation_matrix_x = np.matrix([
    [1, 0, 0],
    [0, m.cos(angle), -m.sin(angle)],
    [0, m.sin(angle), m.cos(angle)]
])
    
    # rotation over Y plane
    rotation_matrix_y = np.matrix([
    [0, m.cos(angle), -m.sin(angle)],
    [1, 0, 0],
    [0, m.sin(angle), m.cos(angle)]
])
    
    angle += 0.01

    i = 0
    for point in points:
        # reason for point.reshape((3,1))
        # vector'(3x1) = rotation_matrix(3x3) * vector(3x1), previously "point" vectors are initiared as (1x3) vector
        rotated2d = np.dot(rotation_matrix_z, point.reshape((3,1)))
        rotated2d = np.dot(rotation_matrix_x, rotated2d)
        rotated2d = np.dot(rotation_matrix_y, rotated2d)
        projected2d = np.dot(projection_matrix, rotated2d)
        x = int(projected2d[0][0] * scale) + circle_pos[0]
        y = int(projected2d[1][0] * scale) + circle_pos[1]


        projection_points[i] = [x, y]
        pygame.draw.circle(screen, BLACK, (x, y), 5) 
        i+=1
    
    connect(0, 1, projection_points)
    connect(1, 2, projection_points)
    connect(2, 3, projection_points)
    connect(3, 0, projection_points)

    connect(4, 5, projection_points)
    connect(5, 6, projection_points)
    connect(6, 7, projection_points)
    connect(7, 4, projection_points)

    connect(1, 5, projection_points)
    connect(2, 6, projection_points)
    connect(3, 7, projection_points)
    connect(4, 0, projection_points)
    
    pygame.display.update()