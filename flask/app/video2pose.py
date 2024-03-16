import time
from pose2fbx import notifyPose2Fbx

def startVideo2Pose(id, type):
    print(f"############ Starting Video2Pose for {id} and {type}")
    time.sleep(3)
    print("############ Pose Estimation created")
    notifyPose2Fbx(id, type)
    