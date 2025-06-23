import pygame
import math
import sys

# ------------------------------------------------------------------------------
# Utility functions
# ------------------------------------------------------------------------------

def rotate_points(points, angle_degrees, center):
    """
    Rotate a list of (x, y) points by the specified angle_degrees around 'center'.
    Returns a new list of rotated points.
    """
    angle = math.radians(angle_degrees)
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    cx, cy = center
    
    rotated = []
    for x, y in points:
        # Translate point so center is (0, 0)
        tx, ty = x - cx, y - cy
        # Rotate
        rx = tx * cos_a - ty * sin_a
        ry = tx * sin_a + ty * cos_a
        # Translate back
        rx += cx
        ry += cy
        rotated.append((rx, ry))
    
    return rotated

def reflect_velocity(vel, p1, p2):
    """
    Reflect velocity vector 'vel' across the line defined by 'p1' -> 'p2'.
    Returns the new velocity vector after reflection.
    """
    # Line vector
    line_dx = p2[0] - p1[0]
    line_dy = p2[1] - p1[1]
    
    # Normalize line direction
    line_len_sq = line_dx * line_dx + line_dy * line_dy
    if abs(line_len_sq) < 1e-12:
        return vel  # Avoid division by zero, no reflection
    
    line_len = math.sqrt(line_len_sq)
    nx = line_dx / line_len
    ny = line_dy / line_len
    
    # We need normal to the line. For a line (nx, ny),
    # a normal can be (ny, -nx) or (-ny, nx).
    # Check which normal we should use by projecting velocity.
    # We'll take one normal, measure dot product, see if we need to flip sign.
    # Let's choose normal = (ny, -nx).
    # Dot product:
    dot = vel[0] * ny + vel[1] * (-nx)
    # If dot < 0, flip normal
    if dot < 0:
        ny = -ny
        nx = nx
    
    # Actually, let's define normal = (ny, -nx) or (-ny, nx) consistently:
    norm_x, norm_y = ny, -nx
    # Now reflect v = v - 2(v·n)n
    # Must normalize n
    n_len_sq = norm_x * norm_x + norm_y * norm_y
    if abs(n_len_sq) < 1e-12:
        return vel
    
    # Make n unit length
    n_len = math.sqrt(n_len_sq)
    ux = norm_x / n_len
    uy = norm_y / n_len
    
    # Dot product of vel with the normal
    vdotn = vel[0]*ux + vel[1]*uy
    
    # Reflection
    rx = vel[0] - 2.0 * vdotn * ux
    ry = vel[1] - 2.0 * vdotn * uy
    
    return (rx, ry)

def point_line_dist_sq(px, py, x1, y1, x2, y2):
    """
    Returns the squared distance from the point (px, py)
    to the line segment (x1, y1)-(x2, y2).
    """
    # Adapted from typical "closest point on line segment" algorithms
    vx = x2 - x1
    vy = y2 - y1
    wx = px - x1
    wy = py - y1
    
    c1 = wx * vx + wy * vy
    c2 = vx * vx + vy * vy
    if c2 < 1e-10:
        # Line segment is effectively a point
        return (px - x1)**2 + (py - y1)**2
    
    b = c1 / c2
    if b < 0:
        # Closest to (x1, y1)
        return (px - x1)**2 + (py - y1)**2
    elif b > 1:
        # Closest to (x2, y2)
        return (px - x2)**2 + (py - y2)**2
    
    # Closest to a point between (x1, y1) and (x2, y2)
    cx = x1 + b * vx
    cy = y1 + b * vy
    
    dx = px - cx
    dy = py - cy
    return dx*dx + dy*dy

# ------------------------------------------------------------------------------
# Main script (pygame)
# ------------------------------------------------------------------------------

def main():
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Bouncing Ball within a Rotating Square")

    clock = pygame.time.Clock()
    
    # Ball properties
    ball_radius = 10
    ball_pos = [400, 300]   # center of screen
    ball_vel = [5, 3]       # initial velocity
    
    # Square properties
    square_center = (screen_width//2, screen_height//2)
    square_size = 200
    half = square_size / 2
    # base square corners (unrotated)
    # Note that these are corners around the center
    square_corners = [
        (square_center[0] - half, square_center[1] - half),
        (square_center[0] + half, square_center[1] - half),
        (square_center[0] + half, square_center[1] + half),
        (square_center[0] - half, square_center[1] + half)
    ]
    
    rotation_angle = 0
    rotation_speed = 1  # degrees per frame

    running = True
    while running:
        dt = clock.tick(60) / 1000.0  # delta time in seconds (not used heavily here)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update rotation
        rotation_angle = (rotation_angle + rotation_speed) % 360
        
        # Move the ball
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]
        
        # Rotate square corners
        rot_corners = rotate_points(square_corners, rotation_angle, square_center)

        # Build edges of the square from the rotated corners
        edges = []
        for i in range(len(rot_corners)):
            p1 = rot_corners[i]
            p2 = rot_corners[(i + 1) % len(rot_corners)]
            edges.append((p1, p2))
        
        # Check collision with edges
        # If the center of the ball is within ball_radius of an edge, reflect
        # velocity. To avoid "sticking" in the wall, we can do a simple approach:
        # After reflection, move the ball slightly away along the new velocity.
        # This prevents repeated collisions in the same frame.
        px, py = ball_pos
        for p1, p2 in edges:
            dist_sq = point_line_dist_sq(px, py, p1[0], p1[1], p2[0], p2[1])
            if dist_sq <= (ball_radius**2 + 1e-6):
                # We have a collision
                ball_vel = reflect_velocity(ball_vel, p1, p2)
                # Move the ball a bit along the new velocity to avoid re-collision
                length_v = math.hypot(ball_vel[0], ball_vel[1])
                if length_v > 1e-6:
                    # Move a fraction of the radius away from the wall
                    # to minimize repeated collision detection in same frame
                    ball_pos[0] += (ball_vel[0] / length_v) * 2
                    ball_pos[1] += (ball_vel[1] / length_v) * 2

        # Draw everything
        screen.fill((0, 0, 0))  # black background

        # Draw the rotating square
        pygame.draw.polygon(screen, (255, 255, 255), rot_corners, width=2)
        
        # Draw the ball
        pygame.draw.circle(screen, (255, 255, 0), (int(ball_pos[0]), int(ball_pos[1])), ball_radius)

        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

# No external files are being created or modified in this script.