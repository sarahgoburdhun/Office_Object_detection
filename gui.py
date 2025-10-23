import tkinter as tk
from tkinter import filedialog, Label, Button
from PIL import Image, ImageTk
import cv2


class GUI:
    def __init__(self, root):

        # initilising main window
        self.root = root
        self.root.title("Office Object Detection")  # title
        self.root.geometry("400x400+700+300")  # set size and location

        # header label
        header = Label(root, text="Welcome to the Office Object Detection Model", fg="black",  font=("Helvetica", 15))
        header.pack(side="top")

        # window frame for image and video display
        self.image_label = Label(root)
        self.image_label.pack(pady=10)
        self.result_label = Label(root, text="", font=("Helvetica", 20))
        self.result_label.pack(pady=10)

        # Buttons for the different commands
        Button(root, text="Upload Image", command=self.upload_image).pack(pady=5)
        Button(root, text="Start Live Video", command=self.start_video_stream).pack(pady=5)
        Button(root, text="Stop Video", command=self.stop_video_stream).pack(pady=5)
        Button(root, text="Back", command=self.go_back).pack(pady=5)

        # cv2 video capture state
        self.cap = None
        self.running = False

    def upload_image(self):
        # open file dialogue
        filename = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
        if filename:
            self.display_image(filename)  # display selected image

    def display_image(self, path):
        # loads and displays selected image
        img = Image.open(path).resize((500, 500))
        imgtk = ImageTk.PhotoImage(img)
        self.image_label.imgtk = imgtk
        self.image_label.configure(image=imgtk)

    def start_video_stream(self):
        # start webcam stream
        if not self.running:
            self.cap = cv2.VideoCapture(0)
            self.running = True
            self.update_video()

    def stop_video_stream(self):
        # stop webcam stream
        self.running = False
        if self.cap:
            self.cap.release()
            self.cap = None
            self.image_label.config(image='')

    def update_video(self):
    # updates the frames for real-time camera feed
        if self.running and self.cap:
            ret, frame = self.cap.read()
            if ret:
                # saves the frame temporarily for classification
                temp_path = "frame.jpg"
                cv2.imwrite(temp_path, frame)

                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(rgb_frame).resize((800, 400))
                imgtk = ImageTk.PhotoImage(image=img)
                # updates with new frame
                self.image_label.imgtk = imgtk
                self.image_label.configure(image=imgtk)

            self.root.after(50, self.update_video)  # sets time between frames to be every 50 ms

    def go_back(self):
        #stop webcam stream
        self.stop_video_stream()
        self.image_label.configure(image='')


