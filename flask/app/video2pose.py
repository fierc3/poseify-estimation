import time
from pose2fbx import notifyPose2Fbx
from error import errorQueue
import subprocess

def startVideo2Pose(id, type, user):
    print(f"############ Starting Video2Pose for {id} and {type}")
    try:
        command = f"bash -c 'cd poseestimation && python estimate_pose.py --dir /poseify/uploads --guid {id} --user-id {user}'"
        print('------------------------------')
        print('Starting the videopose3d process')
        print(command)
        print('------------------------------')
        p2 = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        print("Error occurred while executing the command:")
        print(e.returncode)  # This is the return code
        print("Standard Output:", e.stdout)  # This is the standard output
        print("Standard Error:", e.stderr)  # This is the standard error
        errorQueue(id, type, str(e))
    else:
        print("############ Pose Estimation created")
        notifyPose2Fbx(id, type)
    