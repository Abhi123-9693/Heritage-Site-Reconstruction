import cv2
import matplotlib.pyplot as plt

class Visualization:

    def show_images(self, original, mask, restored):

        plt.figure(figsize=(12,4))

        plt.subplot(1,3,1)
        plt.title("Original")
        plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))

        plt.subplot(1,3,2)
        plt.title("Detected Damage")
        plt.imshow(mask, cmap='gray')

        plt.subplot(1,3,3)
        plt.title("Restored")
        plt.imshow(cv2.cvtColor(restored, cv2.COLOR_BGR2RGB))

        plt.show()

    def show_3d_message(self):
        print("\n3D Visualization Module Coming Soon... - visualization.py:25")