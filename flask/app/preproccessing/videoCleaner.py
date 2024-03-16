import cv2
import mediapipe as mp
import math

def is_full_body_visible(pose_landmarks):
    required_landmarks = [
    mp_pose.PoseLandmark.NOSE,  # Head
    #mp_pose.PoseLandmark.LEFT_SHOULDER, mp_pose.PoseLandmark.RIGHT_SHOULDER,  # Shoulders
    
    #mp_pose.PoseLandmark.LEFT_WRIST, mp_pose.PoseLandmark.RIGHT_WRIST,  # Wrists
    #mp_pose.PoseLandmark.LEFT_HIP, mp_pose.PoseLandmark.RIGHT_HIP,  # Hips
    #mp_pose.PoseLandmark.LEFT_ANKLE, mp_pose.PoseLandmark.RIGHT_ANKLE  # Ankles
    ]
    for landmark_id in required_landmarks:
        landmark = pose_landmarks.landmark[landmark_id]
        # Check if the landmark is not visible or below visibility threshold
        if not (landmark.HasField('visibility') and landmark.visibility > 0.5):
            return False
    return True


# Initialize MediaPipe Pose.
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5)

# Open the video file.
cap = cv2.VideoCapture('/poseify/video/test.mp4')
frameRate = cap.get(cv2.CAP_PROP_FPS) 

# Prepare output video writer.
# Ensure the output path is accessible and writeable.
output_path = '/poseify/video/filteredtest.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Define codec.
out = cv2.VideoWriter(output_path, fourcc, frameRate, (int(cap.get(3)), int(cap.get(4))))
print(cap)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Process the frame with MediaPipe Pose.
    results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    if results.pose_landmarks and is_full_body_visible(results.pose_landmarks):  # Check if a body is detected.
        out.write(frame)  # Write the frame to the output video.

# Release resources.
cap.release()
out.release()

print("Video processing complete. The output is saved as:", output_path)




