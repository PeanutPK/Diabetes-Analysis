import customtkinter as ctk
from tkinter import Menu
from PIL import Image
from diabetes_model import DiabetesModel
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

INTRO_TEXT = ("Introduction\n\n"
              "Diabetes Analysis is a program that help the user "
              "analyze their health risks depends on the data provided "
              "by National Institute of Diabetes and Digestive and "
              "Kidney Diseases.")


class DiabetesUI(ctk.CTk):
    BUTTONS_NAMES = ['BMI', 'BloodPressure', 'Age', 'Glucose']

    def __init__(self, **kwargs):
        """
        Initialize tab and set the default size for a window as 600x315
        """
        super().__init__(**kwargs)
        ctk.set_default_color_theme('green')
        self.title("Diabetes analysis")
        self.geometry('600x315')
        self.tabs = ctk.CTkTabview(self)
        self.current_combo = None

        self.home_tab = None
        self.info_tab = None
        self.graph_tab = None
        self.init_component()

    def setup_menubar(self):
        """
        set up menubar with exit function
        """
        # create menu object
        menubar = Menu(self)
        self.config(menu=menubar)

        # setup exit menu command
        menu_options = Menu(menubar)
        menu_options.add_command(label='Exit', command=self.destroy)

    def init_component(self):
        """
        Setup all tabs and menubar function
        """
        self.setup_menubar()
        self.tabs = ctk.CTkTabview(self)
        self.storytelling_tab()
        self.information_tab()
        self.graphs_plotting_tab()
        self.tabs.pack(pady=10, expand=True, fill='both', side=ctk.LEFT)

    def create_buttons(self, master):
        """
        Initialize buttons for tabs.
        :param master: Root window for buttons.
        """
        for name in self.BUTTONS_NAMES:
            btn = ctk.CTkButton(master, text=name)
            btn.pack(side=ctk.TOP, expand=True, fill='y')

    def information_buttons_binding(self):
        """
        Bind buttons for information tab.
        """
        for widget in self.info_tab.winfo_children():
            if isinstance(widget, ctk.CTkButton):
                if widget.cget('text') == 'BMI':
                    widget.configure(command=self.show_bmi)

    def storytelling_tab(self):
        """
        This tab describes the storytelling part.
        """
        self.home_tab = self.tabs.add('Home')
        wrap_length = self.winfo_width()

        scroll_frame = ctk.CTkScrollableFrame(self.home_tab)
        scroll_frame.pack(expand=True, fill='both')

        textbox = self.create_text_label(scroll_frame, wrap_length,
                                         INTRO_TEXT)
        textbox.pack(expand=True, fill='both', side=ctk.TOP)

        desc_stat_btn = ctk.CTkButton(self.home_tab,
                                      text='Descriptive Statistic')
        desc_stat_btn.pack(side=ctk.TOP, expand=True, fill='both')

    def desc_stat_btn_handler(self):
        pass

    @staticmethod
    def create_text_label(master, length, text):
        return ctk.CTkLabel(master, justify='left', wraplength=length,
                            text=text)

    def information_tab(self):
        """
        This tab let user choose the standard value to display in each topic.
        """
        self.info_tab = self.tabs.add('Information')
        self.create_buttons(self.info_tab)
        self.information_buttons_binding()

    def show_bmi(self):
        """
        Load and show the image of BMI photo.
        """
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
        """
        This tab let the user pick a graph from the provided button choosing
        between statistical data or histogram graph.
        In the future, there will be more types of graphs.
        """
        self.graph_tab = self.tabs.add('Graphs')
        combo = ctk.CTkComboBox(self.graph_tab,
                                values=['Histogram', 'Statistic'],
                                state='readonly')
        combo.set('Histogram')
        self.current_combo = lambda: combo.get()
        combo.pack(side=ctk.TOP)
        self.create_buttons(self.graph_tab)

        def bind_buttons(event=None):
            """Bind buttons when the combo box changes the function."""
            for widget in self.graph_tab.winfo_children():
                if isinstance(widget, ctk.CTkButton):
                    if combo.get() == 'Histogram':
                        widget.configure(command=
                                         lambda name=widget.cget('text'): (
                                             DiabetesModel.load_graph(name))
                                         )
                    elif combo.get() == 'Statistic':
                        widget.configure(command=
                                         lambda name=widget.cget('text'): (
                                             DiabetesModel.describe(self,
                                                                    name)))

        combo.configure(command=bind_buttons)
        bind_buttons()

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
