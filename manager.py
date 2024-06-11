from tkinter import Tk, Frame
from container import Container
from ttkthemes import ThemedStyle

class Manager(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Menu")
        self.resizable(False, False)
        self.configure(bg="#D5D5D5")

        window_width = 800
        window_height = 400

        self.center_window(window_width, window_height)

        self.container = Frame(self, bg="#D5D5D5")
        self.container.pack(fill="both", expand=True)

        self.frames = {
            Container: None
        }

        self.load_frames()

        self.show_frame(Container)

        self.set_theme()

    def center_window(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.geometry(f"{width}x{height}+{x}+{y}")

    def load_frames(self):
        for FrameClass in self.frames.keys():
            frame = FrameClass(self.container, self)
            self.frames[FrameClass] = frame

    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()

    def set_theme(self):
        style = ThemedStyle(self)
        style.set_theme("breeze")

def main():
    app = Manager()
    app.load_frames()
    app.show_frame(Container)
    app.mainloop()

if __name__ == "__main__":
    main()
