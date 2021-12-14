from __future__ import print_function
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import numpy as np
import time
import math


def sine_prof():
    # Initialize new node
    rospy.init_node('varying_vels')

    # Initialize publisher
    velocity_publisher = rospy.Publisher(
        '/nav/cmd_vel', Twist, queue_size=10
    )
    while not velocity_publisher.get_num_connections():
        print("Publisher node still starting")
        time.sleep(0.1)
    
    vel_msg = Twist()

    # The math of a sine wave
    amplitude = 0.05 
    offset = 0.1
    w = 1.0
    t0 = time.time()

    vel_msg.linear.x = amplitude
    vel_msg.linear.y, vel_msg.linear.z = 0, 0 
    vel_msg.angular.x, vel_msg.angular.y, vel_msg.angular.z = 0, 0, 0


    # Publishing
    rate = rospy.Rate(10) # 10 times per second

    while not rospy.is_shutdown():
        t = time.time() - t0
        vel_msg.linear.x = (amplitude * math.sin(w * t)) + offset
        velocity_publisher.publish(vel_msg)
        rate.sleep()

if __name__ == '__main__':
    #placeholder
    try:
        sine_prof()
    except rospy.ROSInterruptException:
        # Stop
        print("End")