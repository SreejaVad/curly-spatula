# Implementation of classic arcade game Pong

# noinspection PyInterpreter
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [1, 1]
paddle1_pos = [PAD_WIDTH, 0]
paddle2_pos = [WIDTH - PAD_WIDTH, 0]
paddle1_vel = [0, 0]
paddle2_vel = [0, 0]
score1 = 0
score2 = 0

# helper function that spawns a ball by updating the
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists

    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel = [0, 0]
    ball_pos[0] += 0.05 * ball_vel[0]
    ball_pos[1] += 0.01 * ball_vel[1]

    ball_vel[0] = ball_vel[0] + random.randrange(120, 240)
    ball_vel[1] = ball_vel[0] + random.randrange(60, 180)

    if right:
        ball_vel[0] =    ball_vel[0]
        ball_vel[1] =  - ball_vel[1]
    else:
        ball_vel[0] =  - ball_vel[0]
        ball_vel[1] =  - ball_vel[1]


def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    ball_init(False)

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel

    # update paddle's vertical position, keep paddle on the screen

    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([0, 0],[PAD_WIDTH, 0], 1, "Red")

    # draw paddles
    c.draw_polygon([paddle1_pos, [0, paddle1_pos[1]], [0, paddle1_pos[1] + PAD_HEIGHT],[PAD_WIDTH, paddle1_pos[1] + PAD_HEIGHT] ], 1, "Red", "Red")

    #c.draw_line(paddle1_pos, [0, paddle1_pos[1]], 1, "Red")
    #c.draw_line([0, paddle1_pos[1]], [0, paddle1_pos[1] + PAD_HEIGHT], 1, "Red")
    #c.draw_line([0, paddle1_pos[1]+ PAD_HEIGHT], [PAD_WIDTH, paddle1_pos[1] + PAD_HEIGHT], 1, "Red")
    #c.draw_line([PAD_WIDTH, paddle1_pos[1] + PAD_HEIGHT], paddle1_pos, 1, "Red")

    c.draw_polygon([paddle2_pos, [WIDTH, paddle2_pos[1]], [WIDTH, paddle2_pos[1] + PAD_HEIGHT],[WIDTH - PAD_WIDTH, paddle2_pos[1] + PAD_HEIGHT] ], 1, "Red", "Red")
    #c.draw_line( paddle2_pos, [WIDTH-1, paddle2_pos], 1, "Red")
    #c.draw_line([WIDTH, paddle2_pos], [WIDTH, paddle2_pos[1] + PAD_HEIGHT], 1, "Red")
    #c.draw_line([WIDTH, paddle2_pos[1] + PAD_HEIGHT], [WIDTH - PAD_WIDTH, paddle2_pos[1] + PAD_HEIGHT], 1, "Red")
    #c.draw_line([WIDTH - PAD_WIDTH, paddle2_pos[1] + PAD_HEIGHT], paddle2_pos, 1, "Red")

    # update ball
    ball_pos[0] += 0.05 * ball_vel[0]
    ball_pos[1] += 0.01 * ball_vel[1]
    # test for ball touching top
    if ball_pos[1] < BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    # test for ball touching bottom
    if ball_pos[1] > HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    # test for ball touching left gutter
    if ball_pos[0] < BALL_RADIUS + PAD_WIDTH:
        if( (ball_pos[1] >= paddle1_pos[1]) and (ball_pos[1] <= paddle1_pos[1] + PAD_HEIGHT) ):
            ball_vel[0] = ball_vel[0] + 0.1 * ball_vel[0]
            ball_vel[0] = -ball_vel[0]
        else:
            ball_init(True)
            score2 += 1

    # test for ball touching right gutter
    if ball_pos[0] > WIDTH - BALL_RADIUS - PAD_WIDTH:
        if( (ball_pos[1] >= paddle2_pos[1]) and (ball_pos[1] <= paddle2_pos[1] + PAD_HEIGHT) ):
            ball_vel[0] = ball_vel[0] + 0.1 * ball_vel[0]
            ball_vel[0] = -ball_vel[0]
        else:
            ball_init(False)
            score1 += 1


    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    c.draw_text(str(score1), (150, 40), 30, "White", "serif")
    c.draw_text(str(score2), (450, 40), 30, "White", "serif")



def keydown(key):
    global paddle1_vel, paddle2_vel
    step = 20
    if str(chr(key)).upper() == "W":
        if  paddle1_pos[1] > 0:
            paddle1_vel[1] = step
            paddle1_pos[1] -=  paddle1_vel[1]
        else:
            paddle1_pos[1] = 0

    if str(chr(key)).upper() == "S":
        if (paddle1_pos[1] + PAD_HEIGHT) < HEIGHT:
            paddle1_vel[1] = step
            paddle1_pos[1] += paddle1_vel[1]
        else:
            paddle1_pos[1] =  HEIGHT - PAD_HEIGHT

    if key==simplegui.KEY_MAP["up"]:
        if  paddle2_pos[1] > 0:
            paddle2_vel[1] = step
            paddle2_pos[1] -=  paddle2_vel[1]
        else:
            paddle2_pos[1] = 0

    if key==simplegui.KEY_MAP["down"]:
        if (paddle2_pos[1] + PAD_HEIGHT) < HEIGHT:
            paddle2_vel[1] =step
            paddle2_pos[1] += paddle2_vel[1]
        else:
            paddle2_pos[1] =  HEIGHT - PAD_HEIGHT



def keyup(key):
    global paddle1_vel, paddle2_vel
    step = 20
    if str(chr(key)).upper() == "W":
        if  paddle1_pos[1] > 0:
            paddle1_vel[1] = step
            paddle1_pos[1] -=  paddle1_vel[1]
        else:
            paddle1_pos[1] = 0

    if str(chr(key)).upper() == "S":
        if (paddle1_pos[1] + PAD_HEIGHT) < HEIGHT:
            paddle1_vel[1] = step
            paddle1_pos[1] += paddle1_vel[1]
        else:
            paddle1_pos[1] =  HEIGHT - PAD_HEIGHT

    if key==simplegui.KEY_MAP["up"]:
        if  paddle2_pos[1] > 0:
            paddle2_vel[1] = step
            paddle2_pos[1] -=  paddle2_vel[1]
        else:
            paddle2_pos[1] = 0

    if key==simplegui.KEY_MAP["down"]:
        if (paddle2_pos[1] + PAD_HEIGHT) < HEIGHT:
            paddle2_vel[1] = step
            paddle2_pos[1] += paddle2_vel[1]
        else:
            paddle2_pos[1] =  HEIGHT - PAD_HEIGHT

def button_handler():
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button2 = frame.add_button("Restart", button_handler, 70)


# start frame
frame.start()
new_game()

