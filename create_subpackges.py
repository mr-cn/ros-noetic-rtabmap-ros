#!/usr/bin/env python3
import os

pkgver='0.21.1'
_pkgver_patch=4
ros_distro='noetic'

subpackages = [
    "conversions",
    "costmap_plugins",
    "demos",
    "examples",
    "launch",
    "legacy",
    "msgs",
    "odom",
    "python",
    #"ros",
    "rviz_plugins",
    "slam",
    "sync",
    "util",
    "viz",
]

# read template PKGBUILD
with open("PKGBUILD.template", "r") as f:
    template = f.read()

for package in subpackages:
    # delete if exists
    if os.path.exists("ros-{}-rtabmap-{}".format(ros_distro, package)):
        os.system("rm -rf ros-{}-rtabmap-{}".format(ros_distro, package))

    # create subpackage directory
    os.makedirs("ros-{}-rtabmap-{}".format(ros_distro, package))

    # copy script to directory
    os.system("cp fix-python-scripts.sh ros-{}-rtabmap-{}/".format(ros_distro, package))

    # replace template strings
    pkgbuild = template.replace("__TEMP_ROSDISTRO__", ros_distro)
    pkgbuild = pkgbuild.replace("__TEMP_SUBPKG__", package)
    pkgbuild = pkgbuild.replace("__TEMP_PKGVER__", pkgver)
    pkgbuild = pkgbuild.replace("__TEMP_PKGVER_PATCH__", str(_pkgver_patch))

    # create subpackage PKGBUILD
    with open("ros-{}-rtabmap-{}/PKGBUILD".format(ros_distro, package), "w") as f:
        f.write(pkgbuild)