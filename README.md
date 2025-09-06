Pedestrian detection is one of the fundamental tasks in computer vision, widely used in **surveillance systems**, **self-driving cars**, **safety monitoring**, and **crowd analytics**.  
This repository contains a simple yet effective implementation of pedestrian detection using **OpenCV in Python**. It leverages the **Histogram of Oriented Gradients (HOG)** descriptor and a **pre-trained Support Vector Machine (SVM)** classifier to detect humans in video streams.

The project demonstrates how classical computer vision techniques can achieve reliable detection without relying on heavy deep learning models. It is lightweight, runs on CPU, and is suitable for beginners who want to understand the mechanics of object detection.

---

## ✨ Features
- 🚶 Detects pedestrians in a video file (default: `people.mp4`)  
- ⚡ Real-time processing with bounding box visualization  
- 📦 Uses OpenCV’s **HOG + SVM** pre-trained pedestrian detector  
- 🖼️ Handles multiple pedestrians in a single frame  
- 🖱️ Press **Q** to quit the detection window  
- 💡 Simple Python code that is easy to read, extend, and modify  

---

## 🧩 How It Works
The pedestrian detection pipeline consists of the following steps:

1. **Histogram of Oriented Gradients (HOG):**  
   - Extracts edge and gradient information from small patches of the image.  
   - Effective at capturing the contour and silhouette of human figures.  

2. **Pre-trained Linear SVM:**  
   - A Support Vector Machine trained on positive (pedestrian) and negative (non-pedestrian) samples.  
   - Classifies detection windows as “person” or “not person.”  

3. **Sliding Window Search:**  
   - The algorithm slides a detection window across the image at different scales.  
   - Ensures detection of pedestrians at varying sizes and positions.  

4. **Bounding Box Visualization:**  
   - All detected pedestrians are highlighted with green rectangles.  
   - The video feed updates frame by frame with detection results.
