import time
import board
import busio
import numpy as np
import adafruit_mlx90640
import matplotlib.pyplot as plt
import os

# Setup I2C and sensor
i2c = busio.I2C(board.SCL, board.SDA, frequency=400000)
mlx = adafruit_mlx90640.MLX90640(i2c)
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ

# Create folder to save images
save_dir = "thermal_full_images"
os.makedirs(save_dir, exist_ok=True)

frame = np.zeros((24 * 32,))
frame_count = 0

# Setup plotting
fig, ax = plt.subplots(figsize=(12, 7))
therm1 = ax.imshow(np.zeros((24, 32)), cmap='inferno', vmin=20, vmax=40)
cbar = fig.colorbar(therm1)
cbar.set_label('Temperature [$^{\circ}$C]', fontsize=14)
plt.axis('off')  # Optional: turn off axis

while True:
    try:
        mlx.getFrame(frame)
        data_array = np.reshape(frame, (24, 32))
        therm1.set_data(np.fliplr(data_array))  # Flip if necessary
        fig.canvas.draw()

        # Save the full plot including colorbar
        filename = os.path.join(save_dir, f"thermal_full_{frame_count:04d}.png")
        fig.savefig(filename, bbox_inches='tight')
        print(f"Saved: {filename}")

        frame_count += 1
        time.sleep(0.5)
    except KeyboardInterrupt:
        print("Exiting...")
        break
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(0.5)
