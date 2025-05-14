import cv2
import mediapipe as mp
import pyautogui

# Initialize camera
cam = cv2.VideoCapture(0)

# Initialize FaceMesh with iris tracking enabled
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True
)

# Get screen size for pyautogui scaling
screen_w, screen_h = pyautogui.size()

# Blink state tracker
blinked = False  # Tracks whether a blink just occurred

while True:
    success, frame = cam.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_h, frame_w, _ = frame.shape

    result = face_mesh.process(rgb_frame)
    landmark_points = result.multi_face_landmarks

    if landmark_points:
        landmarks = landmark_points[0].landmark

        # 1. Pointer control using right iris (landmark 474)
        iris_landmark = landmarks[474]
        x = int(iris_landmark.x * frame_w)
        y = int(iris_landmark.y * frame_h)
        screen_x = int(iris_landmark.x * screen_w)
        screen_y = int(iris_landmark.y * screen_h)
        pyautogui.moveTo(screen_x, screen_y)
        cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

        # 2. Blink detection using left eye landmarks 145 and 159
        upper_lid = landmarks[145]
        lower_lid = landmarks[159]

        x1 = int(upper_lid.x * frame_w)
        y1 = int(upper_lid.y * frame_h)
        x2 = int(lower_lid.x * frame_w)
        y2 = int(lower_lid.y * frame_h)

        cv2.circle(frame, (x1, y1), 4, (0, 255, 255), -1)
        cv2.circle(frame, (x2, y2), 4, (0, 255, 255), -1)

        # Calculate vertical eye opening distance
        eye_opening = abs(upper_lid.y - lower_lid.y)

        # Detect blink (eye closed)
        if eye_opening < 0.015:
            if not blinked:
                blinked = True  # Blink just started
                pyautogui.click()
                cv2.putText(frame, "Blink Detected", (30, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                print("Blink Detected")
        else:
            blinked = False  # Eye is open again, reset for next blink

    # Show video feed
    cv2.imshow('Eye Controlled Mouse', frame)

    # Exit on ESC key
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Cleanup
cam.release()
cv2.destroyAllWindows()
