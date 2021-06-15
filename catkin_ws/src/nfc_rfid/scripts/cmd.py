import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    pub = rospy.Publisher('command_line', String, queue_size=10)
    rospy.init_node('sender', anonymous=True)

    print("Welcom to command line for SmartTool.")
    while True:
        command = input('-> ')
        if command == 'exit':
            break
        else:
            rospy.loginfo(command)
            pub.publish(command)
