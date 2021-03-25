rospy.init_node("rfid_reader")
    pub = rospy.Publisher("rfid_data", String, queue_size=10)

    ser = serial.Serial('/dev/' + serial_device, baud_rate)
    rospy.loginfo("Node `rfid_reader` started.")
    while True:
        try:
            data = ser.readline()
            pub.publish(data)
        except KeyboardInterrupt, e:
            sys.exit(0)

