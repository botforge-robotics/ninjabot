#!/usr/bin/env python3
from turtle import left
import rospy
from ninjabot_msgs.msg import Ws2812b_strip
from ninjabot_msgs.msg import Ws2812b
from ninjabot_msgs.msg import Focus_lights
from ninjabot_msgs.msg import Eyes
from sensor_msgs.msg import Joy
import time

global axes_clicked, btn_clicked, animations, eyes, color, max_color, current_eye, current_animation, body_led_on, focus_light_on, body_strip_msg, left_side_led_msg, right_side_led_msg, focusLight_msg, eyes_msg, anim_reverse, min_time, max_time, time_change_steps, anim_time

axes_clicked = [False, False, False, False, False, False, False, False]
btn_clicked = [False, False, False, False,
               False, False, False, False, False, False]
# steady        1
# dimming       2
# flow n cut    3
# hue flow      4
# rainbow flow  5
animations = [1, 2, 3, 4, 5]
animations_signal =[1,3,1,3,1]
eyes = ["neutral", "left", "right", "evil", "broad"]
color = 255
max_color = 1536
current_eye = 0
current_animation = 0
anim_time = 10

min_time = 2
max_time = 30
time_change_steps = 2

body_led_on = False
focus_light_on = False
anim_reverse = False
body_strip_msg = Ws2812b_strip()
left_side_led_msg = Ws2812b()
right_side_led_msg = Ws2812b()
focusLight_msg = Focus_lights()
eyes_msg = Eyes()


# focus light
focusLight_msg.right_light = False
focusLight_msg.left_light = False


def pub_left_Signal():
    #  Neo pixels default msg
    #  left
    left_side_led_msg.animation = animations_signal[current_animation]
    left_side_led_msg.h = 255
    left_side_led_msg.s = 255
    left_side_led_msg.v = 255
    left_side_led_msg.t = 3
    left_side_led_msg.reverse = False
    left_led_pub.publish(left_side_led_msg)
    # right
    right_side_led_msg.animation = animations_signal[current_animation]
    right_side_led_msg.h = 255
    right_side_led_msg.s = 255
    right_side_led_msg.v = 0
    right_side_led_msg.t = 3
    right_side_led_msg.reverse = False
    right_led_pub.publish(right_side_led_msg)
    # body
    body_strip_msg.global_anim = False
    body_strip_msg.body.animation = animations_signal[current_animation]
    body_strip_msg.body.h = 255
    body_strip_msg.body.s = 255
    body_strip_msg.body.v = 0
    body_strip_msg.body.t = 3
    body_strip_msg.body.reverse = False
    # font
    body_strip_msg.front.animation = animations_signal[current_animation]
    body_strip_msg.front.h = 255
    body_strip_msg.front.s = 255
    body_strip_msg.front.v = 0
    body_strip_msg.front.t = 3
    body_strip_msg.front.reverse=False
    #  rear
    body_strip_msg.rear.animation = animations_signal[current_animation]
    body_strip_msg.rear.h = 255
    body_strip_msg.rear.s = 255
    body_strip_msg.rear.v = 0
    body_strip_msg.rear.t = 3
    body_strip_msg.rear.reverse=False
    # left
    body_strip_msg.left.animation = animations_signal[current_animation]
    body_strip_msg.left.h = 255
    body_strip_msg.left.s = 255
    body_strip_msg.left.v = 0
    body_strip_msg.left.t = 3
    body_strip_msg.left.reverse=False
    # right
    body_strip_msg.right.animation = animations_signal[current_animation]
    body_strip_msg.right.h = 255
    body_strip_msg.right.s = 255
    body_strip_msg.right.v = 0
    body_strip_msg.right.t = 3
    body_strip_msg.right.reverse=False
    #  front_left
    body_strip_msg.front_left.animation = animations_signal[current_animation]
    body_strip_msg.front_left.h = 255
    body_strip_msg.front_left.s = 255
    body_strip_msg.front_left.v = 255
    body_strip_msg.front_left.t = 3
    body_strip_msg.front_left.reverse = False
    #  front_right
    body_strip_msg.front_right.animation = animations_signal[current_animation]
    body_strip_msg.front_right.h = 255
    body_strip_msg.front_right.s = 255
    body_strip_msg.front_right.v = 0
    body_strip_msg.front_right.t = 3
    body_strip_msg.front_right.reverse=False
    #  rear_left
    body_strip_msg.rear_left.animation = animations_signal[current_animation]
    body_strip_msg.rear_left.h = 255
    body_strip_msg.rear_left.s = 255
    body_strip_msg.rear_left.v = 255
    body_strip_msg.rear_left.t = 3
    body_strip_msg.rear_left.reverse=True
    # rear_right
    body_strip_msg.rear_right.animation = animations_signal[current_animation]
    body_strip_msg.rear_right.h = 255
    body_strip_msg.rear_right.s = 255
    body_strip_msg.rear_right.v = 0
    body_strip_msg.rear_right.t = 3
    body_strip_msg.rear_right.reverse=False
    body_led_pub.publish(body_strip_msg)


