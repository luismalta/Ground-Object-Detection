# !/usr/bin/env python

import rospy
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist


import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image


class bebop():

    #Node constructor
    def __init__(self, number):

        node_name = "bebop_drive: " + str(number)
        rospy.init_node(node_name)

        self.takeoff_pub = rospy.Publisher("/bebop/takeoff", Empty, queue_size=1)
        self.land_pub = rospy.Publisher("/bebop/land", Empty, queue_size = 1)
        self.cmd_vel_pub = rospy.Publisher("/bebop/cmd_vel", Twist, queue_size = 1)

        self.image_sub = rospy.Subscriber("/bebop/image_raw", Image, self.image_callback, queue_size = 1)

    def takeoff(self):
        takeoff_msg = Empty()

        rospy.loginfo("Taking off")
        self.takeoff_pub.publish(takeoff_msg)

    def land(self):
        land_msg = Empty()

        rospy.loginfo("Landing")
        self.land_pub.publish(land_msg)

    def cmd_vel(self, vectors):

        cmd_vel_msg = Twist()
        cmd_vel_msg.linear.x = vectors[0]
        cmd_vel_msg.linear.y = vectors[1]
        cmd_vel_msg.linear.z = vectors[2]
        cmd_vel_msg.angular.x = vectors[3]
        cmd_vel_msg.angular.y = vectors[4]
        cmd_vel_msg.angular.z = vectors[5]

        rospy.loginfo("Moving")
        self.cmd_vel_pub.publish(cmd_vel_msg)

    def image_callback(self, image):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(image, "bgr8")
        except CvBridgeError as e:
            print(e)

        image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        image = Img.fromarray(image)
