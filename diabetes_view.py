from PIL import Image
import customtkinter as ctk
from diabetes_model import DiabetesModel


class DiabetesUI(ctk.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("Diabetes analysis")
        self.tabs = ctk.CTkTabview(self)
        self.current = ctk.StringVar()
        self.init_choice_component()

    def init_choice_component(self):
        self.tabs = ctk.CTkTabview(self)
        self.choices_tab()
        self.graph_tab()
        self.tabs.pack(pady=10)

    def choices_tab(self):
        tab1 = self.tabs.add('Information')
        for i in ['BMI', 'Blood Pressure', 'Age']:
            btn = ctk.CTkButton(tab1, text=i)
            if i == 'BMI':
                btn.configure(command=self.show_bmi)
            btn.pack(side=ctk.LEFT)

    def graph_tab(self):
        tab2 = self.tabs.add('Graphs')
        combo = ctk.CTkComboBox(tab2, values=['Histogram', 'Statistic'],
                                state='readonly')
        combo.pack(side=ctk.TOP)

        def bind_buttons(event=None):
            print('Binding ' + combo.get())
            for widget in tab2.winfo_children():
                if isinstance(widget, ctk.CTkButton):
                    if combo.get() == 'Histogram':
                        widget.configure(command=
                                         lambda name=widget.cget('text'): (
                                             DiabetesModel.load_graph(name))
                                         )
                    elif combo.get() == 'Statistic':
                        widget.configure(command=
                                         lambda name=widget.cget('text'): (
                                             DiabetesModel.describe(tab2,
                                                                    name)))

        combo.configure(command=bind_buttons)
        for txt in ['BMI', 'BloodPressure', 'Age']:
            btn = ctk.CTkButton(tab2, text=txt)
            btn.pack(side=ctk.LEFT)
            bind_buttons()

    def show_bmi(self):
        for i in self.winfo_children():
            i.destroy()
        self.back_button(self)
        BMI_image = Image.open('data/information_photos/bmi_info.png')
        my_BMI_image = ctk.CTkImage(light_image=BMI_image,
                                    dark_image=BMI_image,
                                    size=(600, 315))

        BMI_label = ctk.CTkLabel(self, image=my_BMI_image, text='',
                                 bg_color='transparent')
        BMI_label.bind('<Button-1>', command=lambda x: print("clicked"))
        BMI_label.pack(fill='both', expand=True)

    @staticmethod
    def back_button(master):
        button = ctk.CTkButton(master, text='go back',
                               command=master.goback)
        button.pack(side=ctk.TOP)

    def goback(self):
        for i in self.winfo_children():
            i.destroy()
        self.init_choice_component()

    def run(self):
        self.mainloop()


if __name__ == '__main__':
    test_run = DiabetesUI()
    test_run.run()
