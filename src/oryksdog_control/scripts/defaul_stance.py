#!/usr/bin/env python3
#Author: lyle

import rospy
from std_msgs.msg import Float64

rospy.init_node("Robot_Controller")
RATE = 60
command_topics = ["/oryksdog_controller/FR1_joint/command",
                  "/oryksdog_controller/FR2_joint/command",
                  "/oryksdog_controller/FR3_joint/command",
                  "/oryksdog_controller/FL1_joint/command",
                  "/oryksdog_controller/FL2_joint/command",
                  "/oryksdog_controller/FL3_joint/command",
                  "/oryksdog_controller/RR1_joint/command",
                  "/oryksdog_controller/RR2_joint/command",
                  "/oryksdog_controller/RR3_joint/command",
                  "/oryksdog_controller/RL1_joint/command",
                  "/oryksdog_controller/RL2_joint/command",
                  "/oryksdog_controller/RL3_joint/command"]
publishers = []
for i in range(len(command_topics)):
    publishers.append(rospy.Publisher(command_topics[i], Float64, queue_size = 0))

def set_stance():
    for i in range(len(command_topics)):
        publishers[i].publish(0.0)

if __name__ == '__main__':
    set_stance()