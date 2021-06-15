#!/usr/bin/env python
## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

import rospy
from std_msgs.msg import String

prev_uid = '0'
is_Locked = False
def callback(data):
    global prev_uid
    global is_Locked

    pub = rospy.Publisher('command_line', String)
    rospy.loginfo(rospy.get_caller_id() + ' %s', data.data)
    if not data.data == '0' and not is_Locked:
        print(is_Locked)
        pub.publish('Close')
        is_Locked = True
        prev_uid = data.data

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('chatter', String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
