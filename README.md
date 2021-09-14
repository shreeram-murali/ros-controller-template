# ROS Controller Template

This repository contains the template to implement a quick ROS node which performs the following operations through a single node.

1. Subscriber to a sensor topic — in this case, raw camera images.
2. Includes the structure for a controller which can be used to calculate desired positions or velocities.
3. Publisher to the commanded velocity topic.

## Files

The files included in this repository are:

* `src/vision_controller.py`: This is a Python2 program which starts a ROS node that contains an image topic subscriber and a velocity message publisher, structured in such a way that one can code a control strategy in between.  

## Future

* C++ versions for the same template
* ROS subscriber for depth cameras

