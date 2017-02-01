import tkinter

class MyGUI():
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.frm_top = tkinter.Frame()
        self.frm_bot = tkinter.Frame()

        self.info = tkinter.StringVar()
        self.lbl_info = tkinter.Label(self.frm_top, textvariable=self.info)
        
        self.btn_show = tkinter.Button(self.frm_bot, text='Show info', \
                                       command=self.showInfo)
        self.btn_quit = tkinter.Button(self.frm_bot, text='Quit', \
                                       command=self.main_window.destroy)

        self.lbl_info.pack()

        self.btn_show.pack(side='left')
        self.btn_quit.pack(side='left')

        self.frm_top.pack()
        self.frm_bot.pack()

        tkinter.mainloop()

    def showInfo(self):
        self.info.set('Taylor Winowiecki\n2100 N Squirrel Rd')

myGUI = MyGUI()
