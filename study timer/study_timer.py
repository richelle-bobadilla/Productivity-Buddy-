# imports
import tkinter as tk
from tkinter import messagebox

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
        self.slider = tk.Scale(root, orient = "horizontal", from_ = 1, to = 120, length = 300)
        self.slider.pack(pady = 10)

        # start button
        self.start_button = tk.Button(root, text = "Start", command = self.start_timer)
        self.start_button.pack(pady = 10)

        # countdown text
        self.countdown_text = tk.Label(root, text = "", font =("Helvetica", 50), fg = "#618af2", bg = "#2e2e2e")
        self.countdown_text.pack()


    def start_timer(self):
        # start the timer
        self.time_left = int(self.slider.get()) * 60
        self.update_timer()
        

    def update_timer(self):
        # update the countdown text
        if self.time_left > 0:
            minutes, seconds = divmod(self.time_left, 60)
            formatted_time = f"{minutes:02d}:{seconds:02d}"
            self.countdown_text.config(text = formatted_time)
            self.time_left -= 1
            self.root.after(1000, self.update_timer)

        else:
            self.countdown_text.config(text = "00:00")
            messagebox.showinfo("Time's up! Break time :D")




if __name__ == "__main__":

    root = tk.Tk()
    StudyTimer(root)
    root.mainloop()
