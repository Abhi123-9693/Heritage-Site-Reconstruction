import cv2
import numpy as np

class AIModel:

    def detect_damage(self, image_path):
        image = cv2.imread(image_path)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        _, mask = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV)

        return image, mask

    def restore_image(self, image, mask):

        restored = cv2.inpaint(
            image,
            mask,
            3,
            cv2.INPAINT_TELEA
        )

        return restored