#!/usr/bin/env python3



from sensor_msgs.msg import Image
import cv2
import rospy
from cv_bridge import CvBridge, CvBridgeError

bridge = CvBridge()


def main():
	
#	video_capture = cv2.VideoCapture(0)
	video_capture = cv2.VideoCapture("/home/chaitu/Desktop/catkin_ws/src/ninjabot/ninjabot_control/src/raspberryPetDog.mp4")
	
  
	while(video_capture.isOpened()):
		ret,frame = video_capture.read()
		cv_image = bridge.cv2_to_imgmsg(frame, "bgr8")
	#	frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5)
		rospy.loginfo("----Reading the frame----")
		pub.publish(cv_image)
		rospy.loginfo("---publishing the frame----")
		rate.sleep()
		
		cv2.imshow('frame',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	
		
		

if __name__ == '__main__':
	
	rospy.init_node('tennis_ball_pub',anonymous=True)
	pub = rospy.Publisher("tennis_ball_image",Image,queue_size=10)
	rate =rospy.Rate(10)
	main()

cv2.waitKey(0)
cv2.destroyAllWindows()
