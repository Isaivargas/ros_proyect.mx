#! /usr/bin/python3.8

import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import sys


bridge = CvBridge()

def image_callback(ros_image):
  print ('Recibi imagen')
  global bridge
  #ros_image a opencv
  try:
    cv_image = bridge.imgmsg_to_cv2(ros_image, "bgr8")
  except CvBridgeError as e:
    print(e)
  #Ahora usamos lo que aprendimos de OpenCV
  (rows,cols,channels) = cv_image.shape
  cv2.imshow("Ventana", cv_image)
  cv2.waitKey(3)

  
def main(args):
  rospy.init_node('nodoOCV', anonymous=True)
  image_sub = rospy.Subscriber("/usb_cam/image_raw",Image, image_callback)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Salir")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)  
             
   
