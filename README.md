# 👁️ Eye-Controlled Mouse using Computer Vision

> **Control your mouse with your eyes. Blink to click. No hands needed.**  
> A real-time Python project using **MediaPipe**, **OpenCV**, and **PyAutoGUI** to turn your webcam into a hands-free mouse controller.
## 🚀 Features

- ✅ **Real-time iris tracking** for pointer control  
- ✅ **Blink detection** for click simulation  
- ✅ **Smooth pointer movement** for stability  
- ✅ **Configurable thresholds** for eye tracking and clicking  
- ✅ **FaceMesh + iris refinement** using MediaPipe  
- ✅ **Cross-platform compatibility** (Windows, macOS, Linux)
## 🧠 How It Works

This project uses **MediaPipe FaceMesh** to extract 468+ facial landmarks, including the irises.  
- The **right eye iris** is tracked and mapped to screen coordinates using `pyautogui.moveTo()`.
- **Blink detection**: The vertical distance between eyelids is measured; if it drops below a threshold, it simulates a click.
- **Calibration**: The system automatically adjusts to the user's gaze direction, making pointer movement more accurate.
- OpenCV is used to display the video feed with landmarks overlaid for visualization.

---
## 🧰 Tech Stack

| Tool              | Purpose                                           |
|-------------------|---------------------------------------------------|
| [Python](https://www.python.org/)     | Main programming language                          |
| [OpenCV](https://opencv.org/)        | Video capture and visualization                    |
| [MediaPipe](https://mediapipe.dev/)  | Facial landmark detection & iris tracking          |
| [PyAutoGUI](https://pyautogui.readthedocs.io/)  | Mouse movement and click simulation                 |
| [NumPy](https://numpy.org/) *(optional)* | For smoothing/filtering coordinates                 |
How to Run
python eye_mouse.py
1. Look at different parts of the screen to move the mouse.
2. Blink your left eye to perform a click.
3. Press ESC to exit the application.

Permissions:
1.The app uses your webcam — please allow access when prompted.
2.PyAutoGUI controls your mouse, so avoid running this with sensitive apps open initially.
📸 Landmark Reference
Eye Landmarks Used:
Right iris: landmark[474]
Left upper eyelid: landmark[145]
Left lower eyelid: landmark[159]
📬 Contributing
Contributions are welcome! Open an issue or submit a pull request with ideas for improvement, bug fixes, or new features.
