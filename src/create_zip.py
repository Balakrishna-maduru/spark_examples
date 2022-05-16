import os
from zipfile import ZipFile


class Zipper:
    def __init__(self, file_name: str, filepath: str = "") -> None:
        self.zip_object = ZipFile(f'{filepath}{file_name}', 'w')

    def __exit__(self):
        self.zip_object.close()

    def add_file(self, file_name: str, directory_path: str = None) -> None:
        filePath = os.path.join(directory_path, file_name)
        self.zip_object.write(filePath, os.path.basename(filePath))
    
    def add_directory(self, directory_path: str = None) -> None:
        for folder_name, subfolders, filenames in os.walk(directory_path):
            for filename in filenames:
                filePath = os.path.join(folder_name, filename)
                target_path = f"{folder_name.split('/')[-1]}/{os.path.basename(filePath)}"
                print(target_path)
                self.zip_object.write(filePath, target_path)

if __name__ == "__main__":
    zf = Zipper("spark_session_lib.zip")
    # zf.add_file("session.py","/Users/BMadu1/Documents/my_demo/pyspark/spark_examples/src/lib/")
    zf.add_directory("/Users/BMadu1/Documents/my_demo/pyspark/spark_examples/src/")