#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def cb(message):

    if message.data%3 ==0:
        print("1")

    elif message.data%3 !=0:
        print("1")

if __name__ == '__main__':
    rospy.init_node('twice')
    sub = rospy.Subscriber('count_up', Int32, cb)
    #pub = rospy.Publisher('twice', Int32, queue_size=1)
    #rate = rospy.Rate(10)
    rospy.spin()
