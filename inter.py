from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from assesment import evaluate
from tkinter import messagebox
import get_model


class App:
    model = get_model.load()
    def __init__(self):
        self.window = Tk()
        self.window.title("PRIMARY EVALUATION OF WORKS OF ART")
        self.window.geometry('1000x600')
        self.menu = Menu(self.window)
        self.menu_item = Menu(self.menu, tearoff=0)
        self.menu_item.add_command(label='Load image', command=self.load_file)
        self.menu_item.add_separator()
        self.menu_item.add_command(label='Evaluate', command=self.evaluation, state=DISABLED)
        self.menu.add_cascade(label='Menu', menu=self.menu_item)
        self.window.config(menu=self.menu)
        self.window.mainloop()


    def load_file(self):
        self.imgfile = filedialog.askopenfilename(filetypes=(("Images", "*.png"), ("all files", "*.*")))
        # add image
        self.canvas = Canvas(self.window, height=500, width=1000)

        self.canvas.grid(row=0, column=0)
        try:
            # load image
            self.image = Image.open(self.imgfile)
        except FileNotFoundError:
            messagebox.showerror(
            "Error",
            "File not found")
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(500, 250, anchor=CENTER, image=self.photo)
        self.menu_item.entryconfig('Evaluate', state="normal")


    def evaluation(self):
        if self.image:
            self.result = evaluate(self.imgfile, self.model)
        else:
            self.result = "load image"
        res = Label(self.window, text=self.result, font=("Arial Bold", 20))
        res.grid(column=0, row=1)


app = App()