def pub_right_Signal():
    left_side_led_msg.animation = animations_signal[current_animation]
    left_side_led_msg.h = 255
    left_side_led_msg.s = 255
    left_side_led_msg.v = 0
    left_side_led_msg.t = 3
    left_side_led_msg.reverse = False
    left_led_pub.publish(left_side_led_msg)
    # right
    right_side_led_msg.animation = animations_signal[current_animation]
    right_side_led_msg.h = 255
    right_side_led_msg.s = 255
    right_side_led_msg.v = 255
    right_side_led_msg.t = 3
    right_side_led_msg.reverse = False
    right_led_pub.publish(right_side_led_msg)
    # body
    body_strip_msg.global_anim = False
    body_strip_msg.body.animation = animations_signal[current_animation]
    body_strip_msg.body.h = 255
    body_strip_msg.body.s = 255
    body_strip_msg.body.v = 0
    body_strip_msg.body.t = 3
    body_strip_msg.body.reverse = False
    # font
    body_strip_msg.front.animation = animations_signal[current_animation]
    body_strip_msg.front.h = 255
    body_strip_msg.front.s = 255
    body_strip_msg.front.v = 0
    body_strip_msg.front.t = 3
    body_strip_msg.front.reverse=False
    #  rear
    body_strip_msg.rear.animation = animations_signal[current_animation]
    body_strip_msg.rear.h = 255
    body_strip_msg.rear.s = 255
    body_strip_msg.rear.v = 0
    body_strip_msg.rear.t = 3
    body_strip_msg.rear.reverse=False
    # left
    body_strip_msg.left.animation = animations_signal[current_animation]
    body_strip_msg.left.h = 255
    body_strip_msg.left.s = 255
    body_strip_msg.left.v = 0
    body_strip_msg.left.t = 3
    body_strip_msg.left.reverse=False
    # right
    body_strip_msg.right.animation = animations_signal[current_animation]
    body_strip_msg.right.h = 255
    body_strip_msg.right.s = 255
    body_strip_msg.right.v = 0
    body_strip_msg.right.t = 3
    body_strip_msg.right.reverse=False
    #  front_left
    body_strip_msg.front_left.animation = animations_signal[current_animation]
    body_strip_msg.front_left.h = 255
    body_strip_msg.front_left.s = 255
    body_strip_msg.front_left.v = 0
    body_strip_msg.front_left.t = 3
    body_strip_msg.front_left.reverse = False
    #  front_right
    body_strip_msg.front_right.animation = animations_signal[current_animation]
    body_strip_msg.front_right.h = 255
    body_strip_msg.front_right.s = 255
    body_strip_msg.front_right.v = 255
    body_strip_msg.front_right.t = 3
    body_strip_msg.front_right.reverse=True
    #  rear_left
    body_strip_msg.rear_left.animation = animations_signal[current_animation]
    body_strip_msg.rear_left.h = 255
    body_strip_msg.rear_left.s = 255
    body_strip_msg.rear_left.v = 0
    body_strip_msg.rear_left.t = 3
    body_strip_msg.rear_left.reverse=False
    # rear_right
    body_strip_msg.rear_right.animation = animations_signal[current_animation]
    body_strip_msg.rear_right.h = 255
    body_strip_msg.rear_right.s = 255
    body_strip_msg.rear_right.v = 255
    body_strip_msg.rear_right.t = 3
    body_strip_msg.rear_right.reverse=False
    body_led_pub.publish(body_strip_msg)


