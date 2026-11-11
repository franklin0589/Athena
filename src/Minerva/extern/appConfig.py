from configparser import ConfigParser
import Minerva.extern.file as fh

class AppConfig:
    def __init__(self):
        self.config_path = fh.resource_path("config/")
        self.app_path = fh.resource_path("config/Athena.ini")

        fh.make_folder(self.config_path)

        if fh.exists(self.app_path):
            # Found existing Configuration using
            self.config = self.get_config() 
        else:
            # Build Configuration if none exists
            self.config = self.build_config()


    def get_config(self):
        """Retrieving Exising configuration from Standard Path 
        """
        cp = ConfigParser()
        cp.read(self.app_path )
        return cp
    
    def _get_project_folder(self):
        while True:
            input_folder = input("What it the Path of the Project Folder?")
            if fh.exists(input_folder):
                return input_folder
            else:
                print("Failed to Verify Template Location on Device! Please Try Again!")

    def build_config(self):
        cp = ConfigParser()
        cp["DEFAULT"] = {
            "location":self._get_project_folder()
        }
        with open(self.app_path, "w") as configfile:
            cp.write(configfile)
        return cp
    
    def get_location(self):
        return self.config["DEFAULT"]["location"]