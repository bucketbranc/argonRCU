import os, shutil, argparse
from time import sleep
from playsound import playsound

class Moduler():
    def getImports(file_path):
        """
        Retrieve the modules imported in a Python file.
    
        Args:
            file_path (str): The path to the Python file.
    
        Returns:
            set: A set of imported module names.
        """
        with open(file_path, 'r') as file:
            source = file.read()
    
        imported_modules = set()
        for line in source.splitlines():
            if line.startswith('import ') or line.startswith('from '):
                module_parts = line.split(' ')[1].split(',')
                for module_part in module_parts:
                    module_name = module_part.strip().split(' ')[0].split('.')[0]
                    imported_modules.add(module_name)
    
        return imported_modules
    def getModuleLocation(imported_modules):
        """
        Determine the locations of the imported modules.
    
        Args:
            imported_modules (set): A set of imported module names.
    
        Returns:
            dict: A dictionary mapping module names to their file paths.
        """
        module_locations = {}
        for module_name in imported_modules:
            try:
                module = __import__(module_name)
                module_locations[module_name] = os.path.dirname(module.__file__)
            except (ImportError, AttributeError):
                pass
    
        return module_locations
    
# Arguments
parser = argparse.ArgumentParser(description='Donload Code into E6-RCU, Fast and Reliable')
parser.add_argument('filename') 
parser.add_argument('disk') 
parser.add_argument('module') 

args = parser.parse_args()
path = os.getcwd()
# Keep checking for the USB drive every 5 seconds
while True:
    try:
        # Check if the target directory exists (USB drive is connected)
        if os.path.exists("{}:/".format(args.disk)) and os.path.exists('{}\\scr\\{}.py'.format(path, args.filename)):
            # Copy the file to the target directory
            shutil.copyfile('{}\\scr\\{}.py'.format(path, args.filename), '{}:/{}.py'.format(args.disk, args.filename))
            print("File copied successfully!")
            playsound(path + "\\notification.mp3")
            time.sleep(3)
    except Exception as e:
          print(e)

    time.sleep(1)  # Wait for 5 seconds before checking again