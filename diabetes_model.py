import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import customtkinter as ctk
from tkinter import Menu
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

NAMES = ['BMI', 'BloodPressure', 'Age', 'Glucose']


class Data:
    def __init__(self):
        # Initialize graph and data
        sns.set_theme(rc={'figure.figsize': (3, 3)})
        plt.rcParams['figure.figsize'] = [3, 3]
        REPLACE = {1: 'Diabetic', 0: 'Not Diabetic'}

        self.df = pd.read_csv('data/diabetes.csv')
        self.df['Outcome'] = self.df['Outcome'].replace(REPLACE)

    def get_column(self):
        return list(self.df.columns)

    @staticmethod
    def bar_filter(x):
        if x < 18:
            return 'Underweight'
        if 18 <= x <= 24:
            return 'Normal'
        if x > 25:
            return 'Obese'
    
    def get_bmi_range(self):
        new_df = self.df.copy()
        new_df['RangeBMI'] = self.df['BMI'].apply(self.bar_filter)
        return new_df


class DiabetesModel(Data):
    """
    Module for computing and sometimes draw a graph (when the pattern is done)
    """
    def __init__(self):
        super().__init__()

    def load_graph_outcome(self, master: ctk.CTk, name: str):
        """
        Load a graph from the input name and pack it to the origin root.
        :param master: Original frame or root.
        :param name: Name of the data to display histogram
        """
        try:
            widget = master.winfo_children()[2]
            widget.destroy()
        except IndexError:
            pass

        graph_frame = ctk.CTkFrame(master)

        fig, ax = plt.subplots()

        sns.histplot(self.df, x=name, hue='Outcome', multiple='stack')

        ax.set(xlabel='', ylabel='Frequency')

        plt.title('Diabetes Outcome for ' + name)
        canvas = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas.get_tk_widget().pack(side=ctk.TOP, fill='both', expand=True)
        canvas.draw()
        graph_frame.pack(side=ctk.TOP, expand=True, fill='both')

    def describe(self, master: ctk.CTkTabview, name: str):
        """
        Describe all descriptive statistics and dispersion from the csv file.
        :param master: Frame or Tab for packing the item inside.
        :param name: Name of the attribute to pull information from.
        """
        try:
            widget = master.winfo_children()[2]
            widget.destroy()
        except IndexError:
            pass

        label = ctk.CTkLabel(master, text=self.df[name].describe())
        label.pack(side=ctk.TOP, expand=True, fill='both', anchor='n')

    def load_storytelling_hist(self, master: ctk.CTkScrollableFrame):
        """Load all histograms only for storytelling page"""
        for name in NAMES:
            fig, ax = plt.subplots()

            sns.histplot(self.df, x=name, hue='Outcome',
                         multiple='stack')

            ax.set(ylabel='Frequency')

            plt.title('Outcome for ' + name)
            canvas = FigureCanvasTkAgg(fig, master=master)
            canvas.get_tk_widget().pack(side=ctk.TOP, expand=True, fill='both')
            canvas.draw()

    def load_storytelling_stat(self, master):

        for name in NAMES:
            label = ctk.CTkLabel(master,
                                 text=f"{self.df[name].describe()}\n")
            label.pack(side=ctk.TOP)

    def load_correlations_scatter(self, master, x, y):

        fig, ax = plt.subplots()

        coefficient = np.corrcoef(self.df[x], self.df[y])[0, 1]

        sns.scatterplot(self.df, x=x, y=y, hue='Outcome')

        ax.set(xlabel=x, ylabel=y)

        plt.title(f"{x} vs {y} & corr coeff: {coefficient:.2f}")

        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas.get_tk_widget().pack(side=ctk.TOP, fill='both')

        canvas.draw()

    def load_storytelling_corr(self, master):

        self.load_correlations_scatter(master, 'BMI', 'BloodPressure')
        self.load_correlations_scatter(master, 'Glucose', 'Insulin')
        self.load_correlations_scatter(master, 'Glucose', 'BMI')

    def load_pie_chart(self, master):

        diabetics = self.df['Outcome'].value_counts()
        fig, ax = plt.subplots()

        ax.pie(diabetics, labels=diabetics.index, autopct='%1.1f%%')
        plt.title('Ratio of Diabetics and Non-Diabetics')

        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas.get_tk_widget().pack(side=ctk.TOP, expand=True, fill='both')

        canvas.draw()

    @staticmethod
    def load_bar_graph_bmi(master):
        pass

    @staticmethod
    def load_graph(master, x, y):
        frame = ctk.CTkFrame(master=master)


if __name__ == '__main__':
    root = ctk.CTk()
    root.title('Graph Demo Loader')

    scrollable = ctk.CTkScrollableFrame(root)
    scrollable.pack(expand=True, fill='both')

    # DiabetesModel.load_graph(root, 'BMI')

    # DiabetesModel().load_storytelling_hist(scrollable)
    # DiabetesModel().load_storytelling_stat(scrollable)
    # DiabetesModel().load_storytelling_corr(scrollable)
    # DiabetesModel().load_pie_chart(scrollable)

    DiabetesModel().load_bar_graph_bmi()

    root.mainloop()
