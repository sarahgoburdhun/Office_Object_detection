import tkinter as tk
from tkinter import filedialog, Label, Button
from turtle import bgcolor
from PIL import Image, ImageTk
import cv2
from .button import GUIButton


class GUI:
    def __init__(self, root):

        # initialising main window
        self.root = root
        self.root.title("Office Object Detection")  # title
        self.root.geometry("500x300+700+300")  # set size and location

        # header label
        header = Label(root, text="Welcome to the Office Object Detection Model", fg="black",  font=("Helvetica", 15))


        # Buttons for the different commands
        upload_img_btn = GUIButton(root, text="Upload Image", command=self.upload_image, font=("Helvetica", 15), x=50, y=150)
        upload_img_btn.config_colours( activeBG="green4", activeFG="white", bgcolour="SpringGreen3", 
                                        fgcolour="white", hoverBG="green3", hoverFG="white")

        live_stream_btn = GUIButton(root, text="Live Detection", command=self.start_video_stream, font=("Helvetica", 15), x=320, y=150)
        live_stream_btn.config_colours( activeBG="green4", activeFG="white", bgcolour="SpringGreen3", 
                                        fgcolour="white", hoverBG="green3", hoverFG="white")

        quit_btn = GUIButton(root, text="Quit", command=self.quit_app, font=("Helvetica", 15), x=200, y=200)

        quit_btn.config_colours( activeBG="firebrick4", activeFG="white", bgcolour="firebrick3", 
                                        fgcolour="white", hoverBG="red", hoverFG="white")
        
        quit_btn.set_dimensions(height=2, width=8)

        back_btn = GUIButton(root, text="Back",command=self.go_back,
                             font=("Helvetica", 15), x=200, y=100)

        back_btn.config_colours(activeBG="gray30", activeFG="white", bgcolour="gray60",
                                fgcolour="white", hoverBG="gray40", hoverFG="white")
        
        back_btn.set_dimensions(height=2, width=8)

        self.image_label = tk.Label(self.root)
        self.image_label.place(x=50, y=80)

        header.place(x=50, y=50)
        # live_stream_btn.place(x=320, y=150)

        # cv2 video capture state
        self.cap = None
        self.running = False

    def upload_image(self):
        # open file dialogue
        filename = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
        if filename:
            self.display_image(filename)  # display selected image

    def display_image(self, path):
        # create a window
        self.image_window = tk.Toplevel(self.root)
        self.image_window.title("Uploaded Image")
        self.image_window.geometry("600x600+750+300")
        # load and resize the image
        img = Image.open(path).resize((625, 625))
        imgtk = ImageTk.PhotoImage(img)

        # create a label inside the  window
        image_label = tk.Label(self.image_window, image=imgtk)
        image_label.imgtk = imgtk
        image_label.pack(padx=10, pady=10)

    def start_video_stream(self):
         if not self.running:
            # create a new window for the webcam feed
            self.video_window = tk.Toplevel(self.root)
            self.video_window.title("Live Camera Feed")
            self.video_window.geometry("600x600+750+300") 

            # label inside the new window to hold frames
            self.video_label = tk.Label(self.video_window)
            self.video_label.pack(padx=10, pady=10)
        # start webcam stream
            self.cap = cv2.VideoCapture(0)
            self.running = True
            self.update_video()

    def stop_video_stream(self):
        # stop webcam stream
        self.running = False
        if self.cap:
            self.cap.release()
            self.cap = None
        if hasattr(self, "video_window") and self.video_window.winfo_exists():
            self.video_window.destroy()

    def update_video(self):
    # updates the frames for real-time camera feed
        if self.running and self.cap:
            ret, frame = self.cap.read()
            if ret:
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(rgb_frame).resize((625, 625))
                imgtk = ImageTk.PhotoImage(image=img)
                # updates with new frame
                self.video_label.imgtk = imgtk
                self.video_label.configure(image=imgtk)

            self.video_window.after(50, self.update_video)  # sets time between frames to be every 50 ms

    def quit_app(self):
        self.stop_video_stream()  # video stream if it's onw
        self.root.quit()  # exit gui

    def go_back(self):
        # closes any pop-up windows and resets todefault state
        self.stop_video_stream()
        self.image_label.config(image='')
        if hasattr(self, "image_window") and self.image_window.winfo_exists():
            self.image_window.destroy()
