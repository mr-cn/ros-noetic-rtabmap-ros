# Maintainer : ehmish
pkgdesc="ROS - RTAB-Maps ros-pkg."
url='http://www.ros.org/'

pkgname='ros-noetic-rtabmap-ros'
pkgver='0.21.1'
_pkgver_patch=1
arch=('any')
pkgrel=1
license=('BSD')

ros_makedepends=(ros-noetic-genmsg
  ros-noetic-class-loader
  ros-noetic-rtabmap
  ros-noetic-sensor-msgs
  ros-noetic-catkin
  ros-noetic-stereo-msgs
  ros-noetic-visualization-msgs
  ros-noetic-cv-bridge
  ros-noetic-nodelet
  ros-noetic-geometry-msgs
  ros-noetic-std-msgs
  ros-noetic-dynamic-reconfigure
  ros-noetic-image-geometry
  ros-noetic-std-srvs
  ros-noetic-eigen-conversions
  ros-noetic-nav-msgs
  ros-noetic-tf
  ros-noetic-rospy
  ros-noetic-octomap-ros
  ros-noetic-costmap-2d
  ros-noetic-image-transport
  ros-noetic-tf2-ros
  ros-noetic-message-filters
  ros-noetic-move-base-msgs
  ros-noetic-pcl-ros
  ros-noetic-roscpp
  ros-noetic-pcl-conversions
  ros-noetic-rviz
  ros-noetic-tf-conversions
  ros-noetic-laser-geometry)
makedepends=('cmake' 'ros-build-tools'
  ${ros_makedepends[@]}
  pcl)

ros_depends=(ros-noetic-class-loader
  ros-noetic-rtabmap
  ros-noetic-sensor-msgs
  ros-noetic-stereo-msgs
  ros-noetic-visualization-msgs
  ros-noetic-cv-bridge
  ros-noetic-nodelet
  ros-noetic-geometry-msgs
  ros-noetic-std-msgs
  ros-noetic-dynamic-reconfigure
  ros-noetic-image-geometry
  ros-noetic-std-srvs
  ros-noetic-eigen-conversions
  ros-noetic-nav-msgs
  ros-noetic-image-transport-plugins
  ros-noetic-tf
  ros-noetic-rospy
  ros-noetic-octomap-ros
  ros-noetic-costmap-2d
  ros-noetic-image-transport
  ros-noetic-tf2-ros
  ros-noetic-message-filters
  ros-noetic-move-base-msgs
  ros-noetic-pcl-ros
  ros-noetic-roscpp
  ros-noetic-pcl-conversions
  ros-noetic-rviz
  ros-noetic-tf-conversions
  ros-noetic-laser-geometry)
depends=(${ros_depends[@]})

# Git version (e.g. for debugging)
# _tag=release/noetic/rtabmap_ros/${pkgver}-${_pkgver_patch}
# _dir=${pkgname}
# source=("${_dir}"::"git+https://github.com/introlab/rtabmap_ros-release.git"#tag=${_tag})
# sha256sums=('SKIP')

# Tarball version (faster download)
_dir="rtabmap_ros-release-release-noetic-rtabmap_ros-${pkgver}-${_pkgver_patch}"
source=(
	"${pkgname}-${pkgver}-${_pkgver_patch}.tar.gz"::"https://github.com/introlab/rtabmap_ros-release/archive/release/noetic/rtabmap_ros/${pkgver}-${_pkgver_patch}.tar.gz"
	fix-python-scripts.sh	
)
sha256sums=(
	'9e151dbd9426cdb5fb5ce6df5c3af5134337453628265f34921f11f74672e6e9'
	'5528486d640d91136276edda2075aefc06f360e6297e556051bae57b9479aeda'
)

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/noetic/setup.bash ] && source /opt/ros/noetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  ${srcdir}/fix-python-scripts.sh -v 3 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/noetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python3 \
        -DPYTHON_LIBRARY=/usr/lib/libpython3.so \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make

}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}
