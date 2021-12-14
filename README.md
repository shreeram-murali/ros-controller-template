# ROS Navigation Templates

This repository contains the template to implement a quick ROS node which performs the following multiple useful operations through a single node.

Please note that this code repository is **not** a ROS package.

## Files

The files included in this repository are:

* `src/vision_controller.py`: This is a Python2 program which starts a ROS node that contains an image topic subscriber and a velocity message publisher, structured in such a way that one can code a control strategy in between.  
* `src/square_navigation.py`: This is a Python2 program which starts a ROS node which inputs a side length of a square and publishes a set of 2D waypoints this  the `move_base` topic that enables a mobile robot to move to these specified sequence of points such that its motion executes a square of specified length. This allows for autonomous navigation in a mapped environment using Adaptive Monte-Carlo Localization (AMCL).
* `src/varying_velocity_publisher.py`: Python2 ROS publisher which allows a mobile robot to vary its velocity as a function of time. This code implements a sinusoidal variation of a linear velocity profile, but the code can be easily modified for other trajectories. 

## Future

* C++ versions for the same template

