# arm_robot.py. UPDATE IP AND PORT NUMBER

from fanucpy import Robot

def connect_to_fanuc():
    robot = Robot(
        robot_model="Fanuc",
        host="localhost",
        port=18735,
        ee_DO_type="RDO",
        ee_DO_num=7,
    )
    robot.connect()
    return robot
