# arm_robot.py

from fanucpy import Robot

def connect_to_fanuc():
    robot = Robot(
        robot_model="Fanuc",
        host="localhost",  # Update with the actual IP address
        port=18735,            # Update with the actual port
        ee_DO_type="RDO",
        ee_DO_num=7,
    )
    robot.connect()
    return robot
