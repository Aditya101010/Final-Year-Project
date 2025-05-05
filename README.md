# Thermal Anomaly Detection using MLX90640 and Image Enhancement

This project captures, visualizes, and enhances thermal images using the **MLX90640 infrared thermal sensor** with a **Raspberry Pi**. It is part of a final-year engineering project aimed at identifying thermal anomalies in solar panels and electric towers using a drone-mounted system.

---

## 📷 Project Overview

### 1. **Thermal Image Capture**
- Captures raw temperature data (24x32 resolution) from the MLX90640 sensor
- Uses Matplotlib to visualize and save color-mapped thermal images
- Saves each frame as a PNG for later analysis

### 2. **Image Enhancement**
- Loads low-resolution thermal images
- Upscales to 320x240 using cubic interpolation
- Enhances contrast using **CLAHE (Contrast Limited Adaptive Histogram Equalization)**
- Applies **INFERNO** colormap to improve visibility of temperature variations

---

## 🧠 Applications
- Fault detection in solar panels (hot spots)
- Monitoring temperature anomalies in electric transmission lines
- General low-cost thermal surveillance with Raspberry Pi and Python

---

## 🛠️ Hardware & Software Used

### 🔧 Hardware:
- Raspberry Pi 4 Model B
- 7Semi MLX90640 IR Thermal Camera (I2C Interface)

### 🐍 Software/Dependencies:
- Python 3.x
- NumPy
- OpenCV
- Matplotlib
- Adafruit CircuitPython MLX90640 Library

---

## 📁 Folder Structure

