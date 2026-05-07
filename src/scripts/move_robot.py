#!/usr/bin/env python3
import sys
import rospy
import moveit_commander

def move_robot():
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('waste_robot_mover', anonymous=True)

    # Robotun planlama grubunu tanımlıyoruz
    group_name = "arm"
    move_group = moveit_commander.MoveGroupCommander(group_name)

    print("--- Robot Dik Konuma Gidiyor ---")
    move_group.set_named_target("home")
    move_group.go(wait=True)
    rospy.sleep(2)

    print("--- Atık Toplama Pozisyonuna Eğiliyor ---")
    joint_goal = move_group.get_current_joint_values()
    joint_goal[0] = 1.57 # Omuz 90 derece döner
    joint_goal[1] = -1.0 # Dirsek hafif bükülür

    move_group.go(joint_goal, wait=True)
    move_group.stop()
    print("--- Hareket Tamamlandı! ---")

if __name__ == '__main__':
    try:
        move_robot()
    except rospy.ROSInterruptException:
        pass
