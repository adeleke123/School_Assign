from tkinter import *

class VendingMachineApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Vending Machine')
        self.var = StringVar()

        self.create_interface()

    def create_interface(self):
        self.create_title_frame()
        self.create_input_frame()
        self.create_display_frame()

    def create_title_frame(self):
        title_frame = Label(self.root, text='Vending Machine', font='arial 18 bold', width=60, bg='#3B5A73',
                            bd=10, fg='white', relief=RAISED)
        title_frame.grid(row=0, column=0, padx=10, pady=10)

    def create_input_frame(self):
        input_frame = Frame(relief=RAISED, bd=20, bg='#3B5A73')
        input_frame.grid(row=1, column=0, padx=10, pady=10)

        sub_frame = Frame(input_frame, relief=RAISED, bd=10, bg='#3B5A73')
        sub_frame.grid(row=1, column=0, padx=10, pady=10)

        title = Label(sub_frame, text='How many "Candy" do you want ?', bg='#3B5A73', fg='white', width=30,
                      font='arial 15 bold')
        title.grid(row=1, column=0)

        entry = Entry(sub_frame, width=18, bd=7, font='arial 15 bold', justify='center', textvariable=self.var)
        entry.grid(row=2, column=0, padx=10, pady=10)

        b1 = Button(sub_frame, width=18, text='Enter', font='arial 15 bold', bd=10, bg='#E83831', fg='black',
                    command=self.enter)
        b1.grid(row=3, column=0, padx=25, pady=25)

        b2 = Button(sub_frame, width=18, text='Reset', font='arial 15 bold', bd=10, bg='#E83831', fg='black',
                    command=self.reset)
        b2.grid(row=4, column=0, padx=25, pady=25)

    def create_display_frame(self):
        display_frame = Text(self.root, width=15, height=22, bd=10, bg='#BB9E7F', font='arial 15 bold', fg='white')
        display_frame.grid(row=1, column=1, padx=10, pady=10)
        self.txtarea = display_frame

    def enter(self):
        try:
            count = int(self.var.get())
            for _ in range(count):
                self.txtarea.insert(END, '     Candy\n')
            self.clear_entry()
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def reset(self):
        self.txtarea.delete(1.0, END)
        self.clear_entry()

    def clear_entry(self):
        self.var.set("")

if __name__ == "__main__":
    root = Tk()
    app = VendingMachineApp(root)
    root.mainloop()

