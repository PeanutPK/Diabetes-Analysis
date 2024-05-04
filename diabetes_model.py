import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class DiabetesModel:
    @staticmethod
    def load_graph(master: ctk.CTk, name: str):
        for widget in master.winfo_children():
            if not isinstance(widget, (ctk.CTkTabview, ctk.CTkFrame)):
                widget.destroy()
        file_csv = pd.read_csv('data/diabetes.csv')

        replace = {1: 'Diabetic', 0: 'Not Diabetic'}
        file_csv['Outcome'] = file_csv['Outcome'].replace(replace)

        fig, ax = plt.subplots()

        sns.histplot(file_csv, x=name, hue='Outcome', multiple='stack')

        ax.set(xlabel='', ylabel='Frequency')

        plt.title('Diabetes Outcome for ' + name)
        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas.get_tk_widget().pack(side=ctk.LEFT)
        canvas.draw()

    @staticmethod
    def describe(master, name: str):
        for child in master.winfo_children():
            if not isinstance(child, ctk.CTkTabview):
                child.destroy()
        file_csv = pd.read_csv('data/diabetes.csv')

        label = ctk.CTkLabel(master, text=file_csv[name].describe())
        label.pack(side=ctk.LEFT)

    @staticmethod
    def load_storytelling_hist(master: ctk.CTkScrollableFrame):
        """Load all histograms only for storytelling page"""
        NAMES = ['BMI', 'BloodPressure', 'Age', 'Glucose']

        file_csv = pd.read_csv('data/diabetes.csv')

        replace = {1: 'Diabetic', 0: 'Not Diabetic'}
        file_csv['Outcome'] = file_csv['Outcome'].replace(replace)

        for name in NAMES:
            fig, ax = plt.subplots()

            sns.histplot(file_csv, x=name, hue='Outcome', multiple='stack')

            ax.set(xlabel='', ylabel='Frequency')

            plt.title('Outcome for ' + name)
            canvas = FigureCanvasTkAgg(fig, master=master)
            canvas.get_tk_widget().pack(side=ctk.TOP, expand=True, fill='both')
            canvas.draw()


if __name__ == '__main__':
    root = ctk.CTk()
    root.title('Graph Demo Loader')
    root.geometry('288x288')
    scrollable = ctk.CTkScrollableFrame(root)
    scrollable.pack(expand=True, fill='both')

    # DiabetesModel.load_graph(root, 'BMI')
    DiabetesModel.load_storytelling_hist(scrollable)

    root.mainloop()
