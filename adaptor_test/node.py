#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import sys

def make_callback(topic_name):
    def callback(msg):
        rospy.loginfo(f"Received from {topic_name}: {msg.data}")
    return callback

if __name__ == "__main__":
    rospy.init_node("multi_topic_subscriber", anonymous=True)

    if len(sys.argv) < 2:
        rospy.logerr(f"Usage: {sys.argv[0]} <n_topics>")
        sys.exit(1)

    n_topics = int(sys.argv[1])
    subscribers = []

    for i in range(n_topics):
        rospy.loginfo(f"Starting topic {i}.")
        topic = f"/topic_{i}"
        subscribers.append(rospy.Subscriber(topic, String, make_callback(topic)))

    rospy.spin()
    rospy.loginfo("Spin complete.")
