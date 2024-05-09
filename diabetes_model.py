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
        """Initialize data for plotting graph"""
        sns.set_theme(rc={'figure.figsize': (3, 3)})
        plt.rcParams['figure.figsize'] = [3, 3]
        REPLACE = {1: 'Diabetic', 0: 'Not Diabetic'}

        self.df = pd.read_csv('data/diabetes.csv')
        self.df['Outcome'] = self.df['Outcome'].replace(REPLACE)

    def get_column(self):
        return list(self.df.columns)

    @staticmethod
    def bar_filter(x):
        """Filter function for categorizing bmi data"""
        if x < 18.5:
            return 'Underweight'
        if 18.5 <= x < 25:
            return 'Normal'
        if 25 <= x < 30:
            return 'Overweight'
        if 30 <= x < 35:
            return 'Obese'
        if x >= 35:
            return 'Extremely Obese'

    def get_bmi_range(self):
        bmi_value = ['Underweight', 'Normal', 'Overweight',
                     'Obese', 'Extremely Obese']
        new_df = self.df.copy()
        new_df['RangeBMI'] = self.df['BMI'].apply(self.bar_filter)
        sorted_labels = (new_df['RangeBMI'].astype('category').cat.
                         reorder_categories(bmi_value))
        new_df['RangeBMI'] = sorted_labels
        return new_df


class DiabetesModel(Data):
    """
    Module for computing and sometimes draw a graph (when the pattern is done)
    """
    def __init__(self):
        super().__init__()
        self.bmi_range = self.get_bmi_range()

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
        """Load all histograms only for storytelling page
        :param master: Frame or Tab for packing the item inside.
        """
        for name in NAMES:
            fig, ax = plt.subplots()

            sns.histplot(self.df, x=name, hue='Outcome', multiple='stack')

            ax.set(ylabel='Frequency')

            plt.title('Outcome for ' + name)
            canvas = FigureCanvasTkAgg(fig, master=master)
            canvas.get_tk_widget().pack(side=ctk.TOP, expand=True, fill='both')
            canvas.draw()

    def load_storytelling_stat(self, master):
        """Show descriptive statistics only for storytelling page
        :param master: Frame or Tab for packing the item inside.
        """
        for name in NAMES:
            label = ctk.CTkLabel(master, text=f"{self.df[name].describe()}\n")
            label.pack(side=ctk.TOP)

    def load_correlations_scatter(self, master, x, y):
        """
        Plot a scatter plot with its correlation.
        :param master: Frame or Tab for packing the item inside.
        :param x: X-axis attribute for plotting a graph.
        :param y: Y-axis attribute for plotting a graph.
        """
        fig, ax = plt.subplots()

        coefficient = np.corrcoef(self.df[x], self.df[y])[0, 1]

        sns.scatterplot(self.df, x=x, y=y, hue='Outcome')

        ax.set(xlabel=x, ylabel=y)

        plt.title(f"{x} vs {y} & corr coeff: {coefficient:.2f}")

        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas.get_tk_widget().pack(side=ctk.TOP, fill='both')

        canvas.draw()

    def load_storytelling_corr(self, master):
        """
        Function that load all scatterplot that use in story telling.
        :param master: Frame or Tab for packing the item inside.
        """
        self.load_correlations_scatter(master, 'BMI', 'BloodPressure')
        self.load_correlations_scatter(master, 'Glucose', 'Insulin')
        self.load_correlations_scatter(master, 'Glucose', 'BMI')

    def load_pie_chart(self, master):
        """
        Function that loads pie chart that uses in story telling.
        :param master: Frame or Tab for packing the item inside.
        """
        diabetics = self.df['Outcome'].value_counts()
        fig, ax = plt.subplots()

        ax.pie(diabetics, labels=diabetics.index, autopct='%1.1f%%')
        plt.title('Ratio of Diabetics and Non-Diabetics')

        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas.get_tk_widget().pack(side=ctk.TOP, expand=True, fill='both')

        canvas.draw()

    def load_bar_graph_bmi(self, master):
        """
        Function that plots a graph of bmi range that uses in story telling.
        :param master: Frame or Tab for packing the item inside.
        """
        fig, ax = plt.subplots()

        sns.histplot(self.bmi_range, x='RangeBMI', hue='Outcome',
                     multiple='stack')

        ax.set(ylabel='Frequency')

        plt.title('Outcome for BMI sort by range')
        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas.get_tk_widget().pack(side=ctk.TOP, expand=True, fill='both')
        canvas.draw()

    def load_graph(self, master, name):
        """
        A function that handles plotting histogram graph from attribute data.
        """
        try:
            widget = master.winfo_children()[2]
            widget.destroy()
        except IndexError:
            pass

        graph_frame = ctk.CTkFrame(master)

        fig, ax = plt.subplots()

        sns.histplot(self.df, x=name)

        ax.set(xlabel='', ylabel='Frequency')

        plt.title('Diabetes Outcome for ' + name)
        canvas = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas.get_tk_widget().pack(side=ctk.TOP, fill='both', expand=True)
        canvas.draw()
        graph_frame.pack(side=ctk.TOP, expand=True, fill='both')


if __name__ == '__main__':
    root = ctk.CTk()
    root.title('Graph Demo Loader')
    model = DiabetesModel()

    scrollable = ctk.CTkScrollableFrame(root)
    scrollable.pack(expand=True, fill='both')

    graph_test = False
    if graph_test:
        model.load_storytelling_hist(scrollable)
        model.load_storytelling_stat(scrollable)
        model.load_storytelling_corr(scrollable)
        model.load_pie_chart(scrollable)

    root.mainloop()
