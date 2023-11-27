import calendar
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import os
import cv2


def generate_dates_in_current_month():
    today = datetime.today()
    _, last_day_of_month = calendar.monthrange(today.year, today.month)

    date_array = ["Name"]
    current_date = datetime(today.year, today.month, 1)

    while current_date <= datetime(today.year, today.month, last_day_of_month):
        date_array.append(current_date.strftime("%Y-%m-%d"))
        current_date += timedelta(days=1)

    return date_array

path="ImageAttendence"
images=[]
classNames=[]
myList=os.listdir(path)
# print(myList)

for cl in myList:
    currImg=cv2.imread(f'{path}/{cl}')
    images.append(currImg)
    classNames.append(os.path.splitext(cl)[0])
# print(classNames)
columns = generate_dates_in_current_month()

def generate_attendence_data():
    path="Logs"
    my_list_of_paths=os.listdir(path)
    global classNames, columns
    data={'Name':classNames}
    df = pd.DataFrame(data, columns=columns)
    # print(my_list_of_paths)
    for i in my_list_of_paths:
        Marked_Names=[]
        with open(path+"/"+i, "r") as f1:
            lines=f1.readlines()
            for line in lines:
                try:
                    name=(line.split())[0]
                    if(name not in Marked_Names):
                        Marked_Names.append(name)
                except:
                    pass
        try:
            Marked_Names.remove("Intruder_Alert")
            Marked_Names.remove("ALert")
        except:
            pass
        # print(i,end="\t")
        # print(Marked_Names)
        # print("\n")
        i=(i.split('s'))[1]
        i=(i.split('.'))[0]
        # print(i,"\t\t",Marked_Names)
        for name in Marked_Names:
            # print(df)
            df.loc[df['Name']==name, i]="Present"
            # print(df.loc[df['Name']==name, i])
            # print(df)
    df=df.T
    df = df.replace(np.nan, "Abscent")
    return df
df=generate_attendence_data()
# print(df)

# tkinter
import tkinter as tk
from tkinter import ttk
import pandas as pd

class DataFrameViewer(tk.Tk):
    def __init__(self, data_frame):
        super().__init__()

        self.title("DataFrame Viewer")
        self.geometry("800x600")

        self.data_frame = data_frame

        self.create_widgets()

    def create_widgets(self):
        # Create a Treeview widget
        tree = ttk.Treeview(self, columns=['Index'] + list(self.data_frame.columns), show="headings")

        # Add column headings
        tree.heading('Index', text='Index')
        for column in self.data_frame.columns:
            tree.heading(column, text=column)
            tree.column(column, anchor="center")

        # Insert data into the Treeview
        for i, row in self.data_frame.iterrows():
            tree.insert("", "end", values=[i] + list(row))

        # Add Treeview to the window
        tree.pack(expand=True, fill="both")

df = pd.DataFrame(df)

# Create the Tkinter application and pass the DataFrame
app = DataFrameViewer(df)

# Run the Tkinter event loop
app.mainloop()
