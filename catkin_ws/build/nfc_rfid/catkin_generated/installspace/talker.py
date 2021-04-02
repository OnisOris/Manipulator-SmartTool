#!/usr/bin/env python3
# -*- coding: utf8 -*-
## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from std_msgs.msg import String

import RPi.GPIO as GPIO
import MFRC522
import signal
import os

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    # Create an object of the class MFRC522
    MIFAREReader = MFRC522.MFRC522()

    # Welcome message
    print("Welcome to the MFRC522 data read example")

    # This loop keeps checking for chips. If one is near it will get the UID and authenticate
    # Scan for cards    
    while not rospy.is_shutdown():
        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

        # If a card is found
        if status == MIFAREReader.MI_OK:
            print("Card detected")

        # Get the UID of the card
        (status,uid) = MIFAREReader.MFRC522_Anticoll()

        # If we have the UID, continue
        if status == MIFAREReader.MI_OK:

            # Print UID
            str_uid = "Card read UID: %s%s%s%s" % (uid[0], uid[1], uid[2], uid[3])
            rospy.loginfo(str_uid)
            pub.publish(str_uid)
            #print("Card read UID: %s%s%s%s" % (uid[0], uid[1], uid[2], uid[3]))

            # This is the default key for authentication
            key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]

            # Select the scanned tag
            MIFAREReader.MFRC522_SelectTag(uid)

            # Authenticate
            status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

        rate.sleep()

if __name__ == '__main__':
    try:
        print(os.path.abspath(__file__))
        talker()
    except rospy.ROSInterruptException:
        print("Ending read.")
    finally:
        GPIO.cleanup()
