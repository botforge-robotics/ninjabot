#!/usr/bin/env python3
from ninjabot_launcher_api.srv import NinjabotApi, NinjabotApiResponse
import roslaunch
import rospy
import rospkg
r = rospkg.RosPack()
nav_launch_file = r.get_path('ninjabot_navigation') + \
    '/launch/ninjabot_navigation.launch'
real_nav_launch_file = r.get_path(
    'ninjabot_navigation') + '/launch/real_navigation.launch'
map_launch_file = r.get_path('ninjabot_mapping') + \
    '/launch/ninjabot_gmapping.launch'
map_saver_launch_file = r.get_path('ninjabot_mapping') + \
    '/launch/save_map.launch'
teleop_launch_file = r.get_path('ninjabot_teleop') + \
    '/launch/joy_control.launch'

uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
roslaunch.configure_logging(uuid)
global map_parent, start_map_launch_flag, stop_map_launch_flag, map_running, \
    nav_parent, start_nav_launch_flag, stop_nav_launch_flag, nav_running,\
    real_nav_parent, start_real_nav_launch_flag, stop_real_nav_launch_flag, real_nav_running,\
    teleop_parent, start_teleop_launch_flag, stop_teleop_launch_flag, teleop_running,\
    map_saver_parent, start_map_saver_launch_flag, stop_map_saver_launch_flag, map_saver_running
start_map_launch_flag = False
stop_map_launch_flag = False
map_running = False
start_map_saverlaunch_flag = False
stop_map_saver_launch_flag = False
map_saver_running = False
start_nav_launch_flag = False
stop_nav_launch_flag = False
nav_running = False
start_real_nav_launch_flag = False
stop_real_nav_launch_flag = False
real_nav_running = False
start_teleop_launch_flag = False
stop_teleop_launch_flag = False
teleop_running = False


def handleLauncherStart(req):
    global map_parent, start_map_launch_flag, map_running, \
        nav_parent, start_nav_launch_flag, nav_running,\
        real_nav_parent, start_real_nav_launch_flag, real_nav_running,\
        teleop_parent, start_teleop_launch_flag, teleop_running,\
        map_saver_parent, start_map_saver_launch_flag, map_saver_running
    if req.file == "map":
        if map_running:
            return NinjabotApiResponse(False)
        else:
            cli_args = [map_launch_file] + \
                str(req.args).split(" ")
            roslaunch_file = [
                (roslaunch.rlutil.resolve_launch_arguments(cli_args)[0], cli_args[1:])]
            map_parent = roslaunch.parent.ROSLaunchParent(uuid, roslaunch_file)
            start_map_launch_flag = True
            map_running = True
            return NinjabotApiResponse(True)
    elif req.file == "map_saver":
        if map_saver_running:
            return NinjabotApiResponse(False)
        else:
            cli_args = [map_saver_launch_file] + \
                str(req.args).split(" ")
            roslaunch_file = [
                (roslaunch.rlutil.resolve_launch_arguments(cli_args)[0], cli_args[1:])]
            map_saver_parent = roslaunch.parent.ROSLaunchParent(
                uuid, roslaunch_file)
            start_map_saver_launch_flag = True
            map_saver_running = True
            return NinjabotApiResponse(True)
    elif req.file == "nav":
        if nav_running:
            return NinjabotApiResponse(False)
        else:
            cli_args = [nav_launch_file] + \
                str(req.args).split(" ")
            roslaunch_file = [
                (roslaunch.rlutil.resolve_launch_arguments(cli_args)[0], cli_args[1:])]
            nav_parent = roslaunch.parent.ROSLaunchParent(uuid, roslaunch_file)
            start_nav_launch_flag = True
            nav_running = True
            return NinjabotApiResponse(True)
    elif req.file == "real_nav":
        if real_nav_running:
            return NinjabotApiResponse(False)
        else:
            cli_args = [real_nav_launch_file] + \
                str(req.args).split(" ")
            roslaunch_file = [
                (roslaunch.rlutil.resolve_launch_arguments(cli_args)[0], cli_args[1:])]
            real_nav_parent = roslaunch.parent.ROSLaunchParent(
                uuid, roslaunch_file)
            start_real_nav_launch_flag = True
            real_nav_running = True
            return NinjabotApiResponse(True)
    elif req.file == "teleop":
        if teleop_running:
            return NinjabotApiResponse(False)
        else:
            cli_args = [teleop_launch_file] + \
                str(req.args).split(" ")
            roslaunch_file = [
                (roslaunch.rlutil.resolve_launch_arguments(cli_args)[0], cli_args[1:])]
            teleop_parent = roslaunch.parent.ROSLaunchParent(
                uuid, roslaunch_file)
            start_teleop_launch_flag = True
            teleop_running = True
            return NinjabotApiResponse(True)


