#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import numpy as np

def subscriber_callback(pose:Pose):
    msg = Twist()

    if pose.x>9.0 or pose.x<2.0 or pose.y<2.0 or pose.y>9.0:
        msg.linear.x = 1
        msg.angular.z= 1.4
    else:
        msg.linear.x = 5
        msg.angular.z = 0


    publisher.publish(msg)

if __name__=='__main__':
    rospy.init_node("Controller Started")

    rospy.loginfo("Let's start the controller")
    publisher = rospy.Publisher("/turtle1/cmd_vel",Twist, queue_size=10)
    subscriber = rospy.Subscriber("/turtle1/pose",Pose, callback=subscriber_callback)
    rospy.spin()