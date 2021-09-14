import rospy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge
import cv2
import numpy as np
import time


def publisher(vels, interrupt=False):
    vel_msg = Twist()
    # assign values here or generate values from the controller function
    (vel_msg.linear.x, vel_msg.linear.y, vel_msg.linear.z) = (0, 0, 0)
    (vel_msg.angular.x, vel_msg.angular.y, vel_msg.angular.z) = (0, 0, 0)

    velocity_publisher.publish(vel_msg)
    if KeyboardInterrupt:
        (vel_msg.linear.x, vel_msg.angular.z) = (0, 0)
        velocity_publisher.publish(vel_msg)


def controller():
    """The code here calculates the velocity to be published based on vision messages."""


def callback(data, i):
    bridge = CvBridge()
    rospy.loginfo("received video frame")
    start = time.time()
    current_frame = bridge.imgmsg_to_cv2(data)
    # Perform required vision-based detection on current_frame
    result = controller()
    i += 1
    try:
        publisher(result)
    except rospy.ROSInterruptException: pass 


if __name__ == '__main__':
    rospy.init_node('controller')
    i = 0
    velocity_publisher = rospy.Publisher('nav/cmd_vel', Twist, queue_size=10) # Publish to commanded velocity topic
    while not velocity_publisher.get_num_connections(): # Wait till the publisher is fully initialised
        time.sleep(0.5)
        rospy.loginfo('Still waiting for publisher to be initialised') 
    rospy.Subscriber('/camera/topic', Image, callback, callback_args=i)
    rospy.spin()
    cv2.destroyAllWindows()