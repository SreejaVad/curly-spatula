# Ping Pong Game

import simplegui
import random

# Global Variables: Position and Velocity
TABLE_WIDTH = 800
TABLE_HEIGHT = 600
BALL_RADIUS = 20
PADDLE_WIDTH = 8
PADDLE_HEIGHT = 80
HALF_PADDLE_WIDTH = PADDLE_WIDTH / 2
HALF_PADDLE_HEIGHT = PADDLE_HEIGHT / 2
ball_position = [TABLE_WIDTH/2, TABLE_HEIGHT/2]
ball_velocity = [1, 1]
paddle1_position = [PADDLE_WIDTH, 0]
paddle2_position = [TABLE_WIDTH - PADDLE_WIDTH, 0]
paddle1_velocity = [0, 0]
paddle2_velocity = [0, 0]
player1_score = 0
player2_score = 0

# Init code to spawn a ball and updates ball's position & velocity vector.
# if right is True, the ball's velocity is upper right, otherwise upper left
def ball_init(right):
    global ball_position, ball_velocity # x,y values stored as lists

    ball_position = [TABLE_WIDTH/2, TABLE_HEIGHT/2]
    ball_velocity = [0, 0]
    ball_position[0] += 0.05 * ball_velocity[0]
    ball_position[1] += 0.01 * ball_velocity[1]

    ball_velocity[0] = ball_velocity[0] + random.randrange(120, 240)
    ball_velocity[1] = ball_velocity[0] + random.randrange(60, 180)

    if right:
        ball_velocity[0] = ball_velocity[0]
        ball_velocity[1] = - ball_velocity[1]
    else:
        ball_velocity[0] = - ball_velocity[0]
        ball_velocity[1] = - ball_velocity[1]


def start_game():
    global paddle1_position, paddle2_position, paddle1_velocity, paddle2_velocity  # these are floats
    global player1_score, player2_score  # integer variables that are used to store the player's score
    player1_score = 0
    player2_score = 0
    ball_init(False) # Initialize ball position and compute random velocity

def update(canvas):
    global player1_score, player2_score, paddle1_position, paddle2_position, ball_position, ball_velocity

    # draw center line and borders
    canvas.draw_line([TABLE_WIDTH / 2, 0],[TABLE_WIDTH / 2, TABLE_HEIGHT], 1, "White")
    canvas.draw_line([PADDLE_WIDTH, 0],[PADDLE_WIDTH, TABLE_HEIGHT], 1, "White")
    canvas.draw_line([TABLE_WIDTH - PADDLE_WIDTH, 0],[TABLE_WIDTH - PADDLE_WIDTH, TABLE_HEIGHT], 1, "White")
    canvas.draw_line([0, 0],[PADDLE_WIDTH, 0], 1, "Red")

    # Use draw_polygon method (instead of draw_line) to draw paddles
    canvas.draw_polygon([paddle1_position, [0, paddle1_position[1]], [0, paddle1_position[1] + PADDLE_HEIGHT],[PADDLE_WIDTH, paddle1_position[1] + PADDLE_HEIGHT] ], 1, "Red", "Red")
    canvas.draw_polygon([paddle2_position, [TABLE_WIDTH, paddle2_position[1]], [TABLE_WIDTH, paddle2_position[1] + PADDLE_HEIGHT],[TABLE_WIDTH - PADDLE_WIDTH, paddle2_position[1] + PADDLE_HEIGHT] ], 1, "Red", "Red")

    # update ball position
    ball_position[0] += 0.05 * ball_velocity[0]
    ball_position[1] += 0.01 * ball_velocity[1]
    # test for ball touching top border
    if ball_position[1] < BALL_RADIUS:
        ball_velocity[1] = -ball_velocity[1]
    # test for ball touching bottom border
    if ball_position[1] > TABLE_HEIGHT - BALL_RADIUS:
        ball_velocity[1] = -ball_velocity[1]
    # test for ball touching left border
    if ball_position[0] < BALL_RADIUS + PADDLE_WIDTH:
        if( (ball_position[1] >= paddle1_position[1]) and (ball_position[1] <= paddle1_position[1] + PADDLE_HEIGHT) ):
            ball_velocity[0] = ball_velocity[0] + 0.1 * ball_velocity[0]
            ball_velocity[0] = -ball_velocity[0]
        else:
            ball_init(True)
            player2_score += 1

    # test for ball touching right border
    if ball_position[0] > TABLE_WIDTH - BALL_RADIUS - PADDLE_WIDTH:
        if( (ball_position[1] >= paddle2_position[1]) and (ball_position[1] <= paddle2_position[1] + PADDLE_HEIGHT) ):
            ball_velocity[0] = ball_velocity[0] + 0.1 * ball_velocity[0]
            ball_velocity[0] = -ball_velocity[0]
        else:
            ball_init(False)
            player1_score += 1


    # create the ball and corresponding points text
    canvas.draw_circle(ball_position, BALL_RADIUS, 2, "Red", "White")
    canvas.draw_text(str(player1_score), (150, 40), 30, "White", "serif")
    canvas.draw_text(str(player2_score), (450, 40), 30, "White", "serif")



