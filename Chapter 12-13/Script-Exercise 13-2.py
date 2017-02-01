import tkinter

class MyGUI():
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.frm_top1 = tkinter.Frame()
        self.frm_top2 = tkinter.Frame()
        self.frm_med = tkinter.Frame()
        self.frm_bot = tkinter.Frame()

        self.lbl_mil = tkinter.Label(self.frm_top1, text='Miles: ')
        self.ent_mil = tkinter.Entry(self.frm_top1, width=10)
        self.lbl_gal = tkinter.Label(self.frm_top2, text='Gallons: ')
        self.ent_gal = tkinter.Entry(self.frm_top2, width=10)
                                     
        self.btn_mpg = tkinter.Button(self.frm_med, text='Calculate MPG!', \
                                      command=self.calcMPG)
        
        self.mpg = tkinter.StringVar()
        self.lbl_mpg = tkinter.Label(self.frm_bot, textvariable=self.mpg)

        self.lbl_mil.pack(side='left')
        self.ent_mil.pack(side='left')
        self.lbl_gal.pack(side='left')
        self.ent_gal.pack(side='left')
                                     
        self.btn_mpg.pack()
                                     
        self.lbl_mpg.pack()

        self.frm_top1.pack()
        self.frm_top2.pack()
        self.frm_med.pack()
        self.frm_bot.pack()

        tkinter.mainloop()

    def calcMPG(self):
        self.mpg.set('MPG: ' + str(float(self.ent_mil.get()) / float(self.ent_gal.get())))

myGUI = MyGUI()
