#! /usr/bin/python3
from    std_msgs.msg import String
from    sensor_msgs.msg import Image
from    cv_bridge import CvBridge, CvBridgeError

import  rospy
import  cv2 


def callbacksub(data):
    cv=CvBridge()
    imagen=cv2.imgmsg_to_cv2(data,"bgr8")
    cv2.imshow('image',img)
    publisher(imagen)

def publisher(imagen):
    image = self.CvBridge.cv2_to_imgmsg(imagen,encoding="passthrough")
    rospy.Publisher("image_topic",image)
    
    

def subscriber():
    rospy.Subscriber("/camera/rgb/image_raw",Image,callbacksub)
    
    
if __name__ == "__main__":
    try:
       rospy.init_node("object_detection")
       rate = rospy.Rate(10)
       subscriber()
      
             
             
   
