<!-- PROJECT SHIELDS -->

[![ROS][ros-shield]][ros-url] [![Contributors][contributors-shield]][contributors-url] [![Last Commit][last-commit-shield]][last-commit-url] [![Stargazers][stars-shield]][stars-url] [![Issues][issues-shield]][issues-url] [![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->

<div align="center">
<h3 align="center">NINJABOT</h3>
<h6 align="center">Autonomous Mobile Robot</h6>
 <a href="https://github.com/chaitanya-mandala/ninjabot">
    <img src="images/front.jpg" alt="Logo" height="180">
    <img src="images/back.jpg" alt="Logo" height="180">
    <img src="images/eyes.jpg" alt="Logo" height="180">
  </a>
</div>

</br>
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#simulation">Simulation</a>
      <ul>
        <li><a href="#setup">Setup</a></li>
        <li><a href="#gazebo">Gazebo</a></li>
        <li><a href="#rviz">Rviz</a></li>
        <li><a href="#teleop">Teleop</a></li>
        <li><a href="#slam">SLAM</a></li>
        <li><a href="#simulation-navigation">Navigation</a></li>
      </ul>
    </li>
    <li>
      <a href="#real-robot">Real Robot</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#ssh-connection">SSH connection local & wifi</a></li>
        <li><a href="#wifi">Add or remove wifi</a></li>
        <li><a href="#network-configuration"> Network configuration for robot & workstation</a></li>
        <li><a href="#real-rviz">Rviz</a></li>
        <li><a href="#real-teleop">Teleop</a></li>
        <li><a href="#real-mapping">Mapping</a></li>
        <li><a href="#real-navigation">Navigation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- Simulation -->

## Simulation

Ninjabot Gazebo simulation.

#### Setup

1. Clone the repo to ~/catkin_ws/src
   ```sh
   roscd && cd .. && cd src
   git clone https://github.com/chaitanya-mandala/ninjabot.git
   ```
2. Install ros dependency packages, Execute in ~/catkin_Ws
   ```sh
   cd ..
   rosdep install --from-paths src --ignore-src -r -y
   ```
3. Compile catkin workspace
   ```sh
   catkin_make
   ```

#### Gazebo

1. Ninjabot in empty world.

   ```sh
   roslaunch ninjabot_simulation gazebo.launch world:=empty
   ```

      <img align="center" src="images/gazebo_empty.png" alt="Logo" >
   <br></br>

2. Ninjabot in house.
   ```sh
   roslaunch ninjabot_simulation gazebo.launch world:=house
   ```
   <img align="center" src="images/gazebo_house.png" alt="Logo" >

#### Rviz

1. Launch Gazebo simulation.

2. Launching Rviz.
   ```sh
   roslaunch ninjabot_simulation rviz.launch
   ```
   <img align="center" src="images/gazebo_rviz.png" alt="Logo" >

#### Teleop

1. Keyboard Twist teleop.

```sh
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
```
keyboard commands to Move robo

```sh
Reading from the keyboard  and Publishing to Twist!
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .

q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%
anything else : stop

CTRL-C to quit
```
2. JoyStick Twist teleop.
```sh
roslaunch ninjabot_teleop joy_teleop.launch
```

3. Rqt robot steering
```sh
rosrun rqt_robot_steering rqt_robot_steering
```
<img align="center" src="images/rqt_robot_steering.png" alt="Logo" >
<!-- ROADMAP -->

### SLAM
1. Launch Gazebo simulation.
2. Launching SLAM mapping.
```sh
roslaunch ninjabot_mapping ninjabot_mapping.launch
```
move robo with twist teleop for mapping entire area.
<img align="center" src="images/slam.png" alt="Logo" >

3. Save map.
```sh
roslaunch ninjabot_mapping save_map.launch map_name:=<NEW_MAP_NAME>
```
New map will be saved in *catkin_ws/src/ninjabot/ninjabot_mapping/maps/* folder with given map_name. *<b>(Please give map name same as world name for easy convinence for launching navigation.)</b>*

eg:
```sh
roslaunch ninjabot_mapping save_map.launch map_name:=house
```

### Navigation
1. Close all gazebo and rviz windows.

2. Launch Navigation
```sh
roslaunch ninjabot_navigation ninjabot_navigation.launch world:=house
```
(world name is same for both gazebo world and map name)
<img align="center" src="images/navigation.png" alt="Logo" >

## Real-Robot
## Roadmap

- [ ] Add Sample Codes package
<!-- - [ ] Feature 3
  - [ ] Nested Feature -->

See the [open issues](https://github.com/chaitanya-mandala/ninjabot/issues) for a full list of proposed features (and known issues).

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<!-- CONTACT -->

## Contact

MNV Chaitanya Kumar - nagachaitanya948@gmail.com

Project Link: [https://github.com/chaitanya-mandala/ninjabot](https://github.com/chaitanya-mandala/ninjabot)

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

- []()
- []()
- []()

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/chaitanya-mandala/ninjabot.svg?style=for-the-badge
[contributors-url]: https://github.com/chaitanya-mandala/ninjabot/graphs/contributors
[last-commit-shield]: https://img.shields.io/github/last-commit/chaitanya-mandala/ninjabot/noetic.svg?style=for-the-badge
[last-commit-url]: https://github.com/chaitanya-mandala/ninjabot/commit/noetic
[stars-shield]: https://img.shields.io/github/stars/chaitanya-mandala/ninjabot.svg?style=for-the-badge
[stars-url]: https://github.com/chaitanya-mandala/ninjabot/stargazers
[issues-shield]: https://img.shields.io/github/issues/chaitanya-mandala/ninjabot.svg?style=for-the-badge
[issues-url]: https://github.com/chaitanya-mandala/ninjabot/issues
[license-shield]: https://img.shields.io/github/license/chaitanya-mandala/ninjabot.svg?style=for-the-badge
[license-url]: https://github.com/chaitanya-mandala/ninjabot/blob/master/LICENSE.txt
[ros-shield]: https://img.shields.io/badge/ROS-noetic-green?style=for-the-badge&logo=ros
[ros-url]: http://wiki.ros.org/noetic
[product-screenshot]: images/screenshot.png