def handleLauncherStop(req):
    global stop_map_launch_flag, map_running, \
        stop_nav_launch_flag, nav_running,\
        stop_real_nav_launch_flag, real_nav_running,\
        stop_teleop_launch_flag, teleop_running,\
        stop_map_saver_launch_flag, map_saver_running
    if req.file == "map":
        if not map_running:
            return NinjabotApiResponse(False)
        else:
            stop_map_launch_flag = True
            map_running = False
            return NinjabotApiResponse(True)
    elif req.file == "map_saver":
        if not map_saver_running:
            return NinjabotApiResponse(False)
        else:
            stop_map_saver_launch_flag = True
            map_saver_running = False
            return NinjabotApiResponse(True)
    elif req.file == "nav":
        if not nav_running:
            return NinjabotApiResponse(False)
        else:
            stop_nav_launch_flag = True
            nav_running = False
            return NinjabotApiResponse(True)
    elif req.file == "real_nav":
        if not real_nav_running:
            return NinjabotApiResponse(False)
        else:
            stop_real_nav_launch_flag = True
            real_nav_running = False
            return NinjabotApiResponse(True)
    elif req.file == "teleop":
        if not teleop_running:
            return NinjabotApiResponse(False)
        else:
            stop_teleop_launch_flag = True
            teleop_running = False
            return NinjabotApiResponse(True)


def main():
    global map_parent, start_map_launch_flag, stop_map_launch_flag, \
        nav_parent, start_nav_launch_flag, stop_nav_launch_flag,\
        real_nav_parent, start_real_nav_launch_flag, stop_real_nav_launch_flag,\
        teleop_parent, start_teleop_launch_flag, stop_teleop_launch_flag,\
        map_saver_parent, start_map_saver_launch_flag, stop_map_saver_launch_flag
    rospy.init_node('ninjabot_launcher_api_server')
    rospy.Service('ninjabot_launcher_api_start',
                  NinjabotApi, handleLauncherStart)
    rospy.Service('ninjabot_launcher_api_stop',
                  NinjabotApi, handleLauncherStop)
    while not rospy.is_shutdown():
        if start_map_launch_flag:
            map_parent.start()
            start_map_launch_flag = False
        if stop_map_launch_flag:
            map_parent.shutdown()
            stop_map_launch_flag = False
        if start_map_saver_launch_flag:
            map_saver_parent.start()
            start_map_saver_launch_flag = False
        if stop_map_saver_launch_flag:
            map_saver_parent.shutdown()
            stop_map_saver_launch_flag = False
        if start_nav_launch_flag:
            nav_parent.start()
            start_nav_launch_flag = False
        if stop_nav_launch_flag:
            nav_parent.shutdown()
            stop_nav_launch_flag = False
        if start_real_nav_launch_flag:
            real_nav_parent.start()
            start_real_nav_launch_flag = False
        if stop_real_nav_launch_flag:
            real_nav_parent.shutdown()
            stop_real_nav_launch_flag = False
        if start_teleop_launch_flag:
            teleop_parent.start()
            start_teleop_launch_flag = False
        if stop_teleop_launch_flag:
            teleop_parent.shutdown()
            stop_teleop_launch_flag = False


if __name__ == "__main__":
    main()
