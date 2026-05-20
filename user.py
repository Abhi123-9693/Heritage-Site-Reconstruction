from tkinter import Tk
from tkinter.filedialog import askopenfilename

from classes.heritage_site import HeritageSite
from classes.ai_model import AIModel
from classes.reconstruction import Reconstruction
from classes.visualization import Visualization

class User:

    def __init__(self):

        self.site = HeritageSite()
        self.ai = AIModel()
        self.reconstruct = Reconstruction()
        self.visual = Visualization()

        self.image = None
        self.mask = None
        self.restored = None

    def upload_image(self):

        Tk().withdraw()

        file_path = askopenfilename(
            title="Select Heritage Image",
            filetypes=[("Image Files", "*.jpg *.png *.jpeg")]
        )

        if file_path:

            self.site.set_site("Heritage Site", file_path)

            print("\nImage Uploaded Successfully! - user.py:35")
            print(file_path)

    def detect_damage(self):

        details = self.site.get_details()

        if details["Image Path"] == "":
            print("\nPlease upload image first! - user.py:43")
            return

        self.image, self.mask = self.ai.detect_damage(
            details["Image Path"]
        )

        print("\nDamage Detection Completed! - user.py:50")

    def restore_image(self):

        if self.image is None or self.mask is None:
            print("\nPlease detect damage first! - user.py:55")
            return

        self.restored = self.ai.restore_image(
            self.image,
            self.mask
        )

        print("\nImage Restoration Completed! - user.py:63")

    def view_result(self):

        if self.restored is None:
            print("\nPlease restore image first! - user.py:68")
            return

        self.visual.show_images(
            self.image,
            self.mask,
            self.restored
        )

    def save_output(self):

        if self.restored is None:
            print("\nNo restored image found! - user.py:80")
            return

        self.reconstruct.save_output(self.restored)

    def menu(self):

        while True:

            print("\n - user.py:89")
            print("===== HERITAGE SITE RECONSTRUCTION ===== - user.py:90")
            print("1. Upload Site Image - user.py:91")
            print("2. Detect Damaged Parts - user.py:92")
            print("3. Restore using AI - user.py:93")
            print("4. View Reconstruction - user.py:94")
            print("5. Save Output - user.py:95")
            print("6. Exit - user.py:96")

            choice = input("\nEnter Choice: ")

            if choice == "1":
                self.upload_image()

            elif choice == "2":
                self.detect_damage()

            elif choice == "3":
                self.restore_image()

            elif choice == "4":
                self.view_result()

            elif choice == "5":
                self.save_output()

            elif choice == "6":
                print("\nExiting Project... - user.py:116")
                break

            else:
                print("\nInvalid Choice! - user.py:120")