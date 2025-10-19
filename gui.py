import tkinter as tk
from tkinter import filedialog, Label, Button
from PIL import Image, ImageTk
import cv2
import os

class GUI:
    def __init__(self, root):

        #initilising main window
        self.root = root
        self.root.title("Office Object Detection")  #title
        self.root.geometry("1200x1200") #size

        #header label
        header = Label(root, text="Office Object Detection GUI", fg="black", bg="white")

        #window frame for image and video display
        self.image_label = Label(root)
        self.image_label.pack(pady=10)

        self.result_label = Label(root, text="", font=("Helvetica", 20))
        self.result_label.pack(pady=10)

        # Buttons for the different commands
        Button(root, text="Upload Image", command=self.upload_image).pack(pady=5)
        Button(root, text="Start Live Video", command=self.start_video_stream).pack(pady=5)
        Button(root, text="Stop Video", command=self.stop_video_stream).pack(pady=5)
