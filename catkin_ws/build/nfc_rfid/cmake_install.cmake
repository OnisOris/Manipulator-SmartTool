# Install script for directory: /home/pi/Desktop/Manipulator-SmartTool/catkin_ws/src/nfc_rfid

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/pi/Desktop/Manipulator-SmartTool/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/pi/Desktop/Manipulator-SmartTool/catkin_ws/build/nfc_rfid/catkin_generated/installspace/nfc_rfid.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/nfc_rfid/cmake" TYPE FILE FILES
    "/home/pi/Desktop/Manipulator-SmartTool/catkin_ws/build/nfc_rfid/catkin_generated/installspace/nfc_rfidConfig.cmake"
    "/home/pi/Desktop/Manipulator-SmartTool/catkin_ws/build/nfc_rfid/catkin_generated/installspace/nfc_rfidConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/nfc_rfid" TYPE FILE FILES "/home/pi/Desktop/Manipulator-SmartTool/catkin_ws/src/nfc_rfid/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/nfc_rfid" TYPE PROGRAM FILES "/home/pi/Desktop/Manipulator-SmartTool/catkin_ws/build/nfc_rfid/catkin_generated/installspace/talker.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/nfc_rfid" TYPE PROGRAM FILES "/home/pi/Desktop/Manipulator-SmartTool/catkin_ws/build/nfc_rfid/catkin_generated/installspace/listener.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/nfc_rfid" TYPE PROGRAM FILES "/home/pi/Desktop/Manipulator-SmartTool/catkin_ws/build/nfc_rfid/catkin_generated/installspace/MFRC522.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/nfc_rfid" TYPE PROGRAM FILES "/home/pi/Desktop/Manipulator-SmartTool/catkin_ws/build/nfc_rfid/catkin_generated/installspace/talker_master.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/nfc_rfid" TYPE PROGRAM FILES "/home/pi/Desktop/Manipulator-SmartTool/catkin_ws/build/nfc_rfid/catkin_generated/installspace/listener_master.py")
endif()

