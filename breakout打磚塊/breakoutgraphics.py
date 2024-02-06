"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, and Jerry Liao.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2, y=self.window.height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        self.ball_stay_still = True
        onmouseclicked(self.ball_click_to_move)

        # Draw bricks
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.brick = GRect(brick_width, brick_height,
                                    x=(brick_width + brick_spacing) * i, y=brick_offset+(brick_spacing+brick_height)*j)
                self.brick.filled = True
                if j == 0 or j == 1:
                    color = 'red'
                elif j == 2 or j == 3:
                    color = 'orange'
                elif j == 4 or j == 5:
                    color = 'yellow'
                elif j == 6 or j == 7:
                    color = 'green'
                else:
                    color = 'blue'
                self.brick.fill_color = color
                self.brick.color = color
                self.window.add(self.brick)

        # Calculate total bricks number
        self.total_bricks = brick_cols*brick_rows

    def paddle_move(self, mouse):
        """
        Paddle follows mouse's horizontal movement. Paddle always appears completely.
        """
        if self.paddle.width/2 < mouse.x < self.window.width - self.paddle.width/2:
            self.paddle.x = mouse.x-self.paddle.width/2

    def ball_click_to_move(self, event):
        """
        If ball stay stationary at the starting point first, click the mouse to let ball be ready to move.
        """
        if self.ball_stay_still is True:
            self.ball_stay_still = False
            self.set_starting_velocity()

    def set_starting_velocity(self):
        """
        Set y velocity as the number of ''initial y speed'', x velocity as random positive or negative number.
        """
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def reset_ball(self):
        """
        Add a stationary new ball at the starting point.
        """
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                        y=(self.window.height - self.ball.height) / 2)
        self.__dx = 0
        self.__dy = 0
        self.ball_stay_still = True

    def random_dx(self):
        """
        set a new x velocity using random positive or negative number.
        """
        new_dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            new_dx = -new_dx
        return new_dx

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dx(self, new_dx):
        self.__dx = new_dx

    def set_dy(self, new_dy):
        self.__dy = new_dy
