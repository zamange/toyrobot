
## Maze Robot
This Python program simulates a robot navigating a maze. The robot can move forward, backward, turn left, and turn right. It can also execute a sprint command to move multiple steps at once. Additionally, the robot can solve mazes automatically using a search algorithm.

## Prerequisites
- Python 3.x
- Tkinter

## Usage
To run the program, execute the following command in your terminal:

bash
Copy code:
    python3 maze_robot.py

The program will prompt you to enter a name for your robot. After entering the name, you can start issuing commands to the robot.

## Commands
The robot understands the following commands:

off: Shutdown the robot.
help: Display information about available commands.
forward n: Move the robot forward by n steps.
back n: Move the robot backward by n steps.
right: Turn the robot 90 degrees to the right.
left: Turn the robot 90 degrees to the left.
sprint n: Sprint forward according to a formula.
replay: Replay the command history.
replay silent: Replay the command history silently.
replay reversed: Replay the command history in reverse order.
mazerun [direction]: Solve the maze automatically and move to the specified edge.
Note
You can run the program with the turtle option to visualize the robot's movements using the Turtle graphics library. Example: python3 maze_robot.py turtle.
The maze solving functionality requires a separate maze_solver.py module.
Make sure to include the maze_solver.py module in the same directory as maze_robot.py for maze solving to work properly.
