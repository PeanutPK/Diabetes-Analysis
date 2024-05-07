import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import customtkinter as ctk
from tkinter import Menu
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

sns.set_theme(rc={'figure.figsize': (3, 3)})
plt.rcParams['figure.figsize'] = [3, 3]

FILE_CSV = pd.read_csv('data/diabetes.csv')
REPLACE = {1: 'Diabetic', 0: 'Not Diabetic'}
FILE_CSV['Outcome'] = FILE_CSV['Outcome'].replace(REPLACE)
NAMES = ['BMI', 'BloodPressure', 'Age', 'Glucose']


class DiabetesModel:
    """
    Module for computing and sometimes draw a graph (when the pattern is done)
    """

    @staticmethod
    def load_graph(master: ctk.CTk, name: str):
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

        sns.histplot(FILE_CSV, x=name, hue='Outcome', multiple='stack')

        ax.set(xlabel='', ylabel='Frequency')

        plt.title('Diabetes Outcome for ' + name)
        canvas = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas.get_tk_widget().pack(side=ctk.TOP, fill='both', expand=True)
        canvas.draw()
        graph_frame.pack(side=ctk.TOP, expand=True, fill='both')

    @staticmethod
    def describe(master: ctk.CTkTabview, name: str):
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

        label = ctk.CTkLabel(master, text=FILE_CSV[name].describe())
        label.pack(side=ctk.TOP, expand=True, fill='both', anchor='n')

    @staticmethod
    def load_storytelling_hist(master: ctk.CTkScrollableFrame):
        """Load all histograms only for storytelling page"""
        for name in NAMES:
            fig, ax = plt.subplots()

            sns.histplot(FILE_CSV, x=name, hue='Outcome',
                         multiple='stack')

            ax.set(ylabel='Frequency')

            plt.title('Outcome for ' + name)
            canvas = FigureCanvasTkAgg(fig, master=master)
            canvas.get_tk_widget().pack(side=ctk.TOP, expand=True, fill='both')
            canvas.draw()

    @staticmethod
    def load_storytelling_stat(master):

        for name in NAMES:
            label = ctk.CTkLabel(master,
                                 text=f"{FILE_CSV[name].describe()}\n")
            label.pack(side=ctk.TOP)

    @staticmethod
    def load_correlations_scatter(master, x, y):

        fig, ax = plt.subplots()

        coefficient = np.corrcoef(FILE_CSV[x], FILE_CSV[y])[0, 1]

        sns.scatterplot(FILE_CSV, x=x, y=y, hue='Outcome')

        ax.set(xlabel=x, ylabel=y)

        plt.title(f"{x} vs {y} & corr coeff: {coefficient:.2f}")

        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas.get_tk_widget().pack(side=ctk.TOP, fill='both')

        canvas.draw()

    def load_storytelling_corr(self, master):

        self.load_correlations_scatter(master, 'BMI', 'BloodPressure')
        self.load_correlations_scatter(master, 'Glucose', 'Insulin')
        self.load_correlations_scatter(master, 'Glucose', 'BMI')

    @staticmethod
    def load_pie_chart(master):

        diabetics = FILE_CSV['Outcome'].value_counts()
        fig, ax = plt.subplots()

        ax.pie(diabetics, labels=diabetics.index, autopct='%1.1f%%')
        plt.title('Ratio of Diabetics and Non-Diabetics')

        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas.get_tk_widget().pack(side=ctk.TOP, expand=True, fill='both')

        canvas.draw()

    @staticmethod
    def load_bar_graph_bmi(master):
        pass


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
