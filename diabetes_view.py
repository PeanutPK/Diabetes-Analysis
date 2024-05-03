import customtkinter as ctk
from PIL import Image
from diabetes_model import DiabetesModel
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class DiabetesUI(ctk.CTk):
    BUTTONS_NAMES = ['BMI', 'BloodPressure', 'Age']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("Diabetes analysis")
        self.tabs = ctk.CTkTabview(self)
        self.current_combo = None

        self.home_tab = None
        self.info_tab = None
        self.graph_tab = None
        self.init_choice_component()

    def init_choice_component(self):
        self.tabs = ctk.CTkTabview(self)
        self.storytelling_tab()
        self.information_tab()
        self.graphs_plotting_tab()
        self.tabs.pack(pady=10)

    def create_buttons(self, master):
        for name in self.BUTTONS_NAMES:
            btn = ctk.CTkButton(master, text=name)
            if master == self.info_tab:
                self.information_buttons_binding(name, btn)
            elif master == self.graph_tab:
                self.graphs_buttons_binding(name, btn)
            btn.pack(side=ctk.LEFT)

    def information_buttons_binding(self, name, btn):
        if name == 'BMI':
            btn.configure(command=self.show_bmi)
        btn.pack(side=ctk.LEFT)

    def storytelling_tab(self):
        self.home_tab = self.tabs.add('Home')

    def information_tab(self):
        self.info_tab = self.tabs.add('Information')
        self.create_buttons(self.info_tab)

    def show_bmi(self):
        for i in self.info_tab.winfo_children():
            i.destroy()
        self.back_button(self.info_tab)
        BMI_image = Image.open('data/information_photos/bmi_info.png')
        my_BMI_image = ctk.CTkImage(light_image=BMI_image,
                                    dark_image=BMI_image,
                                    size=(600, 315))

        BMI_label = ctk.CTkLabel(self.info_tab, image=my_BMI_image, text='',
                                 bg_color='transparent')
        BMI_label.bind('<Button-1>', command=lambda x: print("clicked"))
        BMI_label.pack(fill='both', expand=True)

    def graphs_plotting_tab(self):
        self.graph_tab = self.tabs.add('Graphs')
        combo = ctk.CTkComboBox(self.graph_tab,
                                values=['Histogram', 'Statistic'],
                                state='readonly')
        self.current_combo = lambda: combo.get()
        combo.pack(side=ctk.TOP)
        self.create_buttons(self.graph_tab)

        # def bind_buttons(event=None):
        #     # For debug binding command.
        #     # print('Binding ' + combo.get())
        #     for widget in self.graph_tab.winfo_children():
        #         if isinstance(widget, ctk.CTkButton):
        #             if combo.get() == 'Histogram':
        #                 widget.configure(command=
        #                                  lambda name=widget.cget('text'): (
        #                                      DiabetesModel.load_graph(name))
        #                                  )
        #             elif combo.get() == 'Statistic':
        #                 widget.configure(command=
        #                                  lambda name=widget.cget('text'): (
        #                                      DiabetesModel.describe(
        #                                          self.graph_tab,
        #                                          name)))

        # combo.configure(command=bind_buttons)
        # for txt in self.BUTTONS_NAMES:
        #     btn = ctk.CTkButton(self.graph_tab, text=txt)
        #     btn.pack(side=ctk.LEFT)
        #     bind_buttons()

    def graphs_buttons_binding(self, name, btn):
        print('Binding ' + self.current_combo())
        if self.current_combo() == 'Histogram':
            btn.configure(command=
                          lambda btn_name=btn.cget('text'): (
                              DiabetesModel.load_graph(btn_name))
                          )
        elif self.current_combo() == 'Statistic':
            btn.configure(command=
                          lambda: (
                              DiabetesModel.describe(
                                  self.graph_tab, name)))

    def back_button(self, master):
        button = ctk.CTkButton(master, text='go back',
                               command=lambda: self.goback(master))
        button.pack(side=ctk.TOP)

    def goback(self, master: ctk.CTkFrame):
        for widget in master.winfo_children():
            widget.destroy()
        self.create_buttons(master)

    def run(self):
        self.mainloop()


if __name__ == '__main__':
    test_ui = DiabetesUI()
    test_ui.run()
