from tkinter import *
from tkinter.ttk import Progressbar
from tkinter.ttk import Combobox
from num2words import num2words
from covid import Covid
from matplotlib import pyplot as plt
from matplotlib import style
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import time
import os
import random
import tkinter
from  tkinter import ttk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
style.use('ggplot')

########################

class Covid_Operation:
    covid = Covid()
    ctry_data = ''

    def get_world_cases_info(self):
        try:
            confirmed = self.covid.get_total_confirmed_cases()
            recovered = self.covid.get_total_recovered()
            deaths = self.covid.get_total_deaths()
            return (confirmed, recovered, deaths)
        except Exception as e:
            messagebox.showerror('Network Problem', 'Please check your Internet Connection')
            print(e)
            exit()

    def country_list(self):
        try:
            self.ctry_data = self.covid.list_countries()
        except:
            messagebox.showerror('Network Problem', 'Please check your Internet Connection')
            exit()
        cntry_list = []
        cntry_id_list = []
        for di in self.ctry_data:
            for k, v in di.items():
                if (not (v.isnumeric())):
                    cntry_list.append(v)
                else:
                    cntry_id_list.append(v)

        cntry_list.sort()
        cntry_id_list.sort()
        return (cntry_list, cntry_id_list)

    def get_all_data(self):
        try:
            data = self.covid.get_data()
        except:
            messagebox.showerror('Error', 'Something Went Wrong')

        df = pd.DataFrame(data)
        print(df)
        df.to_excel("Report_CoronaVirus_Cases.xlsx", sheet_name='coronavirus_cases', )
        val = "File created Successfully\nFile Name : " + "Report_CoronaVirus_Cases.xlsx"
        self.T1.delete(1.0, END)
        self.T1.insert(END, val)
        messagebox.showinfo("Congratulation", "File created Successfully")


