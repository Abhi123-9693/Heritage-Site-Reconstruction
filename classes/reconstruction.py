import cv2

class Reconstruction:

    def save_output(self, image, path="output/restored_output.jpg"):

        cv2.imwrite(path, image)

        print(f"\nOutput Saved Successfully at: {path} - reconstruction.py:9")