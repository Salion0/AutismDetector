import tkinter as tk
from tkinter import ttk
from Class.AutismClassifier import AutismClassifier
import pandas as pd
import pickle


class gui:
    # Define _window
    _window = tk.Tk()
    _window.minsize(width=500, height=300)
    _window.columnconfigure(0, weight=1, minsize=75)
    _window.rowconfigure(0, weight=1, minsize=50)
    _window.rowconfigure(1, weight=1, minsize=50)
    _window.rowconfigure(2, weight=1, minsize=50)

    # Define all the variables to handle
    _a1 = tk.StringVar()
    _a2 = tk.StringVar()
    _a3 = tk.StringVar()
    _a4 = tk.StringVar()
    _a5 = tk.StringVar()
    _a6 = tk.StringVar()
    _a7 = tk.StringVar()
    _a8 = tk.StringVar()
    _a9 = tk.StringVar()
    _a10 = tk.StringVar()
    _a_scores = [_a1, _a2, _a3, _a4, _a5, _a6, _a7, _a8, _a9, _a10]
    _age = tk.StringVar()
    _gender = tk.StringVar()
    _ethnicity = tk.StringVar()
    _country = tk.StringVar()
    _jaundice = tk.StringVar()
    _family_member_pdd = tk.StringVar()
    _class_lbl = None
    _class = None
    _classifier = AutismClassifier()

    def _classify(self):
        patient = self._get_tuple()
        self._classifier.load_model(file_name="dump/model")
        prediction = self._classifier.classify_tuples(tuples=patient)
        text = "ASD: "
        print(prediction)
        if prediction.item() == 0:
            text = text + "No"
        elif prediction.item() == 1:
            text = text + "Yes"
        self._class_lbl.config(text=text)

    def _get_tuple(self):
        # Create a series from the df
        columns_file = open("dump/columns", "rb")
        columns = pickle.load(columns_file)

        dict = {}

        # a_scores
        i = 0
        for score in columns[0:10]:
            dict[score] = self._a_scores[i].get()
            i = i + 1

        dict["age"] = self._age.get()

        if self._gender.get() == "F":
            dict["gender"] = 0
        elif self._gender.get() == "M":
            dict["gender"] = 1

        if self._jaundice.get() == "No":
            dict["jaundice"] = 0
        elif self._jaundice.get() == "Yes":
            dict["jaundice"] = 1

        if self._family_member_pdd.get() == "No":
            dict["family member with PDD"] = 0
        elif self._family_member_pdd.get() == "Yes":
            dict["family member with PDD"] = 1


        # ethnicity
        for column in columns[14:24]:
            if column == self._ethnicity.get():
                dict[column] = "1"
            else:
                dict[column] = "0"

        # country
        for column in columns[24:]:
            if column == self._country.get():
                dict[column] = "1"
            else:
                dict[column] = "0"

        series = pd.Series(dict)
        tuples = pd.DataFrame(series).T
        return tuples

    def _get_values(self):
        print("A1: " + self._a1.get())
        print("A2: " + self._a2.get())
        print("Ethnicity: " + self._ethnicity.get())
        self._set_class_label()

    def _set_class_label(self):
        self._class_lbl.config(text=self._class)

    def make_window(self):
        # Define frames
        frame_a = tk.Frame(master=self._window, bg="#4f4e4c", bd=10)
        frame_b = tk.Frame(master=self._window, bg="#4f4e4c", bd=10)
        frame_c = tk.Frame(master=self._window, bg="#4f4e4c", bd=10)

        frame_a.grid(row=0, column=0, sticky="nsew")
        frame_b.grid(row=1, column=0, sticky="nsew")
        frame_c.grid(row=2, column=0, sticky="nsew")

        # Create element in frame a : A1_score,A2_score,exc...

        for i in range(0, 10):
            frame_a.columnconfigure(i, weight=1)
            frame_a.rowconfigure(i, weight=1)
            text = "A" + f"{i + 1}"

            lbl = tk.Label(master=frame_a, text=text, bg='#e2ffc6')
            lbl.grid(row=0, column=i, sticky="nsew", padx=10)

            rd_bttn_name = "a" + f"{i + 1}"
            rd_bttn_frame = tk.Frame(master=frame_a, name=rd_bttn_name,bg="#4f4e4c")
            rd_bttn_frame.grid(row=1, column=i, sticky="nsew", padx=10)
            for j in range(0, 2):
                rd_bttn = tk.Radiobutton(master=rd_bttn_frame, variable=self._a_scores[i], text=j, value=j,bg="#4f4e4c")
                rd_bttn.pack()

        # Define elements in frame b: age, Gender, Ethinicity, Jaundice, Family member with PDD
        frame_b.rowconfigure(0, weight=1)
        frame_b.rowconfigure(1, weight=1)
        labels = ["Age", "Gender","Country","Ethinicity", "Jaundice", "Family Member with PDD"]
        text_var_array = [self._age, self._gender,self._country, self._ethnicity, self._jaundice, self._family_member_pdd]

        i = 0

        columns_file = open("dump/columns", "rb")
        columns = pickle.load(columns_file)


        age_entry = tk.Entry(master=frame_b, textvariable=self._age)
        gender_cbx = ttk.Combobox(master=frame_b, textvariable=self._gender)
        ethnicity_cbx = ttk.Combobox(master=frame_b, textvariable= self._ethnicity)
        jaundice_cbx = ttk.Combobox(master=frame_b, textvariable=self._jaundice)
        family_cbx = ttk.Combobox(master=frame_b, textvariable=self._family_member_pdd)
        country_cbx = ttk.Combobox(master=frame_b, textvariable=self._country)


        eth_list = []
        for eth in columns[14:24]:
            eth_list.append(eth)
        eth_val = tuple(eth_list)
        ethnicity_cbx['values'] = eth_val


        country_list = []
        for country in columns[24:]:
            country_list.append(country)
        country_val = tuple(country_list)

        gender_cbx['values'] = ('F', 'M')
        country_cbx['values'] = country_val
        family_cbx['values'] = ("Yes","No")
        jaundice_cbx['values'] = ("Yes","No")
        #gender_cbx['values'] = ()



        for label in labels:
            frame_b.columnconfigure(i, weight=1)

            lbl = tk.Label(master=frame_b, text=label, bg='#e2ffc6')
            lbl.grid(row=0, column=i, sticky="nsew", padx=10)

            entry = tk.Entry(master=frame_b, textvariable=text_var_array[i])


            #entry.grid(row=1, column=i, sticky="nsew", padx=10)

            i = i + 1
        # End FOR#
        age_entry.grid(row=1, column=0, sticky="nsew", padx=10)
        gender_cbx.grid(row=1, column=1, sticky="nsew", padx=10)
        country_cbx.grid(row=1,column=2,sticky="nsew",padx=10)
        ethnicity_cbx.grid(row=1, column=3, sticky="nsew", padx=10)
        jaundice_cbx.grid(row=1, column=4, sticky="nsew", padx=10)
        family_cbx.grid(row=1, column=5, sticky="nsew", padx=10)

        #Define frame class_lbl = Nonee_c elements: classifiy button, Label: "ASD:",label Class (hidden)
        frame_c.columnconfigure(0, weight=1)
        frame_c.columnconfigure(1, weight=1)

        clf_bttn = tk.Button(master=frame_c, text="Classify", command=self._classify)
        self._class_lbl = tk.Label(master=frame_c, text="Class/ASD")

        clf_bttn.grid(row=0, column=0, sticky="nsew")
        self._class_lbl.grid(row=0, column=1, sticky="nsew")

    def start(self):
        self._window.mainloop()

