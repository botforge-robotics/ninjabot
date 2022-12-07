#!/usr/bin/env python3

import socket
import netifaces as ni
import rospy
from ninjabot_msgs.msg import Lcd
from ninjabot_msgs.msg import Ws2812b_strip
from ninjabot_msgs.msg import Ws2812b
from ninjabot_msgs.msg import Focus_lights
from sensor_msgs.msg import Imu, MagneticField, Temperature
from std_msgs.msg import String
import time

import math
from mpu9250_jmdev.registers import *
from mpu9250_jmdev.mpu_9250 import MPU9250

G = 9.80665
MagFieldConversion_uT_T = 0.000001

##################################################
# Create                                         #
##################################################

mpu = MPU9250(
    address_ak=AK8963_ADDRESS,
    address_mpu_master=MPU9050_ADDRESS_68,  # In 0x68 Address
    address_mpu_slave=None,
    bus=1,
    gfs=GFS_1000,
    afs=AFS_8G,
    mfs=AK8963_BIT_16,
    mode=AK8963_MODE_C100HZ)

##################################################
# Configure                                      #
##################################################
mpu.configure()  # Apply the settings to the registers.


def main():
    lcd_pub = rospy.Publisher('/ninjabot/lcd', Lcd, queue_size=10)
    body_led_pub = rospy.Publisher(
        '/ninjabot/body_strip', Ws2812b_strip, queue_size=10)
    left_led_pub = rospy.Publisher(
        '/ninjabot/left_strip', Ws2812b, queue_size=10)
    right_led_pub = rospy.Publisher(
        '/ninjabot/right_strip', Ws2812b, queue_size=10)
    focus_light_pub = rospy.Publisher(
        '/ninjabot/focus_lights', Focus_lights, queue_size=10)
    imu_pub = rospy.Publisher('imu/data_raw', Imu, queue_size=10)
    mag_pub = rospy.Publisher('imu/mag', MagneticField, queue_size=10)
    temp_pub = rospy.Publisher('imu/temperature', Temperature, queue_size=10)
    rospy.init_node('initializer_node', anonymous=True)
    imu_msg = Imu()
    mag_msg = MagneticField()
    temprature_msg = Temperature()
    global ip
    connected = False
    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        # wait until topics available
        if not connected:
            for topic in rospy.get_published_topics():
                if "/ninjabot/rightWheelSpeed" == topic[0]:
                    connected = True
        else:
            time.sleep(2)
            ip = "local conn."
            try:
                ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
            except:
                ip = "local conn."
            hostName = socket.gethostname()

            # default leds animation after robot initialized
            body_strip_msg = Ws2812b_strip()
            side_leds_msg = Ws2812b()
            body_strip_msg.global_anim = True
            body_strip_msg.body.h = 0
            body_strip_msg.body.s = 0
            body_strip_msg.body.v = 0
            body_strip_msg.body.t = 10
            body_strip_msg.body.animation = 1
            body_strip_msg.body.reverse = False

            side_leds_msg.h = 0
            side_leds_msg.s = 0
            side_leds_msg.v = 0
            side_leds_msg.t = 10
            side_leds_msg.animation = 1
            side_leds_msg.reverse = False

            body_led_pub.publish(body_strip_msg)
            left_led_pub.publish(side_leds_msg)
            right_led_pub.publish(side_leds_msg)

            # focus light
            focusLight_msg = Focus_lights()
            focusLight_msg.right_light = False
            focusLight_msg.left_light = False
            focus_light_pub.publish(focusLight_msg)

            ##################################################
            # Calibrate                                      #
            ##################################################
            lcdMsg = Lcd()
            lcdMsg.message = str(hostName)
            lcdMsg.row = 0
            lcd_pub.publish(lcdMsg)
            lcdMsg.message = "Calibrating IMU"
            lcdMsg.row = 1
            lcd_pub.publish(lcdMsg)
            mpu.calibrate()  # Calibrate sensors
            # The calibration function resets the sensors, so you need to reconfigure them
            mpu.configure()

            # publish host name and ip to lcd
            lcdMsg.message = str(ip)
            lcdMsg.row = 1
            lcd_pub.publish(lcdMsg)
            # shutdown this node
            # rospy.signal_shutdown("initialized")
            while not rospy.is_shutdown():
                mx, my, mz = mpu.readMagnetometerMaster()
                mag_msg.header.stamp = rospy.get_rostime()
                mag_msg.magnetic_field.x = mx*MagFieldConversion_uT_T
                mag_msg.magnetic_field.y = my*MagFieldConversion_uT_T
                mag_msg.magnetic_field.z = mz*MagFieldConversion_uT_T
                # mag_msg.magnetic_field_covariance[0] = 0.01
                # mag_msg.magnetic_field_covariance[4] = 0.01
                # mag_msg.magnetic_field_covariance[8] = 0.01

                # create imu msg
                q0 = 1.0  # W
                q1 = 0.0  # X
                q2 = 0.0  # Y
                q3 = 0.0  # Z

                # Fill imu message
                imu_msg.header.stamp = rospy.get_rostime()
                imu_msg.header.frame_id = 'imu_link_1'

                imu_msg.orientation.x = q0
                imu_msg.orientation.y = q1
                imu_msg.orientation.z = q2
                imu_msg.orientation.w = q3
                # imu_msg.orientation_covariance[0] = 0.01
                # imu_msg.orientation_covariance[4] = 0.01
                # imu_msg.orientation_covariance[8] = 0.01

                gx, gy, gz = mpu.readGyroscopeMaster()
                imu_msg.angular_velocity.x = math.radians(gx)
                imu_msg.angular_velocity.y = math.radians(gy)
                imu_msg.angular_velocity.z = math.radians(gz)
                # imu_msg.angular_velocity_covariance[0] = 0.03
                # imu_msg.angular_velocity_covariance[4] = 0.03
                # imu_msg.angular_velocity_covariance[8] = 0.03

                ax, ay, az = mpu.readAccelerometerMaster()
                imu_msg.linear_acceleration.x = ax*G
                imu_msg.linear_acceleration.y = ay*G
                imu_msg.linear_acceleration.z = az*G
                # imu_msg.linear_acceleration_covariance[0] = 10
                # imu_msg.linear_acceleration_covariance[4] = 10
                # imu_msg.linear_acceleration_covariance[8] = 10

                temprature_msg.header.frame_id = 'imu_link_1'
                temprature_msg.temperature = mpu.readTemperatureMaster()
                temprature_msg.header.stamp = rospy.get_rostime()

                temp_pub.publish(temprature_msg)
                imu_pub.publish(imu_msg)
                mag_pub.publish(mag_msg)
                rate.sleep()
        rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass