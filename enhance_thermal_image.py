# enhance_thermal_image.py

import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse
import os

def enhance_thermal_image(input_path):
    # Step 1: Load grayscale image
    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Failed to load image: {input_path}. Make sure it's a valid image.")

    # Step 2: Interpolate to 320x240
    interpolated_img = cv2.resize(img, (320, 240), interpolation=cv2.INTER_CUBIC)

    # Step 3: CLAHE contrast enhancement
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    enhanced_img = clahe.apply(interpolated_img)

    # Step 4: Apply INFERNO colormap
    colored_img = cv2.applyColorMap(enhanced_img, cv2.COLORMAP_INFERNO)

    # Step 5: Show and optionally save
    plt.figure(figsize=(8, 6))
    plt.imshow(cv2.cvtColor(colored_img, cv2.COLOR_BGR2RGB))
    plt.title("Interpolated & Enhanced Thermal Image")
    plt.axis('off')
    plt.show()

    output_path = "enhanced_output.png"
    cv2.imwrite(output_path, colored_img)
    print(f"Enhanced image saved as: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image_path", help="Path to the thermal grayscale image")
    args = parser.parse_args()
    enhance_thermal_image(args.image_path)
