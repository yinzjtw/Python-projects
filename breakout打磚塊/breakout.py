"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, and Jerry Liao.


Players can play "breakout" game by running this code:
Player's goal is to remove all the bricks by using ball to hit the bricks.
At the beginning, ball will be stationary at the starting point.
Player clicks the mouse, and ball will start dropping.
If ball hits the paddle, it'll bounce back at random horizontal direction (paddle can be moved by the mouse);
if it drops under the horizontal line, player lost one life.
Game will end at:　1)no life left or 2) all the bricks are removed.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 10			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    used_life = 0
    count_brick = 0
    while True:
        if used_life == NUM_LIVES or count_brick == graphics.total_bricks:
            break
        else:
            dx = graphics.get_dx()  #self.__dx一開始抓的值多少 不會因為後面改而變動 除非CODER端的SEIF DX DY改變 所以要SETTER
            dy = graphics.get_dy()
            graphics.ball.move(dx, dy)
            pause(FRAME_RATE)

            # If ball hits walls at the two sides, or hits the ceiling, turn around.
            if graphics.ball.x < 0 or graphics.ball.x + graphics.ball.width > graphics.window.width:
                graphics.set_dx(-dx)
            if graphics.ball.y <= 0:
                graphics.set_dy(-dy)  # 用setter改coder端儲存的dx值，迴圈就會get到新的值

            # If ball falls out of the horizontal line, lost one life.
            # Put a stationary new ball at the starting position.
            if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                used_life += 1
                graphics.reset_ball()

            # Finds out if ball hits the paddle or any brick.
            maybe_object = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
            if maybe_object is None:
                maybe_object = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y)
                if maybe_object is None:
                    maybe_object = graphics.window.get_object_at\
                        (graphics.ball.x + graphics.ball.width, graphics.ball.y + graphics.ball.height)
                    if maybe_object is None:
                        maybe_object = graphics.window.get_object_at\
                            (graphics.ball.x + graphics.ball.width, graphics.ball.y + graphics.ball.height)
            if maybe_object is not None:
                # If ball hits the paddle, reset horizontal speed and direction,and reverse the vertical direction.
                if maybe_object is graphics.paddle:
                    graphics.set_dx(graphics.random_dx())
                    if dy > 0:  # to make sure ball won't stuck in the middle of the paddle.
                        graphics.set_dy(-dy)
                else:
                    # If ball hits a brick, reset horizontal speed and direction,and reverse the vertical direction.
                    # Remove the hit brick as well.
                    graphics.set_dx(graphics.random_dx())
                    graphics.set_dy(-dy)
                    graphics.window.remove(maybe_object)
                    count_brick += 1


if __name__ == '__main__':
    main()


