This is a test set for micromouse controlling system. 

Right.py: Rightwall follower, main algorithm.

rotationt.py: For testing rotation motions.

sensort.py: Testing the side sensors' reading.

motortest.py: Testing for the motor's movement.

Gyrotry: Testing whether the robot moves properly in a short distance in the maze.

puretryIR: Using sensors without gyro to see whether it moves correctly in the maze. Previous work and needs to be updated.

Rightwall.sh: A bash script for trying to make it record the path into a file.

gyroTest.py, adjustgy.py: For adjusting gyro sensor.

To run any python files, please run:

$ python3 <filename>

in terminal environment of micromouse.

To get make the program runnable directly from brickman, please set the previlige of the files like this:

$ chmod +x <filename>

And don't delete the first line commented in every python files.
