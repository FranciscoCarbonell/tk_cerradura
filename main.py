from tkinter import Tk, Label, Frame, Button
from PIL import Image, ImageTk


class MainWindow(Tk):
    def __init__(self):
        super().__init__()

    def set_number(self, event, button):
        self.label2['text'] += button['text']
    
    def setupUi(self):
        self.img = ImageTk.PhotoImage(Image.open('images.png'))
        self.label = Label(self, image=self.img)
        self.label.grid(row=0, column=0, sticky='ew', pady=(30, 0))

        self.frame = Frame(self)
        self.label2 = Label(self.frame, text='', pady=10)
        self.label2.config(font=("", 20))
        self.label2.grid(row=0, column=0, columnspan=3, pady=(10, 0), sticky='we')
        row_buttons = [('1', '2', '3'), ('4', '5', '6'), ('7', '8', '9'), ('*', '0', '#')]
        row=1
        num = 0
        for rbuttons in row_buttons:
            for index, txt_btn in enumerate(rbuttons):
                padx, pady = 20, 20
                button = Button(self.frame, text=txt_btn, pady=pady, padx=padx)
                name_btn = 'button_%s' % num
                setattr(self, name_btn, button)
                button = getattr(self, name_btn)
                button.grid(row=row, column=index, padx=padx, pady=pady, sticky='nswe')
                button.bind('<Button-1>', lambda event, btn=button: self.set_number(event, btn))
                num += 1
            row += 1
        self.frame.grid(row=1, column=0, sticky='ns')
        self.configure()
    
    def configure(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

widget = MainWindow()
widget.setupUi()
widget.mainloop()