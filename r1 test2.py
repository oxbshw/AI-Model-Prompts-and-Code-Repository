import pygame
import math
import sys

# Initialize Pygame
pygame.init()
screen_size = 600
screen = pygame.display.set_mode((screen_size, screen_size))
clock = pygame.time.Clock()

# Square parameters
square_center = (screen_size//2, screen_size//2)
square_size = 500
half_square = square_size // 2
square_angle = 0
rotation_speed = 0.5  # Degrees per frame

# Ball parameters
ball_radius = 20
ball_pos = [screen_size//2, screen_size//2]
ball_vel = [3, 3.5]
ball_color = (255, 255, 0)  # Yellow

def rotate_point(point, angle, center=(0, 0)):
    """Rotate a point around a center point by given angle in degrees"""
    angle_rad = math.radians(angle)
    x, y = point[0] - center[0], point[1] - center[1]
    new_x = x * math.cos(angle_rad) - y * math.sin(angle_rad)
    new_y = x * math.sin(angle_rad) + y * math.cos(angle_rad)
    return (new_x + center[0], new_y + center[1])

def check_collision(ball_pos, square_center, square_angle, half_size, radius):
    # Convert ball position to square's local coordinate system
    dx = ball_pos[0] - square_center[0]
    dy = ball_pos[1] - square_center[1]
    local_pos = rotate_point((ball_pos[0], ball_pos[1]), -square_angle, square_center)

    # Get local coordinates relative to square center
    local_x = local_pos[0] - square_center[0]
    local_y = local_pos[1] - square_center[1]

    collisions = []

    # Check collisions with all walls
    if local_x > half_size - radius:
        collisions.append(('right', local_x - (half_size - radius)))
    elif local_x < -half_size + radius:
        collisions.append(('left', local_x - (-half_size + radius)))

    if local_y > half_size - radius:
        collisions.append(('bottom', local_y - (half_size - radius)))
    elif local_y < -half_size + radius:
        collisions.append(('top', local_y - (-half_size + radius)))

    return collisions

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update square rotation
    square_angle += rotation_speed
    if square_angle >= 360:
        square_angle -= 360

    # Update ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # Check collisions
    collisions = check_collision(ball_pos, square_center, square_angle, half_square, ball_radius)

    for collision in collisions:
        wall, overlap = collision

        # Calculate collision normal in world coordinates
        if wall in ('left', 'right'):
            angle = square_angle if wall == 'right' else square_angle + 180
            normal = pygame.math.Vector2(1, 0).rotate(angle)
        else:
            angle = square_angle + 90 if wall == 'bottom' else square_angle - 90
            normal = pygame.math.Vector2(1, 0).rotate(angle)

        normal = normal.normalize()

        # Reflect velocity
        ball_vel = pygame.math.Vector2(ball_vel)
        ball_vel = ball_vel.reflect(normal)
        ball_vel = list(ball_vel)

        # Position correction
        correction_vec = pygame.math.Vector2(normal) * overlap
        ball_pos[0] -= correction_vec.x
        ball_pos[1] -= correction_vec.y

    # Draw everything
    screen.fill((0, 0, 0))

    # Draw rotating square
    square_surface = pygame.Surface((square_size, square_size), pygame.SRCALPHA)
    pygame.draw.rect(square_surface, (255, 255, 255), (0, 0, square_size, square_size), 2)
    rotated_square = pygame.transform.rotate(square_surface, square_angle)
    rect = rotated_square.get_rect(center=square_center)
    screen.blit(rotated_square, rect.topleft)

    # Draw ball
    pygame.draw.circle(screen, ball_color, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

# Created/Modified files during execution:
# No files are created or modified on disk; all rendering is done in memory and displayed on screen.