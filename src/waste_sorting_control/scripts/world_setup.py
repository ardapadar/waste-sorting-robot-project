#!/usr/bin/env python3
import rospy
import moveit_commander
from geometry_msgs.msg import PoseStamped
import sys

def setup_world():
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('world_setup_node', anonymous=True)
    
    scene = moveit_commander.PlanningSceneInterface()
    rospy.sleep(2) # Sistemin bağlanması için kısa bir bekleme

    # 1. KONVEYÖR (Robotun tam önünde duran engel)
    conveyor_pose = PoseStamped()
    conveyor_pose.header.frame_id = "base_link"
    conveyor_pose.pose.position.x = 0.5  # Robotun önündeki mesafe
    conveyor_pose.pose.position.y = 0.0
    conveyor_pose.pose.position.z = 0.15 # Yükseklik
    scene.add_box("conveyor", conveyor_pose, size=(0.4, 1.0, 0.3))

    # 2. KUTULAR (Atıkların bırakılacağı yerler)
    # Örnek olarak bir kutu ekleyelim, yerini RViz'de görelim
    bin_pose = PoseStamped()
    bin_pose.header.frame_id = "base_link"
    bin_pose.pose.position.x = 0.0
    bin_pose.pose.position.y = 0.4  # Robotun sol tarafı
    bin_pose.pose.position.z = 0.1
    scene.add_box("waste_bin", bin_pose, size=(0.3, 0.3, 0.2))

    print("--- MOVEIT SAHNESI GÜNCELLENDI ---")
    print("Konveyör ve kutu engel olarak eklendi.")

if __name__ == '__main__':
    setup_world()