def pub_body_msg():
    body_strip_msg.global_anim = True
    body_strip_msg.body.animation = animations[current_animation]
    body_strip_msg.body.h = color
    body_strip_msg.body.s = 255
    body_strip_msg.body.v = 255
    body_strip_msg.body.t = anim_time
    body_strip_msg.body.reverse = anim_reverse
    body_led_pub.publish(body_strip_msg)
    left_side_led_msg.animation = animations[current_animation]
    left_side_led_msg.h = color
    left_side_led_msg.s = 255
    left_side_led_msg.v = 255
    left_side_led_msg.t = anim_time
    left_side_led_msg.reverse = anim_reverse
    left_led_pub.publish(left_side_led_msg)
    right_side_led_msg.animation = animations[current_animation]
    right_side_led_msg.h = color
    right_side_led_msg.s = 255
    right_side_led_msg.v = 255
    right_side_led_msg.t = anim_time
    right_side_led_msg.reverse = anim_reverse
    right_led_pub.publish(right_side_led_msg)

def turn_off_strips():
    body_strip_msg.global_anim = True
    body_strip_msg.body.animation = 1
    body_strip_msg.body.h = 0
    body_strip_msg.body.s = 0
    body_strip_msg.body.v = 0
    body_strip_msg.body.t = 10
    body_strip_msg.body.reverse = anim_reverse
    body_led_pub.publish(body_strip_msg)
    left_side_led_msg.animation = 1
    left_side_led_msg.h = 0
    left_side_led_msg.s = 0
    left_side_led_msg.v = 0
    left_side_led_msg.t = 10
    left_side_led_msg.reverse = anim_reverse
    left_led_pub.publish(left_side_led_msg)
    right_side_led_msg.animation = 1
    right_side_led_msg.h = 0
    right_side_led_msg.s = 0
    right_side_led_msg.v = 0
    right_side_led_msg.t = 10
    right_side_led_msg.reverse = anim_reverse
    right_led_pub.publish(right_side_led_msg)

