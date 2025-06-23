# Bouncing Ball in Rotating Square

## Prompt Information

**Category**: Graphics/Animation  
**Difficulty**: ⭐⭐⭐  
**Language**: English  
**Skills Tested**: Physics simulation, collision detection, coordinate transformation, graphics programming

## Prompt Text

```
Write a Python script for a bouncing yellow ball within a square. 
Make sure to handle collision detection properly. Make the square 
slowly rotate. Implement it in Python. Ensure the ball stays within 
the square.
```

## Expected Output

A complete Python script that:
- Creates a graphical window with animation
- Displays a yellow ball bouncing within a square boundary
- Implements proper collision detection with square walls
- Rotates the square slowly and continuously
- Maintains the ball within the rotating square boundaries
- Uses appropriate graphics library (pygame, tkinter, or similar)

## Skills Evaluation

### Primary Skills (70 points)
- **Physics Simulation (25 points)**
  - Realistic ball movement and velocity
  - Proper gravity or momentum implementation
  - Smooth animation without jitter

- **Collision Detection (25 points)**
  - Accurate detection of ball-wall collisions
  - Proper velocity reversal upon collision
  - Handling of corner cases and edge collisions

- **Coordinate Transformation (20 points)**
  - Correct rotation of square around center point
  - Proper transformation of collision boundaries
  - Maintaining ball position relative to rotated square

### Secondary Skills (30 points)
- **Code Quality (15 points)**
  - Clean, readable code structure
  - Appropriate variable naming
  - Proper commenting and documentation

- **Graphics Implementation (15 points)**
  - Smooth visual animation
  - Appropriate use of graphics library
  - Efficient rendering without flickering

## Evaluation Criteria

### Excellent (90-100 points)
- Perfect collision detection in all scenarios
- Smooth rotation and ball movement
- Clean, well-documented code
- Handles edge cases properly
- Efficient and optimized implementation

### Good (70-89 points)
- Collision detection works in most cases
- Minor visual glitches or jerky movement
- Code is functional but may lack optimization
- Basic documentation present

### Satisfactory (50-69 points)
- Basic collision detection implemented
- Ball stays mostly within boundaries
- Code runs but may have bugs
- Limited or unclear documentation

### Needs Improvement (0-49 points)
- Poor or missing collision detection
- Ball frequently escapes boundaries
- Code has significant bugs or doesn't run
- No documentation or comments

## Common Challenges

### Technical Challenges
- Implementing rotation transformation matrices
- Handling collision detection in rotated coordinate system
- Maintaining smooth animation frame rate
- Dealing with floating-point precision issues

### AI Model Challenges
- Understanding coordinate system transformations
- Balancing multiple requirements (collision + rotation)
- Choosing appropriate graphics libraries
- Implementing smooth animation loops

## Sample Test Cases

### Test Case 1: Basic Functionality
- Ball should bounce off all four walls
- Square should rotate continuously
- No escape from boundaries

### Test Case 2: Edge Cases
- Ball hitting corners should bounce appropriately
- High-speed ball should not pass through walls
- Rotation speed should not affect collision detection

### Test Case 3: Performance
- Animation should run smoothly (30+ FPS)
- No memory leaks during extended runtime
- Responsive to user interactions (if any)

## Variations

### Easier Version (⭐⭐)
```
Create a bouncing ball in a stationary square with proper collision detection.
```

### Harder Version (⭐⭐⭐⭐)
```
Create multiple bouncing balls of different colors within a rotating square, 
with ball-to-ball collision detection and physics.
```

### Alternative Focus (⭐⭐⭐)
```
Create a bouncing ball within a rotating triangle, ensuring the ball 
follows the triangle's rotation and bounces off all three sides.
```

## Implementation Notes

### Recommended Libraries
- **pygame**: Best for game-like animations
- **tkinter**: Simple, built-in Python GUI library
- **matplotlib**: For mathematical visualization approach
- **pyglet**: Advanced graphics and animation

### Key Concepts
- Vector mathematics for ball movement
- Rotation matrices for coordinate transformation
- Frame-based animation loops
- Collision response calculations

## Related Resources

- [Pygame Documentation](https://www.pygame.org/docs/)
- [2D Collision Detection Tutorial](https://developer.mozilla.org/en-US/docs/Games/Techniques/2D_collision_detection)
- [Rotation Matrix Mathematics](https://en.wikipedia.org/wiki/Rotation_matrix)
- [Game Physics Basics](https://gafferongames.com/post/integration_basics/)

---

**Added**: June 23, 2025  
**Last Updated**: June 23, 2025  
**Contributor**: Repository Team
