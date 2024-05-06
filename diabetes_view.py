import customtkinter as ctk
from tkinter import Menu
from PIL import Image
from diabetes_model import DiabetesModel

INTRO_TEXT = ("Introduction\n\n"
              "Diabetes Analysis is a program that help the user "
              "analyze their health risks depends on the data provided "
              "by National Institute of Diabetes and Digestive and "
              "Kidney Diseases.\n\n")

OPTIONS = {'expand': 'True', 'pady': 5, 'padx': 5}
BUTTONS_NAMES = ['BMI', 'BloodPressure', 'Age', 'Glucose']


class DiabetesUI(ctk.CTk):

    def __init__(self, **kwargs):
        """
        Initialize tab and set the default size for a window as 600x315
        """
        super().__init__(**kwargs)
        ctk.set_default_color_theme('green')
        self.title("Diabetes analysis")

        self.model = DiabetesModel()
        self.toplevel = None

        self.current_image = None  # current image in the information tab
        self.current_combo = None  # current selected combobox

        self.tabs = ctk.CTkTabview(self)
        self.btn_frame = None  # Frame for buttons in graph tab and info tab
        self.home_tab = None  # Home tab / storytelling
        self.info_tab = None  # Information showing tab
        self.graph_tab = None  # Graph showing tab depends on user selection
        self.init_component()

    def setup_menubar(self):
        """
        set up menubar with exit function
        """
        # create menu object
        menubar = Menu(self)

        # setup exit menu command
        exit_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Exit menu", menu=exit_menu)
        exit_menu.add_command(label='Exit', command=self.destroy)

        self.config(menu=menubar)

    def init_component(self):
        """
        Setup all tabs and menubar function
        """
        self.tabs = ctk.CTkTabview(self)
        self.storytelling_tab()
        self.information_tab()
        self.graphs_plotting_tab()
        self.tabs.configure(command=self.tab_changes_handler)
        self.tabs.pack(pady=10, expand=True, fill='both', side=ctk.TOP)

    def tab_changes_handler(self):
        """For clearing others widget, that is not TabView widget."""
        for widget in self.winfo_children():
            if not isinstance(widget, ctk.CTkTabview):
                widget.destroy()

    def create_buttons(self, master):
        """
        Initialize buttons for tabs.
        :param master: Root window for buttons.
        """
        self.btn_frame = ctk.CTkFrame(master)
        for name in BUTTONS_NAMES:
            btn = ctk.CTkButton(self.btn_frame, text=name)
            btn.pack(side=ctk.LEFT, fill='x', **OPTIONS)
        self.btn_frame.pack(side=ctk.TOP, fill='x', **OPTIONS, anchor='n')

    def storytelling_tab(self):
        """
        This tab describes the storytelling part.
        """
        self.home_tab = self.tabs.add('Home')
        wrap_length = self.winfo_width()

        scroll_frame = ctk.CTkScrollableFrame(self.home_tab)
        scroll_frame.pack(fill='both', **OPTIONS)

        textbox = self.create_text_label(scroll_frame, wrap_length,
                                         INTRO_TEXT)
        textbox.pack(side=ctk.TOP, fill='both', **OPTIONS)

        pie_btn = ctk.CTkButton(scroll_frame, text='Show Ratio Pie Chart')
        pie_btn.bind('<Button-1>', command=self.pie_btn_handler)
        pie_btn.pack(side=ctk.TOP, fill='both', **OPTIONS)

        # Create button for the statistic descriptions popup window
        desc_stat_btn = ctk.CTkButton(scroll_frame,
                                      text='Descriptive Statistic')
        desc_stat_btn.bind('<Button-1>', command=self.desc_stat_btn_handler)
        desc_stat_btn.pack(side=ctk.TOP, fill='both', **OPTIONS)

        # Create button for the histograms popup window
        hist_btn = ctk.CTkButton(scroll_frame, text='Histogram')
        hist_btn.bind('<Button-1>', command=self.hist_btn_handler)
        hist_btn.pack(side=ctk.TOP, fill='both', **OPTIONS)

        # Create button for scatter plots with a correlations popup window
        hist_btn = ctk.CTkButton(scroll_frame, text='Correlation')
        hist_btn.bind('<Button-1>', command=self.corr_btn_handler)
        hist_btn.pack(side=ctk.TOP, fill='both', **OPTIONS)

    def pie_btn_handler(self, event=None):
        """
        Handler for histogram button to show histograms.
        :param event: Widget event handler that usually set as none.
        """
        if self.toplevel is None or not self.toplevel.winfo_exists():
            storytelling = ctk.CTkToplevel()
            storytelling.title('Ratio of diabetic vs non-diabetic data')
            storytelling.attributes('-topmost', True)

            scrollable = ctk.CTkScrollableFrame(storytelling)
            scrollable.pack(fill='both', **OPTIONS)
            self.model.load_pie_chart(scrollable)
            self.toplevel = storytelling
        else:
            self.toplevel.focus()

    def desc_stat_btn_handler(self, event=None):
        """
        Handler for statistic button to show descriptive statistics.
        :param event: Widget event handler that usually set as none.
        """
        if self.toplevel is None or not self.toplevel.winfo_exists():
            storytelling = ctk.CTkToplevel()
            storytelling.title('Descriptive Statistic')
            storytelling.attributes('-topmost', True)

            scrollable = ctk.CTkScrollableFrame(storytelling)
            scrollable.pack(fill='both', **OPTIONS)
            self.model.load_storytelling_stat(scrollable)
            self.toplevel = storytelling
        else:
            self.toplevel.focus()

    def hist_btn_handler(self, event=None):
        """
        Handler for histogram button to show histograms.
        :param event: Widget event handler that usually set as none.
        """
        if self.toplevel is None or not self.toplevel.winfo_exists():
            storytelling = ctk.CTkToplevel()
            storytelling.title('Histograms')
            storytelling.attributes('-topmost', True)

            scrollable = ctk.CTkScrollableFrame(storytelling)
            scrollable.pack(fill='both', **OPTIONS)
            self.model.load_storytelling_hist(scrollable)
            self.toplevel = storytelling
        else:
            self.toplevel.focus()

    def corr_btn_handler(self, event=None):
        """
        Handler for histogram button to show histograms.
        :param event: Widget event handler that usually set as none.
        """
        if self.toplevel is None or not self.toplevel.winfo_exists():
            storytelling = ctk.CTkToplevel()
            storytelling.title('Correlations')
            storytelling.attributes('-topmost', True)

            scrollable = ctk.CTkScrollableFrame(storytelling)
            scrollable.pack(fill='both', **OPTIONS)
            self.model.load_storytelling_corr(scrollable)
            self.toplevel = storytelling
        else:
            self.toplevel.focus()

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

    def information_buttons_binding(self):
        """
        Bind buttons for information tab.
        """
        for widget in self.btn_frame.winfo_children():
            if widget.cget('text') == 'BMI':
                widget.configure(command=self.create_image)
            else:
                widget.configure(command=self.unfinished_information_tab)

    def unfinished_information_tab(self):
        """
        Display an unfinished message for user to wait for further development.
        """
        sorry_message = ('Sorry for your inconvenience.\n'
                         'This page is under construction '
                         'please wait until the next update.')
        my_font = ctk.CTkFont(family='<Calibri>', size=25, weight='bold')
        for i in self.info_tab.winfo_children():
            if not isinstance(i, ctk.CTkFrame):
                i.destroy()
        BMI_label = ctk.CTkLabel(self.info_tab, text=sorry_message,
                                 bg_color='transparent', font=my_font)
        BMI_label.pack(fill='both', **OPTIONS)

    def create_image(self):
        """
        Load and show the image of BMI standard value information photo.
        """
        for widget in self.info_tab.winfo_children():
            if widget != self.btn_frame:
                print(widget)
                widget.destroy()

        image_frame = ctk.CTkFrame(self.info_tab)
        image_frame.pack(side=ctk.TOP, fill='both', **OPTIONS)
        image = Image.open('data/information_photos/bmi_info.png')
        image_width, image_height = image.size

        def resize(event=None):
            new_width = image_frame.winfo_width()
            new_height = (image_height / image_width) * new_width
            self.current_image.configure(size=(new_width, new_height))

        self.current_image = ctk.CTkImage(light_image=image, dark_image=image,
                                          size=image.size)
        label = ctk.CTkLabel(image_frame, image=self.current_image, text='',
                             bg_color='transparent')
        label.pack(side=ctk.TOP)

        self.info_tab.bind('<Configure>', resize)

    def graphs_plotting_tab(self):
        """
        This tab let the user pick a graph from the provided button choosing
        between statistical data or histogram graph.
        In the future, there will be more types of graphs.
        """
        self.graph_tab = self.tabs.add('Graphs')
        combo = ctk.CTkComboBox(self.graph_tab, state='readonly',
                                values=['Histogram', 'Statistic'])
        combo.set('Histogram')
        self.current_combo = lambda: combo.get()
        combo.pack(side=ctk.TOP)
        self.create_buttons(self.graph_tab)

        def bind_graph_tab_buttons(event=None):
            """Bind buttons when the combo box changes the function."""
            for widget in self.btn_frame.winfo_children():
                if combo.get() == 'Histogram':
                    widget.configure(command=
                                     lambda name=widget.cget('text'): (
                                         self.model.load_graph(self,
                                                               name)))
                elif combo.get() == 'Statistic':
                    widget.configure(command=
                                     lambda name=widget.cget('text'): (
                                         self.model.describe(self,
                                                             self.graph_tab,
                                                             name)))

        combo.configure(command=bind_graph_tab_buttons)
        bind_graph_tab_buttons()

    def run(self):
        """
        Set up the menu bars and loop the main window.
        Set protocol for an exiting window
        as quit to stop any process after mainloop.
        """
        self.protocol("WM_DELETE_WINDOW", self.quit)
        self.setup_menubar()
        self.mainloop()

    def unused(self):

        def back_button(self, master):
            """
            Button that returns to the previous page.
            :param master: Root of the window before going to another page
            :return:
            """
            button = ctk.CTkButton(master, text='go back',
                                   command=lambda: self.goback(master))
            button.pack(side=ctk.TOP)

        def goback(self, master: ctk.CTkFrame):
            """
            A back button handle to return to the master frame.
            :param master: Origin frame.
            """
            for widget in master.winfo_children():
                widget.destroy()
            self.create_buttons(master)
            if master == self.info_tab:
                self.information_buttons_binding()


if __name__ == '__main__':
    test_ui = DiabetesUI()
    test_ui.run()