def joy_callback(data):
    global axes_clicked, btn_clicked, animations, eyes, color, max_color, current_eye, current_animation, body_led_on, focus_light_on, body_strip_msg, left_side_led_msg, right_side_led_msg, focusLight_msg, eyes_msg, anim_reverse, min_time, max_time, anim_time, time_change_steps

    # axes loop through
    # change color
    if (data.axes[2] == -1 and not axes_clicked[2]):
        axes_clicked[2] = True
        if (body_led_on):
            color += 255
            if (color > max_color):
                color = 255
            pub_body_msg()
            rospy.loginfo("change color to " + str(color))
    elif (data.axes[2] == 1 and axes_clicked[2]):
        axes_clicked[2] = False
    # change animation
    if (data.axes[5] == -1 and not axes_clicked[5]):
        axes_clicked[5] = True
        if (data.buttons[4] == 1):
            current_animation += 1
            if (current_animation >= len(animations)-1):
                current_animation = 0
            pub_left_Signal()
            rospy.loginfo("change left signal animation to " +
                          str(animations[current_animation]))
        elif (data.buttons[5] == 1):
            current_animation += 1
            if (current_animation >= len(animations)-1):
                current_animation = 0
            pub_right_Signal()
            rospy.loginfo("change right signal animation to " +
                          str(animations[current_animation]))
        elif (body_led_on):
            current_animation += 1
            if (current_animation > len(animations)-1):
                current_animation = 0
            pub_body_msg()
            rospy.loginfo("change body animation to " +
                          str(animations[current_animation]))
    elif (data.axes[5] == 1 and axes_clicked[5]):
        axes_clicked[5] = False

    # increase time
    if (data.axes[6] == -1 and not axes_clicked[6]):
        axes_clicked[6] = True
        if (body_led_on):
            anim_time += time_change_steps
            if (anim_time >= max_time):
                anim_time = max_time
            pub_body_msg()
            rospy.loginfo(
                "increasing body animation time to " + str(anim_time))
    elif (data.axes[6] == 1 and not axes_clicked[6]):
        axes_clicked[6] = True
        if (body_led_on):
            anim_time -= time_change_steps
            if (anim_time <= min_time):
                anim_time = min_time
            pub_body_msg()
            rospy.loginfo(
                "decreasing body animation time to " + str(anim_time))
    elif (data.axes[6] == 0 and axes_clicked[6]):
        axes_clicked[6] = False
    # change eyes and anim reverse
    if (data.axes[7] == -1 and not axes_clicked[7]):
        axes_clicked[7] = True
        current_eye += 1
        if (current_eye >= len(eyes)):
            current_eye = 0
        rospy.loginfo("change eyes to " + eyes[current_eye])
        eyes_msg.type = eyes[current_eye]
        eyes_pub.publish(eyes_msg)
    elif (data.axes[7] == 1 and not axes_clicked[7]):
        axes_clicked[7] = True
        if (anim_reverse):
            if (body_led_on):
                anim_reverse = False
                pub_body_msg()
                rospy.loginfo("anim forward")
        else:
            if (body_led_on):
                anim_reverse = True
                pub_body_msg()
                rospy.loginfo("anim reverse")
    elif (data.axes[7] == 0 and axes_clicked[7]):
        axes_clicked[7] = False

    # buttons loop through
    # Focus lights
    if (data.buttons[2] == 1 and not btn_clicked[2]):
        btn_clicked[2] = True
        if (focus_light_on):
            focus_light_on = False
            rospy.loginfo("focus light off")
            focusLight_msg.right_light = False
            focusLight_msg.left_light = False
            focus_light_pub.publish(focusLight_msg)
        else:
            focus_light_on = True
            rospy.loginfo("focus light on")
            focusLight_msg.right_light = True
            focusLight_msg.left_light = True
            focus_light_pub.publish(focusLight_msg)
    elif (data.buttons[2] == 0 and btn_clicked[2]):
        btn_clicked[2] = False

    # full body animation
    if (data.buttons[3] == 1 and not btn_clicked[3]):
        btn_clicked[3] = True
        if (body_led_on):
            body_led_on = False
            turn_off_strips()
            rospy.loginfo("body animation off")
        else:
            body_led_on = True
            pub_body_msg()
            rospy.loginfo("body animation on")
    elif (data.buttons[3] == 0 and btn_clicked[3]):
        btn_clicked[3] = False
    # right signal
    if (data.buttons[5] == 1 and not btn_clicked[5]):
        btn_clicked[5] = True
        if (current_animation >= len(animations)-1):
            current_animation = 0
        body_led_on = False
        pub_right_Signal()
        rospy.loginfo("right signal on")
    elif (data.buttons[5] == 0 and btn_clicked[5]):
        btn_clicked[5] = False
        turn_off_strips()
        rospy.loginfo("right signal off")
    # left signal
    if (data.buttons[4] == 1 and not btn_clicked[4]):
        btn_clicked[4] = True
        if (current_animation >= len(animations)-1):
            current_animation = 0
        body_led_on = False
        pub_left_Signal()
        rospy.loginfo("left signal on")
    elif (data.buttons[4] == 0 and btn_clicked[4]):
        btn_clicked[4] = False
        turn_off_strips()
        rospy.loginfo("left signal off")


def main():
    rospy.init_node('ninjabot_joy_node', anonymous=True)
    rate = rospy.Rate(20)  # 10hz
    while not rospy.is_shutdown():

        rate.sleep()


if __name__ == '__main__':
    body_led_pub = rospy.Publisher(
        '/ninjabot/body_strip', Ws2812b_strip, queue_size=10)
    left_led_pub = rospy.Publisher(
        '/ninjabot/left_strip', Ws2812b, queue_size=10)
    right_led_pub = rospy.Publisher(
        '/ninjabot/right_strip', Ws2812b, queue_size=10)
    focus_light_pub = rospy.Publisher(
        '/ninjabot/focus_lights', Focus_lights, queue_size=10)
    eyes_pub = rospy.Publisher('/ninjabot/eyes', Eyes, queue_size=10)
    joy_sub = rospy.Subscriber('/joy', Joy, joy_callback)

    try:
        main()
    except rospy.ROSInterruptException:
        pass
