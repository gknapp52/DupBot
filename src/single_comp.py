## File that is used to compare single file to various 
import cv2
import os

# This function aggregates all files in directory into an array
def parse_files( directory_path ) :

    file_list = []

    try:
        for file in os.walk(directory_path):
            print()

    except FileNotFoundError:
        print(f"The directory '{directory_path}' does not exist.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return file_list