class MainUI(Covid_Operation):
    T1 = ''

    def __init__(self):
        self.window = Tk()
        self.country_combo = ''
        self.graph_frame = ''
        self.toolbar = ''
        self.canvas = ''
        self.image_lb = ''
        self.country_id_combo = ''

    def Set_Window(self):
        self.window.title('Coronavirus COVID-19 Global Cases')
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        size = str(screen_width) + "x" + str(screen_height)
        self.window.geometry(size)
        self.window.configure(bg='black')
        self.window.iconbitmap('corona.ico')

    def Set_Header(self):
        header_frame = Frame(self.window, height=10, bg='#4C4B4B')
        header_frame.pack(fill=X,padx=5,pady=5)

        header_label = Label(header_frame, text='Coronavirus COVID-19 Global Cases  provided by Johns Hopkins university and worldometers.info', bg='#4C4B4B', fg='white',
                             font=('Arial', 10, 'bold'))
        header_label.pack(side=LEFT, ipadx=5, ipady=5, padx=0)


    def Set_Footer(self):
        footer_frame = Frame(self.window, bg='#4C4B4B')
        footer_frame.pack(side=BOTTOM, fill=X,padx=5,pady=5)

        footer_label = Label(footer_frame, text='@ Copyright- Designed and Develeoped by Abdul zubair Abdul wahab pathan',
                             fg='white', bg='#4C4B4B', font=('Arial', 10, 'bold'))
        footer_label.pack(side=BOTTOM, ipadx=5, ipady=5, padx=20)

    def Set_Terminal(self):
        Terminal_frame = Frame(self.window)
        Terminal_frame.pack(side=RIGHT, fill=Y, pady=0, padx=5)

        # Progress bar
        pgbar = Progressbar(Terminal_frame, length=200, orient=HORIZONTAL, value=10)
        pgbar.pack(side=BOTTOM, fill=X)
        pgbar.start()

        # Terminal Label
        title_label = Label(Terminal_frame, text='Terminal', fg='black', bg='#DAE0E2', justify=LEFT, relief=SUNKEN,
                            bd=3, font=('Arial', 10, 'bold'))
        title_label.pack(anchor=W, fill=X)

        # Terminal
        scroll = Scrollbar(Terminal_frame)
        scroll.pack(side=RIGHT, fill=Y)

        self.T1 = Text(Terminal_frame, fg='white', bg='#2C3335', font=('Verdana', 10, 'bold'), width=49,
                       yscrollcommand=scroll.set, relief=SUNKEN, bd=3)
        self.T1.pack(side=RIGHT, fill=Y)
        scroll.config(command=self.T1.yview)

        self.T1.insert(END, "\n ----- Coronavirus COVID-19 Global Cases Information -----\n\n")

    def World_Coronavirus_Details(self):

        world_details_frame = Frame(self.window, bg='black', bd=0)  # RED
        world_details_frame.pack(side=TOP, fill=X, padx=(5,0), pady=(0,5))

        ## CONFIRMED FRAME

        Confirmed_frame = Frame(world_details_frame, bg='#4C4B4B', width=30)  # GREEN
        Confirmed_frame.pack(side=LEFT)

        cf = Frame(Confirmed_frame, bg='#4C4B4B')  # BLUE
        cf.pack(pady=20, padx=40)

        cl1 = Label(cf, text='Total Confirmed', fg='white', bg='#4C4B4B', font=('Arial', 20, 'bold'))
        cl1.pack(side=TOP)

        cl2 = Label(cf, text='679977', fg='red', bg='#4C4B4B', font=('Arial', 30, 'bold'))
        cl2.pack(side=TOP)

        ## DEATHS FRAME

        Death_frame = Frame(world_details_frame, bg='#4C4B4B')
        Death_frame.pack(side=LEFT, padx=5)

        dfr = Frame(Death_frame, bg='#4C4B4B')
        dfr.pack(pady=20, padx=40)

        dl1 = Label(dfr, text='  Total Deaths ', fg='white', bg='#4C4B4B', font=('Arial', 20, 'bold'))
        dl1.pack(side=TOP)

        dl2 = Label(dfr, text='679977', fg='white', bg='#4C4B4B', font=('Arial', 30, 'bold'))
        dl2.pack(side=TOP)

        ## RECOVERED FRAME

        Recovered_frame = Frame(world_details_frame, bg='#4C4B4B')
        Recovered_frame.pack(side=LEFT, padx=0, pady=0)

        Rfr = Frame(Recovered_frame, bg='#4C4B4B')
        Rfr.pack(pady=20, padx=40)

        rl1 = Label(Rfr, text='Total Recovered', fg='white', bg='#4C4B4B', font=('Arial', 20, 'bold'))
        rl1.pack(side=TOP)

        rl2 = Label(Rfr, text='679977', fg='#45CE30', bg='#4C4B4B', font=('Arial', 30, 'bold'))
        rl2.pack(side=TOP)

        confirm, recovered, deaths = self.get_world_cases_info()
        cl2.config(text=confirm)
        rl2.config(text=recovered)
        dl2.config(text=deaths)

    def Buttons_Frame(self):

        bt_frame = Frame(self.window, bg='#4C4B4B', width=300)
        bt_frame.pack(side=LEFT, expand=False, fill=BOTH, padx=5, pady=0)

        v = self.country_list()[0]
        self.country_combo = Combobox(bt_frame, value=v, height=10, width=30,font=('arial',8,'bold'),cursor='hand2')
        self.country_combo.place(x=35, y=50)
        self.country_combo.set('Get Status By Country Name')

        bt_font = ('Arial', 10, 'bold')

        process_button = Button(bt_frame, text='Processed', fg='#000000', bg='#4C4B4B', width=10, height=1, font=bt_font,
                                command=self.get_country_info,padx=3,pady=3,cursor='hand2')
        process_button.place(x=85, y=90,)

        list_button = Button(bt_frame, text='Get List of Countries', fg='black',width=17, bg='#4C4B4B', height=1,
                             font= ('verdana', 10, 'bold'), command=self.get_cntry_list,padx=3,pady=3,cursor='hand2')
        list_button.place(x=50, y=300)

        all_data_button = Button(bt_frame, text='Get All Data', fg='black',width=17, bg='#4C4B4B', height=1,
                                 font=('verdana', 10, 'bold'), command=self.get_all_data,relief=RAISED,padx=3,pady=3,cursor='hand2')
        all_data_button.place(x=50, y=360)

        v_id = self.country_list()[1]
        self.country_id_combo = Combobox(bt_frame, values=v_id, height=10, width=30,font=('arial',8,'bold'),cursor='hand2' )
        self.country_id_combo.place(x=35, y=170)
        self.country_id_combo.set("Get Status By Country id")

        process_button_id = Button(bt_frame, text='Processed', fg='#000000', bg='#4C4B4B', width=10, height=1,
                                   font=bt_font,
                                   command=self.get_country_info,padx=4,pady=4,cursor='hand2')
        process_button_id.place(x=85, y=210, )

    def Graph_Frame(self, ):
        self.graph_frame = Frame(self.window, bg='#4C4B4B', width=575, bd=10)
        self.graph_frame.pack(side=LEFT, fill=BOTH, pady=0)

        dir_list = os.listdir('Images')
        random.shuffle(dir_list)
        img_file = random.choice(dir_list)
        img_path = r"Images" + "\\" + img_file
        img = PhotoImage(file=img_path)

        self.image_lb = Label(self.graph_frame, image=img)
        self.image_lb.image = img  # keep a reference
        self.image_lb.pack(fill=BOTH, expand=1)

    ## CORONAVIRUS TRACKER PROGRAMM

    def get_cntry_list(self):
        cntry_list = []
        self.T1.delete(1.0, END)
        for di in self.ctry_data:
            for k, v in di.items():
                print(k, v, end='\t')
                val = k + "  " + v + "\t"
                self.T1.insert(END, val)
            self.T1.insert(END, "\n")
        messagebox.showinfo("Congratualation", 'Result Created Successfully')

    def get_country_info(self):

        if (self.canvas != ""):
            self.canvas.get_tk_widget().pack_forget()
            self.toolbar.pack_forget()
            self.ax.clear()
            self.fig.clear()

        self.image_lb.config(image='')
        self.image_lb.image = ''

        country_name = self.country_combo.get()
        country_id = self.country_id_combo.get()

        if (country_name == "Get Status By Country Name" and country_id == 'Get Status By Country id'):
            messagebox.showerror('Error', 'Please Select Country')
            country_name = 'India'

        if (country_name != "Get Status By Country Name"):
            try:
                data = self.covid.get_status_by_country_name(country_name)
            except:
                messagebox.showerror('Network Problem', 'Please check your Internet Connection')

        if (country_id != 'Get Status By Country id'):
            try:
                data = self.covid.get_status_by_country_id(country_id)
            except:
                messagebox.showerror('Network Problem', 'Please check your Internet Connection')

        self.T1.delete(1.0, END)

        if country_name == 'India' or country_id == '91':
            print('TRUE')
            img = PhotoImage(file='India.png')
            self.T1.image_create(1.0, image=img)
            self.T1.image = img

        print(data)
        self.T1.insert(END, "\n\n")
        self.T1.insert(END, "--" * 20)
        self.T1.insert(END, "\n")

        l1 = ['confirmed', 'active', 'deaths', 'recovered']
        x = []
        y = []

        bar_title_country_name=''

        for k, v in data.items():
            val = str(k) + "  " + str(v) + "\n"
            self.T1.insert(END, val)
            if('country'==k):
                bar_title_country_name=v
            if k in l1:
                x.append(k)
                y.append(v)

        self.T1.insert(END, "--" * 20)
        self.T1.insert(END, "\n")

        ### PLOTTING GRAPH ON TKINTER WINDOW

        self.fig = plt.Figure(figsize=(8,4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.bar(x, y)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.graph_frame,)  # A tk.DrawingArea.
        self.canvas.get_tk_widget().configure(background='#99AAAB', highlightcolor='#99AAAB', highlightbackground='#99AAAB')
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self.graph_frame)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        self.ax.set_title(' Report Corona cases of ' + bar_title_country_name)
        self.ax.set_ylabel('Count')

        for a, b in zip(x, y):
            print(a, b)
            self.ax.text(a, b, str(b), horizontalalignment='center', verticalalignment='top')

        messagebox.showinfo("Congratualation", 'Result Created Successfully')

        x = []
        y = []

        self.country_id_combo.set("Get Status By Country id")
        self.country_combo.set('Get Status By Country Name')

    def ui_mainloop(self):
        self.window.mainloop()