def keydown(key):
    global paddle1_velocity, paddle2_velocity
    step = 20
    if str(chr(key)).upper() == "W":
        if  paddle1_position[1] > 0:
            paddle1_velocity[1] = step
            paddle1_position[1] -=  paddle1_velocity[1]
        else:
            paddle1_position[1] = 0

    if str(chr(key)).upper() == "S":
        if (paddle1_position[1] + PADDLE_HEIGHT) < TABLE_HEIGHT:
            paddle1_velocity[1] = step
            paddle1_position[1] += paddle1_velocity[1]
        else:
            paddle1_position[1] =  TABLE_HEIGHT - PADDLE_HEIGHT

    if key==simplegui.KEY_MAP["up"]:
        if  paddle2_position[1] > 0:
            paddle2_velocity[1] = step
            paddle2_position[1] -=  paddle2_velocity[1]
        else:
            paddle2_position[1] = 0

    if key==simplegui.KEY_MAP["down"]:
        if (paddle2_position[1] + PADDLE_HEIGHT) < TABLE_HEIGHT:
            paddle2_velocity[1] =step
            paddle2_position[1] += paddle2_velocity[1]
        else:
            paddle2_position[1] =  TABLE_HEIGHT - PADDLE_HEIGHT



def keyup(key):
    global paddle1_velocity, paddle2_velocity
    step = 20
    if str(chr(key)).upper() == "W":
        if  paddle1_position[1] > 0:
            paddle1_velocity[1] = step
            paddle1_position[1] -=  paddle1_velocity[1]
        else:
            paddle1_position[1] = 0

    if str(chr(key)).upper() == "S":
        if (paddle1_position[1] + PADDLE_HEIGHT) < TABLE_HEIGHT:
            paddle1_velocity[1] = step
            paddle1_position[1] += paddle1_velocity[1]
        else:
            paddle1_position[1] =  TABLE_HEIGHT - PADDLE_HEIGHT

    if key==simplegui.KEY_MAP["up"]:
        if  paddle2_position[1] > 0:
            paddle2_velocity[1] = step
            paddle2_position[1] -=  paddle2_velocity[1]
        else:
            paddle2_position[1] = 0

    if key==simplegui.KEY_MAP["down"]:
        if (paddle2_position[1] + PADDLE_HEIGHT) < TABLE_HEIGHT:
            paddle2_velocity[1] = step
            paddle2_position[1] += paddle2_velocity[1]
        else:
            paddle2_position[1] =  TABLE_HEIGHT - PADDLE_HEIGHT

def button_handler():
    start_game()

# create game frame
game_frame = simplegui.create_frame("Ping-Pong", TABLE_WIDTH, TABLE_HEIGHT)
game_frame.set_draw_handler(update)
game_frame.set_keydown_handler(keydown)
game_frame.set_keyup_handler(keyup)
button2 = game_frame.add_button("Restart", button_handler, 70)


# start game after creating game frame window.
game_frame.start()
start_game()

