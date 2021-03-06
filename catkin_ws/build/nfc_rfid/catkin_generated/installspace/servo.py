#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time, rospy
from std_msgs.msg import String

class Servo:

    def __init__(self, pin, freq):
        self.pin = pin
        self.freq = freq

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

        self.pwm = GPIO.PWM(self.pin, self.freq)
        self.pwm.start(0)
        self.is_Locked = False

    def turn_right(self, t):
        self.pwm.ChangeDutyCycle(6)
        time.sleep(t)
        self.pwm.ChangeDutyCycle(0)

    def turn_left(self, t):
        self.pwm.ChangeDutyCycle(8)
        time.sleep(t)
        self.pwm.ChangeDutyCycle(0)

    def setup(self):
        self.turn_right(0.5)

    def lock(self):
        self.turn_left(0.33)
        self.is_Locked = True
        return 'Locked.'

    def unlock(self):
        self.turn_right(0.35)
        self.is_Locked = False
        return 'Unlocked.'

def callback(data, servo):
    #uid = data.data
    #global prev_uid
    if not servo.is_Locked and not data.data == '0' and not data.data == 'Open':
        rospy.loginfo(data.data)
        time.sleep(10)
        servo.setup()
        rospy.loginfo(servo.lock())
    #    rospy.loginfo(servo.unlock())
    #    prev_uid = data.data
    #    print(prev_uid, uid)
    elif data.data == 'Open':
        rospy.loginfo(data.data)
        rospy.loginfo(servo.unlock())
        time.sleep(15)
    else:
        rospy.loginfo(data.data)

def listener(servo):
    rospy.init_node('servo', anonymous=True)
    rospy.Subscriber('chatter', String, callback, servo)
    rospy.spin()

if __name__ == "__main__":
    try:
        servo = Servo(17, 50)
        listener(servo)
    except rospy.ROSInterruptException:
        GPIO.cleanup()
    finally:
        GPIO.cleanup()
