#!/usr/bin/env python3

import socket
import netifaces as ni
import rospy
from ninjabot_msgs.msg import Lcd
from ninjabot_msgs.msg import Ws2812b_strip
from ninjabot_msgs.msg import Ws2812b
from ninjabot_msgs.msg import Focus_lights
import time
def main():
    lcd_pub = rospy.Publisher('/ninjabot/lcd', Lcd, queue_size=10)
    body_led_pub = rospy.Publisher('/ninjabot/body_strip', Ws2812b_strip, queue_size=10)
    left_led_pub = rospy.Publisher('/ninjabot/left_strip', Ws2812b, queue_size=10)
    right_led_pub = rospy.Publisher('/ninjabot/right_strip', Ws2812b, queue_size=10)
    focus_light_pub = rospy.Publisher('/ninjabot/focus_lights', Focus_lights, queue_size=10)
    rospy.init_node('initializer_node', anonymous=True)
    global ip
    connected = False
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        # wait until topics available
        if not connected:
            for topic in rospy.get_published_topics():
                if "/ninjabot/rightWheelSpeed" == topic[0]:
                    connected = True
        else:
            time.sleep(2)
            ip="local conn."
            try:
                ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
            except:
                ip="local conn."
            hostName = socket.gethostname()
            # publish host name and ip to lcd
            lcdMsg = Lcd()
            lcdMsg.message = str(hostName)
            lcdMsg.row = 0
            lcd_pub.publish(lcdMsg)
            lcdMsg.message = str(ip)
            lcdMsg.row = 1
            lcd_pub.publish(lcdMsg)

            # default leds animation after robot initialized
            body_strip_msg = Ws2812b_strip()
            side_leds_msg = Ws2812b()
            body_strip_msg.global_anim = True
            body_strip_msg.body.h =0
            body_strip_msg.body.s = 0
            body_strip_msg.body.v =0
            body_strip_msg.body.t =10
            body_strip_msg.body.animation = 1
            body_strip_msg.body.reverse = False
            
            side_leds_msg.h =0
            side_leds_msg.s = 0
            side_leds_msg.v =0
            side_leds_msg.t =10
            side_leds_msg.animation = 1
            side_leds_msg.reverse = False

            body_led_pub.publish(body_strip_msg)
            left_led_pub.publish(side_leds_msg)
            right_led_pub.publish(side_leds_msg)

            # focus light
            focusLight_msg = Focus_lights()
            focusLight_msg.right_light =False
            focusLight_msg.left_light = False 
            focus_light_pub.publish(focusLight_msg)
            
            # shutdown this node
            rospy.signal_shutdown("initialized")
        rate.sleep()
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
