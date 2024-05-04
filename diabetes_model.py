import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

sns.set_theme(rc={'figure.figsize': (2, 2)})


class DiabetesModel:
    FILE_CSV = pd.read_csv('data/diabetes.csv')
    REPLACE = {1: 'Diabetic', 0: 'Not Diabetic'}
    FILE_CSV['Outcome'] = FILE_CSV['Outcome'].replace(REPLACE)
    NAMES = ['BMI', 'BloodPressure', 'Age', 'Glucose']

    def load_graph(self, master: ctk.CTk, name: str):
        for widget in master.winfo_children():
            if not isinstance(widget, (ctk.CTkTabview, ctk.CTkFrame)):
                widget.destroy()

        replace = {1: 'Diabetic', 0: 'Not Diabetic'}
        self.FILE_CSV['Outcome'] = self.FILE_CSV['Outcome'].replace(replace)

        fig, ax = plt.subplots()

        sns.histplot(self.FILE_CSV, x=name, hue='Outcome', multiple='stack')

        ax.set(xlabel='', ylabel='Frequency')

        plt.title('Diabetes Outcome for ' + name)
        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas.get_tk_widget().pack(side=ctk.LEFT)
        canvas.draw()

    def describe(self, master, name: str):
        for child in master.winfo_children():
            if not isinstance(child, ctk.CTkTabview):
                child.destroy()

        label = ctk.CTkLabel(master, text=self.FILE_CSV[name].describe())
        label.pack(side=ctk.LEFT)

    def load_storytelling_hist(self, master: ctk.CTkScrollableFrame):
        """Load all histograms only for storytelling page"""

        for name in self.NAMES:
            fig, ax = plt.subplots()

            sns.histplot(self.FILE_CSV, x=name, hue='Outcome',
                         multiple='stack')

            ax.set(ylabel='Frequency')

            plt.title('Outcome for ' + name)
            canvas = FigureCanvasTkAgg(fig, master=master)
            canvas.get_tk_widget().pack(side=ctk.TOP)
            canvas.draw()

    def load_storytelling_stat(self, master):
        for name in self.NAMES:
            label = ctk.CTkLabel(master,
                                 text=f"{self.FILE_CSV[name].describe()}\n")
            label.pack(side=ctk.TOP)

    def load_correlations_scatter(self, master, x, y):
        fig, ax = plt.subplots()

        coefficient = np.corrcoef(self.FILE_CSV[x], self.FILE_CSV[y])[0, 1]

        sns.scatterplot(self.FILE_CSV, x=x, y=y, hue='Outcome')

        ax.set(xlabel=x, ylabel=y)

        plt.title(f"{x} vs {y} & corr coeff: {coefficient:.2f}")

        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas.get_tk_widget().pack(side=ctk.TOP, fill='both')

        canvas.draw()

    def load_storytelling_corr(self, master):
        self.load_correlations_scatter(master, 'BMI', 'BloodPressure')
        self.load_correlations_scatter(master, 'Glucose', 'Insulin')
        self.load_correlations_scatter(master, 'Glucose', 'BMI')


if __name__ == '__main__':
    root = ctk.CTk()
    root.title('Graph Demo Loader')

    scrollable = ctk.CTkScrollableFrame(root)
    scrollable.pack(expand=True, fill='both')

    # DiabetesModel.load_graph(root, 'BMI')

    # DiabetesModel().load_storytelling_hist(scrollable)
    # DiabetesModel().load_storytelling_stat(scrollable)
    DiabetesModel().load_storytelling_corr(scrollable)

    root.mainloop()
