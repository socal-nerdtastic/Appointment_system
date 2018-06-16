from tkinter import *

class Menu():
    def __init__(self,master):
        self.master = master
        # master is the frame or whole interface. Frame is the section of the whole screen you've chosen
        self.master = Frame(self.master, width=500, height=500, bg='#ffffff')
        self.master.pack()
        # after these lines, it becomes a blank slate once again
        # title header
        self.clinic_header = Label(self.master, text="+ Stephen's Clinic +", font=('arial 30'), fg='red', bg='white')
        self.clinic_header.place(x=80, y=0)
        # new patient button *** add cmd ***
        self.new_patient = Button(self.master, text="Add a new patient", width=40, height=5, bg="#9999ff",command=self.add_patient)
        self.new_patient.place(x=105, y=130)
        # update patient button *** add cmd ***
        self.update_patient = Button(self.master, text="Update/Delete Patients", width=40, height=5, bg="#9999ff",command=self.change_patient)
        self.update_patient.place(x=105, y=250)
        # schedule patient button *** add cmd ***
        self.schedule_patient = Button(root, text="View Schedule", width=40, height=5, bg="#9999ff",command=self.view_schedule)
        self.schedule_patient.place(x=105, y=370)
    def add_patient(self):
            pass
    def change_patient(self):
            pass
    def view_schedule(self):
            pass

root = Tk()
# size of root
b = Menu(root)
root.geometry("500x500+0+0")
# cant be resized
root.resizable(False, False)
# just says that i will put your window in an infinite loop until you
# close the window yourself
root.mainloop()
