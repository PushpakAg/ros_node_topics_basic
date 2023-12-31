#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("Received Data: %s",data.data)

def listener():
    rospy.init_node("Subscriber_Node",anonymous=True)
    rospy.Subscriber("talking_topic_2",String,callback)
    rospy.spin()
if __name__ == "__main__":
    try:
        listener()
    except rospy.ROSInterruptException:
        pass