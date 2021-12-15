# -*- coding: utf-8 -*-
"""
Spyder Editor
"""

#import pandas as pd
from pandas import DataFrame, concat, to_numeric, read_csv
from numpy import array
import mplcursors

from tkinter import Tk, Label, Frame, Entry, Button, ttk, messagebox, Toplevel
from tkinter.filedialog import askopenfilename

from pandastable import Table

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

class my_program:
    def __init__(self, master):
        self.master = master
        master.title("Dilato moduli calculation app")
        
        
        # create the frames 
        self.left_frame = Frame(root, width=400, height= 400, bg='grey')
        self.left_frame.pack(side='left', fill='both', padx=10, pady=5, expand=0)

        self.right_frame = Frame(root, width=400, height=400, bg='grey')
        self.right_frame.pack(side='right', fill='both', padx=10, pady=5, expand=True)

        self.toolbarFrame = Frame(self.right_frame, width=50, height= 50, bg='grey')
        self.toolbarFrame.pack(side='bottom', fill='both', padx=10, pady=5, expand=True)
        
        self.tableFrame = Frame(self.left_frame, width=100, height= 100, bg='grey')
        self.tableFrame.grid(row=17, column= 0, columnspan=6, rowspan=100)
        
        # Create all buttons and Entry fields
        self.dsonde_label = Label(self.left_frame,  text="Diameter of the probe [mm]: ").grid(row = 1, column = 0, padx=5, pady=5)
        self.dsonde_entry = Entry(self.left_frame, bd=5, width=20)
        self.poisson_label = Label(self.left_frame, text="Poisson number (0 - 0.5): ").grid(row = 2, column = 0, padx=5, pady=5)
        self.poisson_entry = Entry(self.left_frame, bd=5, width=20)
        
        self.import_button = Button(self.left_frame, text="Open File", command= self.import_data)
        self.module_button = Button(self.left_frame, text="Calculate Modules", command=self.calculate_modules)
        self.plot_avg_button = Button(self.left_frame, text="plot average", command=self.plot_average)
        self.plot_allarms_button = Button(self.left_frame, text="plot all arms", command=self.plot_allarms)
        self.plot_armpairs_button = Button(self.left_frame, text="plot arm pairs", command=self.plot_armpairs)
        self.plot_tableresults_button = Button(self.left_frame, text="results table", command=self.plot_tableresults)

        self.dsonde_entry.grid(row = 1, column = 1, padx=5, pady=5)
        self.poisson_entry.grid(row = 2, column = 1, padx=5, pady=5)
        self.import_button.grid(row = 0, column = 0, padx=5, pady=5)
        self.module_button.grid(row = 1, column = 3, padx=5, pady=5)
        self.plot_avg_button.grid(row = 0, column = 5, padx=5, pady=5)
        self.plot_allarms_button.grid(row = 1, column = 5, padx=5, pady=5)
        self.plot_armpairs_button.grid(row = 2, column = 5, padx=5, pady=5)
        self.plot_tableresults_button.grid(row = 3, column = 5, padx=5, pady=5)
        

        # Define the entry windows for the points calculated
        '''
        self.dict = {}
        for i in range(10):
            self.dict['Typ%s' %i] = Entry(left_frame, bd=5, width=20)'''
            
        self.Typ1_entry = Entry(self.left_frame, bd=5, width=20)
        self.Typ2_entry = Entry(self.left_frame, bd=5, width=20)
        self.Typ3_entry = Entry(self.left_frame, bd=5, width=20)
        self.Typ4_entry = Entry(self.left_frame, bd=5, width=20)
        self.Typ5_entry = Entry(self.left_frame, bd=5, width=20)
        self.Typ6_entry = Entry(self.left_frame, bd=5, width=20)
        self.Typ7_entry = Entry(self.left_frame, bd=5, width=20)
        self.Typ8_entry = Entry(self.left_frame, bd=5, width=20)
        self.Typ9_entry = Entry(self.left_frame, bd=5, width=20)
        self.Typ10_entry = Entry(self.left_frame, bd=5, width=20)
        
        self.Typ1_p1_entry = Entry(self.left_frame, bd=5, width=20)
        self.Typ1_p2_entry = Entry(self.left_frame, bd=5, width=20)
        self.Typ2_p1_entry = Entry(self.left_frame, bd=5, width=20)
        self.Typ2_p2_entry = Entry(self.left_frame, bd=5, width=20)
        self.Typ3_p1_entry = Entry(self.left_frame, bd=5, width=20)
        self.Typ3_p2_entry = Entry(self.left_frame, bd=5, width=20)
        self.Typ4_p1_entry = Entry(self.left_frame, bd=5, width=20)
        self.Typ4_p2_entry = Entry(self.left_frame, bd=5, width=20)
        self.Typ5_p1_entry = Entry(self.left_frame, bd=5, width=20)
        self.Typ5_p2_entry = Entry(self.left_frame, bd=5, width=20)
        self.Typ6_p1_entry = Entry(self.left_frame, bd=5, width=20)
        self.Typ6_p2_entry = Entry(self.left_frame, bd=5, width=20)
        self.Typ7_p1_entry = Entry(self.left_frame, bd=5, width=20)
        self.Typ7_p2_entry = Entry(self.left_frame, bd=5, width=20)
        self.Typ8_p1_entry = Entry(self.left_frame, bd=5, width=20)
        self.Typ8_p2_entry = Entry(self.left_frame, bd=5, width=20)
        self.Typ9_p1_entry = Entry(self.left_frame, bd=5, width=20)
        self.Typ9_p2_entry = Entry(self.left_frame, bd=5, width=20)
        self.Typ10_p1_entry = Entry(self.left_frame, bd=5, width=20)
        self.Typ10_p2_entry = Entry(self.left_frame, bd=5, width=20)
        
        # Set the entry windows to the positions
        self.Typ1_entry.grid(row = 5, column=1, padx=5, pady=5)
        self.Typ1_p1_entry.grid(row = 5, column = 3, padx=5, pady=5)
        self.Typ1_p2_entry.grid(row =5, column = 5, padx=5, pady=5)
        
        self.Typ2_entry.grid(row = 6, column=1, padx=5, pady=5)
        self.Typ2_p1_entry.grid(row = 6, column=3, padx=5, pady=5)
        self.Typ2_p2_entry.grid(row = 6, column=5, padx=5, pady=5)
        
        self.Typ3_entry.grid(row = 7, column = 1, padx=5, pady=5)
        self.Typ3_p1_entry.grid(row = 7, column = 3, padx=5, pady=5)
        self.Typ3_p2_entry.grid(row = 7, column = 5, padx=5, pady=5)
        
        self.Typ4_entry.grid(row = 8, column = 1, padx=5, pady=5)
        self.Typ4_p1_entry.grid(row = 8, column = 3, padx=5, pady=5)
        self.Typ4_p2_entry.grid(row = 8, column = 5, padx=5, pady=5)
        
        self.Typ5_entry.grid(row = 9, column = 1, padx=5, pady=5)
        self.Typ5_p1_entry.grid(row = 9, column = 3, padx=5, pady=5)
        self.Typ5_p2_entry.grid(row = 9, column = 5, padx=5, pady=5)
        
        self.Typ6_entry.grid(row=10, column = 1, padx=5, pady=5)
        self.Typ6_p1_entry.grid(row=10, column = 3, padx=5, pady=5)
        self.Typ6_p2_entry.grid(row=10, column = 5, padx=5, pady=5)
        
        self.Typ7_entry.grid(row=11, column = 1, padx=5, pady=5)
        self.Typ7_p1_entry.grid(row=11, column = 3, padx=5, pady=5)
        self.Typ7_p2_entry.grid(row=11, column = 5, padx=5, pady=5)
        
        self.Typ8_entry.grid(row=12, column = 1, padx=5, pady=5)
        self.Typ8_p1_entry.grid(row=12, column = 3, padx=5, pady=5)
        self.Typ8_p2_entry.grid(row=12, column = 5, padx=5, pady=5)
        
        self.Typ9_entry.grid(row=13, column = 1, padx=5, pady=5)
        self.Typ9_p1_entry.grid(row=13, column = 3, padx=5, pady=5)
        self.Typ9_p2_entry.grid(row=13, column = 5, padx=5, pady=5)
        
        self.Typ10_entry.grid(row=14, column = 1, padx=5, pady=5)
        self.Typ10_p1_entry.grid(row=14, column = 3, padx=5, pady=5)
        self.Typ10_p2_entry.grid(row=14, column = 5, padx=5, pady=5)

        # create three lists for the calculation of the modules. This lists contain the type of module, start and end point.
        self.mode = [self.Typ1_entry, self.Typ2_entry, self.Typ3_entry, self.Typ4_entry, self.Typ5_entry, 
                     self.Typ6_entry, self.Typ7_entry, self.Typ8_entry, self.Typ9_entry, self.Typ10_entry]
        self.start = [self.Typ1_p1_entry, self.Typ2_p1_entry, self.Typ3_p1_entry, self.Typ4_p1_entry, 
                      self.Typ5_p1_entry, self.Typ6_p1_entry, self.Typ7_p1_entry, self.Typ8_p1_entry, 
                      self.Typ9_p1_entry, self.Typ10_p1_entry]
        self.end = [self.Typ1_p2_entry, self.Typ2_p2_entry, self.Typ3_p2_entry, self.Typ4_p2_entry, 
                    self.Typ5_p2_entry, self.Typ6_p2_entry, self.Typ7_p2_entry, self.Typ8_p2_entry, 
                    self.Typ9_p2_entry, self.Typ10_p2_entry]

        for c in range(5,15):
            for r in range(5):
                if r == 0:
                    Label(self.left_frame, text='Type: ').grid(row=c, column=r)
                if r == 2:
                    Label(self.left_frame, text='start: ').grid(row=c, column=r)
                if r == 4:
                    Label(self.left_frame, text='end: ').grid(row=c, column=r)

        #initiate Figure
        self.fig = Figure(figsize=(13, 13))
        self.ax1 = self.fig.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.right_frame)
        self.canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self.toolbarFrame)
        self.toolbar.update()
        self.toolbar.pack(side='top', fill='both', expand=1)

        # Create table to show data
        self.tree = ttk.Treeview(self.tableFrame, show='headings')
        self.tree.pack(side='top', fill='both', expand=1)

        self.colnames = ['Pressure [kPa]', 'arm1 [mm]', 'arm2 [mm]', 'arm3 [mm]', 'arm4 [mm]', 'arm5 [mm]', 'arm6 [mm]', 'AVG [mm]']
        self.tree['columns']=(self.colnames)
        self.tree.column('Pressure [kPa]', anchor='center', width=120)
        self.tree.column('arm1 [mm]', anchor='center', width=100)
        self.tree.column('arm2 [mm]', anchor='center', width=100)
        self.tree.column('arm3 [mm]', anchor='center', width=100)
        self.tree.column('arm4 [mm]', anchor='center', width=100)
        self.tree.column('arm5 [mm]', anchor='center', width=100)
        self.tree.column('arm6 [mm]', anchor='center', width=100)
        self.tree.column('AVG [mm]', anchor='center', width=100)
        
        self.tree.heading('Pressure [kPa]', text='Pressure [kPa]', anchor='center')
        self.tree.heading('arm1 [mm]', text='arm1 [mm]', anchor='center')
        self.tree.heading('arm2 [mm]', text='arm2 [mm]', anchor='center')
        self.tree.heading('arm3 [mm]', text='arm3 [mm]', anchor='center')
        self.tree.heading('arm4 [mm]', text='arm4 [mm]', anchor='center')
        self.tree.heading('arm5 [mm]', text='arm5 [mm]', anchor='center')
        self.tree.heading('arm6 [mm]', text='arm6 [mm]', anchor='center')
        self.tree.heading('AVG [mm]', text='AVG [mm]', anchor='center')




    def import_data(self):
        self.filepath = askopenfilename(filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")])

        self.df = read_csv(self.filepath, skiprows = 35)
        self.df = self.df.drop([0])
        self.df = self.df.drop('Line No.', axis=1)
        self.pres = to_numeric(self.df['TPC Average'], downcast="float")
        self.arm1 = to_numeric(self.df['Arm 1'], downcast="float")
        self.arm2 = to_numeric(self.df['Arm 2'], downcast="float")
        self.arm3 = to_numeric(self.df['Arm 3'], downcast="float")
        self.arm4 = to_numeric(self.df['Arm 4'], downcast="float")
        self.arm5 = to_numeric(self.df['Arm 5'], downcast="float")
        self.arm6 = to_numeric(self.df['Arm 6'], downcast="float")
        self.arm_avg = (self.arm1 + self.arm2 + self.arm3 + self.arm4 + self.arm5 + self.arm6) / 6
        self.df_data = concat([self.pres, self.arm1,  self.arm2,  self.arm3,  self.arm4,  self.arm5,  self.arm6,  self.arm_avg], axis=1)
    
        for row in range(2, len(self.df_data)):
            self.tree.insert('', 'end', values=(self.df_data.iloc[row].values[0], 
                                                self.df_data.iloc[row].values[1], 
                                                self.df_data.iloc[row].values[2], 
                                                self.df_data.iloc[row].values[3],
                                                self.df_data.iloc[row].values[4],
                                                self.df_data.iloc[row].values[5],
                                                self.df_data.iloc[row].values[6],
                                                self.df_data.iloc[row].values[7].round(4)))   



    def calculate_modules(self):
        self.test_type = {}
        self.G = []
        self.E = []
        self.df_calc = DataFrame()
        self.df_raw = DataFrame()

        for x in range(len(self.mode)):
            if self.mode[x].get() != '':
                self.test_type[self.mode[x].get()] = array([int(self.start[x].get()), int(self.end[x].get())])

        #Convert the entry for the diameter to a float and check if it worked
        try:
            d_sond = float(self.dsonde_entry.get())
        except:
            messagebox.showinfo("Error!", "Der Durchmesser muss eine Zahl sein!")
            
        #Convert the entry for the poisson number to a float and check if it worked    
        try:
            poisson = float(self.poisson_entry.get())
            if poisson < 0 or poisson > 0.5:
                messagebox.showinfo("Error!", "Die Poissonzahl muss eine Zahl zwischen 0 und 0.5 sein!")
        except:
            messagebox.showinfo("Error!", "Die Poissonzahl muss eine Zahl sein!")
        
        counter = [1,2]
        for case in self.test_type:
            #calculate pressure
            p_start = self.pres[self.test_type[case][0]].round(0)
            p_end = self.pres[self.test_type[case][1]].round(0)
            delta_p = p_end - p_start
            pressure = [p_start, p_end, delta_p, ' ', ' ']
            
            #calculate arm 1/4
            d_start_14 = self.arm1[self.test_type[case][0]] + self.arm4[self.test_type[case][0]] + d_sond
            d_end_14 =  self.arm1[self.test_type[case][1]] + self.arm4[self.test_type[case][1]] + d_sond
            delta_d_14 = d_end_14 - d_start_14
            
            SD_14 = (self.arm1[self.test_type[case][0]] + self.arm4[self.test_type[case][0]] + d_sond) / \
                    (((self.arm1[self.test_type[case][1]] + self.arm4[self.test_type[case][1]]) / 2 - \
                     (self.arm1[self.test_type[case][0]] + self.arm4[self.test_type[case][0]]) / 2)*2)
            
            G_14 = int(delta_p * SD_14 / 2 / 1000)
            E_14 = int(G_14 * 2 * (1+poisson))
            arm14 = [d_start_14, d_end_14, delta_d_14, G_14, E_14]
            arm14 = [round(num, 3) for num in arm14]
            
            #calculate arm 2/5
            d_start_25 = self.arm2[self.test_type[case][0]] + self.arm5[self.test_type[case][0]] + d_sond
            d_end_25 =  self.arm2[self.test_type[case][1]] + self.arm5[self.test_type[case][1]] + d_sond
            delta_d_25 = d_end_25 - d_start_25
            
            SD_25 = (self.arm2[self.test_type[case][0]] + self.arm5[self.test_type[case][0]] + d_sond) / \
                    (((self.arm2[self.test_type[case][1]] + self.arm5[self.test_type[case][1]]) / 2 - \
                     (self.arm2[self.test_type[case][0]] + self.arm5[self.test_type[case][0]]) / 2)*2)
            
            G_25 = int(delta_p * SD_25 / 2 / 1000)
            E_25 = int(G_25 * 2 * (1+poisson))
            arm25 = [d_start_25, d_end_25, delta_d_25, G_25, E_25]
            arm25 = [round(num, 3) for num in arm25]
            
            #calculate arm 3/6
            d_start_36 = self.arm3[self.test_type[case][0]] + self.arm6[self.test_type[case][0]] + d_sond
            d_end_36 =  self.arm3[self.test_type[case][1]] + self.arm6[self.test_type[case][1]] + d_sond
            delta_d_36 = d_end_36 - d_start_36
            
            SD_36 = (self.arm3[self.test_type[case][0]] + self.arm6[self.test_type[case][0]] + d_sond) / \
                    (((self.arm3[self.test_type[case][1]] + self.arm6[self.test_type[case][1]]) / 2 - \
                     (self.arm3[self.test_type[case][0]] + self.arm6[self.test_type[case][0]]) / 2)*2)
            
            G_36 = int(delta_p * SD_36 / 2 / 1000)
            E_36 = int(G_36 * 2 * (1+poisson))
            arm36 = [d_start_36, d_end_36, delta_d_36, G_36, E_36]
            arm36 = [round(num, 3) for num in arm36]
            
            #calculate average arms
            d_start_all = self.arm_avg[self.test_type[case][0]] * 2 + d_sond
            d_end_all =  self.arm_avg[self.test_type[case][1]] * 2 + d_sond
            delta_d_all = d_end_all - d_start_all
            SD = (self.arm_avg[self.test_type[case][0]] * 2 + d_sond) / ((self.arm_avg[self.test_type[case][1]] - self.arm_avg[self.test_type[case][0]]) * 2)
            G_temp = int(delta_p * SD / 2 / 1000)
            self.G.append(G_temp)
            E_temp = int(G_temp * 2 * (1+poisson))
            self.E.append(E_temp)
            G_all = int(delta_p * SD / 2 / 1000)
            E_all = int(G_all * 2 * (1+poisson))
            arm_all = [d_start_all, d_end_all, delta_d_all, G_all, E_all]
            arm_all = [round(num, 3) for num in arm_all]
            
            #save the results in a dataframe
            case_string = [str(case),"","","",""]
            definition = ["start","end","delta","G-module","E-module"]
            table_temp = DataFrame({'':case_string , ' ':definition, 'Pressure [kPa]':pressure, 'arms 1/4 [mm]':arm14, 'arms 2/5 [mm]':arm25, \
                                       'arms 3/6 [mm]':arm36, 'arm average  [mm]':arm_all})
            table_temp = concat([table_temp], keys=[str(case)])
            self.df_calc = concat([self.df_calc, table_temp])
            
            #create dataframe with raw data and save it
            pres_raw = [p_start, p_end]
            arm1_raw = [self.arm1[self.test_type[case][0]], self.arm1[self.test_type[case][1]]]
            arm2_raw = [self.arm2[self.test_type[case][0]], self.arm2[self.test_type[case][1]]]
            arm3_raw = [self.arm3[self.test_type[case][0]], self.arm3[self.test_type[case][1]]]
            arm4_raw = [self.arm4[self.test_type[case][0]], self.arm4[self.test_type[case][1]]]
            arm5_raw = [self.arm5[self.test_type[case][0]], self.arm5[self.test_type[case][1]]]
            arm6_raw = [self.arm6[self.test_type[case][0]], self.arm6[self.test_type[case][1]]]
            
            table_temp_raw = DataFrame({'':counter, 'Pressure [kPa]':pres_raw, 'Arm 1 [mm]':arm1_raw, 'Arm 2 [mm]':arm2_raw, \
                                          'Arm 3 [mm]':arm3_raw, 'Arm 4 [mm]':arm4_raw, 'Arm 5 [mm]':arm5_raw, \
                                          'Arm 6 [mm]':arm6_raw})
                
            self.df_raw = concat([self.df_raw, table_temp_raw])
            
            counter[0]+=2
            counter[1]+=2
            



    def plot_average(self):
        ##### plot figure arm average #####
        self.ax1.cla()
        
        points_avg = self.ax1.scatter(self.arm_avg, self.pres, label = 'Average arms', facecolors='royalblue', edgecolors='black')
        self.ax1.set_xlabel('Radial Displacement [mm]', fontsize=15)
        self.ax1.set_ylabel('Pressure [kPa]', fontsize=15)
        self.ax1.set_title('Deformation (average arms) vs Pressure', fontsize = 30)
        self.ax1.grid(True)
        self.ax1.set_facecolor("floralwhite")
        self.ax1.legend(fontsize=15, loc = 'lower right');
        
  
        labels = list(range(1,len(self.arm_avg)))
        cursor = mplcursors.cursor(points_avg)
        cursor.connect("add", lambda sel: sel.annotation.set_text('Point ' + str(labels[sel.target.index])))
        
        # Plot the lines of the calculated modules
        try:
            count1 = 0
            for i in self.test_type:
                x_values = [self.arm_avg[self.test_type[i][0]], self.arm_avg[self.test_type[i][1]]];
                y_values = [self.pres[self.test_type[i][0]], self.pres[self.test_type[i][1]]];
                self.ax1.plot(x_values, y_values, '-or')
                self.ax1.annotate(list(self.test_type.keys())[count1], (self.arm_avg[self.test_type[i][0]], self.pres[self.test_type[i][0]]), fontsize = 15,\
                             textcoords="offset points", xytext=(10,-10))
                count1 += 1
    
            count2 = 0
            text_final = ''
            for ii in self.test_type:
                text_final += (ii + ': G = ' + str(self.G[count2]) + ' MPa, E = ' + str(self.E[count2]) + ' MPa' + str("\n") + str("\n"))
                count2 += 1
            self.ax1.text(0.02, 0.96, text_final[:-2], ha='left', va='top',\
                     transform=self.ax1.transAxes, fontsize = 15, bbox=dict(facecolor='white', alpha=1));
           
        except:
            None
            
        self.canvas.draw()





    def plot_allarms(self):
        ##### plot figure all arms #####

        self.ax1.cla()
        self.points_all1 = self.ax1.scatter(self.arm1, self.pres, label = 'Arm 1', facecolors='yellow', edgecolors='black')
        self.points_all2 = self.ax1.scatter(self.arm2, self.pres, label = 'Arm 2', facecolors='orange', edgecolors='black')
        self.points_all3 = self.ax1.scatter(self.arm3, self.pres, label = 'Arm 3', facecolors='red', edgecolors='black')
        self.points_all4 = self.ax1.scatter(self.arm4, self.pres, label = 'Arm 4', facecolors='green', edgecolors='black')
        self.points_all5 = self.ax1.scatter(self.arm5, self.pres, label = 'Arm 5', facecolors='blue', edgecolors='black')
        self.points_all6 = self.ax1.scatter(self.arm6, self.pres, label = 'Arm 6', facecolors='black', edgecolors='black')
        self.ax1.legend(fontsize=15, loc = 'lower right');
        mplcursors.cursor([self.points_all1, self.points_all2, self.points_all3, self.points_all4, self.points_all5, self.points_all6])
        
        self.ax1.set_xlabel('Radial Displacement [mm]', fontsize=15)
        self.ax1.set_ylabel('Pressure [kPa]', fontsize=15)
        self.ax1.set_facecolor("floralwhite")
        self.ax1.set_title('Deformation (all arms) vs Pressure', fontsize = 30)
        self.ax1.grid(True)
        
        self.canvas.draw()
        
        
        
        
        
        
    def plot_armpairs(self):
    ##### plot figure arm pairs #####
    
        self.ax1.cla()
        self.points_pair1_4 = self.ax1.scatter((self.arm1+self.arm4)/2,self.pres, facecolors='yellow', edgecolors='black', label = 'Armpair 1 + 4')
        self.points_pair2_5 = self.ax1.scatter((self.arm2+self.arm5)/2,self.pres, facecolors='red', edgecolors='black', label = 'Armpair 2 + 5')
        self.points_pair3_6 = self.ax1.scatter((self.arm3+self.arm6)/2,self.pres, facecolors='blue', edgecolors='black', label = 'Armpair 3 + 6')
        self.ax1.legend(fontsize=15, loc = 'lower right');
        mplcursors.cursor([self.points_pair1_4, self.points_pair2_5, self.points_pair3_6])
    
        self.ax1.set_xlabel('Radial Displacement [mm]', fontsize=15)
        self.ax1.set_ylabel('Pressure [kPa]', fontsize=15)
        self.ax1.set_facecolor("floralwhite")
        self.ax1.set_title('Deformation (armpairs) vs Pressure', fontsize = 30)
        self.ax1.grid(True)
        
        self.canvas.draw()
    
    

    
   
    def plot_tableresults(self):

        self.newWindow       = Toplevel()
        self.tree2 = ttk.Treeview(self.newWindow, show='headings')
        self.tree2.pack(side='bottom', fill='both', padx=10, pady=5, expand=True)
        
        self.table = pt = Table(self.tree2, dataframe=self.df_calc,
                                    showtoolbar=True, showstatusbar=True)
        pt.show()



# Initiate the program
root = Tk()
my_gui = my_program(root)
root.mainloop()