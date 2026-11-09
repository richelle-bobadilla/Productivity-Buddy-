# imports
import tkinter as tk

class StudyTimer:

    def __init__(self, root):

        # set up
        self.root = root
        self.root.title("Study Timer")
        self.time_left = 0

        self.root.configure(bg = "#2e2e2e")


        #widgets
        # instructions
        self.instructions = tk.Label(root, text = "How long do you want to study?")
        self.instructions.pack(pady = 20)

        # slider
        self.slider = tk.Scale(root, orient = "horizontal", from_ = 5, to = 120, length = 300)
        self.slider.pack(pady = 10)
        # start button
        # countdown text
        pass

    def start_timer(self):
        # start the timer
        pass

    def update_timer(self):
        # update the countdown text
        pass



if __name__ == "__main__":

    root = tk.Tk()
    StudyTimer(root)
    root.mainloop()
