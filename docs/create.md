{% include navigation.html %}

# Create Task
#### [Click Here for the Video](https://youtu.be/AnA6Bw60aAE)
#### [Click Here to Visit My Create Task Wiki](https://github.com/SreejaVad/curly-spatula/wiki/Create-Task-Write-Up)
#### [Click Here to View Running Code On CodeSkulptor](https://py2.codeskulptor.org/#user49_RqH3NC6Ooe_0.py)
#### [Click Here to View Raw Code on Github](https://github.com/SreejaVad/curly-spatula/blob/main/ponggame.py)

3a: (i) (ii) (iii) (147 words)
> This program is intended to be a ping pong-inspired game that could serve as a 'brain-break' so students can take short intermissions in between their work in a more interactive way that wouldn't be as addicting as other video games and that could contrast the more academic aspects of their lives. This program is written in python and is a two-player game that uses the "W" & "S" and "UP" & "DOWN" keys to control each paddle. This game uses a GUI framework called "simplegui" to support windowing (frame) capabilities, window draw, and key handlers. The draw handler is responsible for drawing on the window so the viewer sees the updates of the game instantaneously.  As the players move the "UP" and "DOWN" keys, the input, the output results in the paddles moving up and down and the ball being moved to both sides of the screen.

3b: (i)
<p align="Left">
  <img 
    width="550"
    height=""
    src="https://user-images.githubusercontent.com/89220356/166173498-f64e277f-e16e-4643-88a1-49cbd52deff8.png">
</p>

3b: (ii)
<p align="Left">
  <img 
    width="550"
    height=""
    src="https://user-images.githubusercontent.com/89220356/166173401-8e4dc872-800d-4ef1-98a8-2eee90f8e43b.png">
</p>

3b: (iii) (iv) (v) (214 words)
> The names of the lists being used in this response is "ball_position[0, 0]" and "ball_velocity[0, 0]". The ball position list values are set to the middle of the table in the ball_unit function. Ball_position is a list of x, y values of the "ball_position" on the frame (ping-pong table) while "ball_velocity" is a list of velocity vectors that are used to compute new corresponding x, y values of the position. The list was used to help manage the indexes in terms of the position of (x,y) as well as the velocity of (x,y). Initial velocity vector list values are set to 0 and then incremented by random values based on direction. If the direction is true, then the ball moves towards the top right as the "y" value of the velocity vector is negated and the y value of the ball position decreases. Same reason for the false case where both x and y positions decreases and the ball moves towards the top left. We took the list for both position and velocity vectors so that we can access list values with their indexes corresponding to x and y respectively. If we use variables other than the list, we may have to define pos_x, pos_y for the position, and vel_x, vel_y for velocity respectively.


3c: (i)
<p align="Left">
  <img 
    width="550"
    height=""
    src="https://user-images.githubusercontent.com/89220356/166186078-b2ee12a3-450a-4441-a2ee-d299d44ca7da.png">
<p align="Left">
  <img 
    width="550"
    height=""
    src="https://user-images.githubusercontent.com/89220356/166186140-f5856cbe-0a17-475b-b473-4ee5c665fc5d.png">
<p align="Left">
  <img 
    width="550"
    height=""
    src="https://user-images.githubusercontent.com/89220356/166186167-99c159fb-0523-4e5b-a7c9-3c93e486e777.png">
<br>
3c: (ii)
<p align="Left">
  <img 
    width="550"
    height=""
    src="https://user-images.githubusercontent.com/89220356/166186961-b419aadf-65bd-42c6-81b3-1702e34dbe81.png">
<br>

3c : (iii) (iv) (250 words)
> I am using the simplegui module for User Interface. This module offers a frame that is nothing but a window. We can register event handlers such as draw hander (in our case, "update") who is responsible for drawing on the canvas. After the frame is started, the registered draw handler is invoked about 60 times per second and updates the canvas as per the code in the draw handler (update) function. Code in this function draws the table, updates the ball position, and checks whether the ball is touching the paddle or not. If not touching the paddle, the opponent scores a point. Negates the "y" velocity vector when the ball touches either the top or bottom borders of the table. The score is updated on the screen. The " update" function draws ping-pong table borders, middle line, and left and right paddles. The "ball_init" function sets the ball position at the middle of the board and sets velocity vectors to some random values. The update function moves the ball position from its current position by adding velocity vectors. Also checks whether the ball is touching either the top or the bottom border of the table. If touches, the ball's vertical vector is reversed so that ball bounces back. If the ball touches the paddle, the horizontal vector is reversed so that the ball bounces in the horizontal direction. If the ball doesn't touch the paddle, the ball starts in the middle of the table.

<br>

3d: (i) (127 Words)
#### First Call: ball_init(True)
> This function initializes the ball position to the middle of the ping-pong table. The velocity vectors list values are set to some random values. The argument value is "True" and the vertical velocity vector (y)value is negated.

<br>


Second Call: ball_init(False)
> The argument value is "False", both the horizontal (x) & vertical velocity vector (y) values are negated.

<br>


3d: (ii)

<br>


Condition(s) tested by the first call:
> if direction:
ball_velocity[0] = ball_velocity[0]
ball_velocity[1] = - ball_velocity[1]

<br>

Condition(s) tested by the second call:
> else:
ball_velocity[0] = - ball_velocity[0]
ball_velocity[1] = - ball_velocity[1]

<br>

3d: (iii)
> Result of the first call: The direction value "True" is tested here and the ball initially starts going to the top right of the table as the velocity vertical vector is negated.
> Result of the second call:The direction value "False" is tested here and the ball initially starts going to the top left of the table as both horizontal & vertical velocity vectors are negated.



