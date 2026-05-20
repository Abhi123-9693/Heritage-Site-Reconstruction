class HeritageSite:
    def __init__(self):
        self.site_name = ""
        self.image_path = ""

    def set_site(self, name, path):
        self.site_name = name
        self.image_path = path

    def get_details(self):
        return {
            "Site Name": self.site_name,
            "Image Path": self.image_path
        }