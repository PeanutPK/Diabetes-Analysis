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
IMPORTANT_WIDGET = (ctk.CTkTabview, Menu, ctk.CTkButton)


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
        self.image = None

        self.tabs = ctk.CTkTabview(self)
        self.btn_frame = None  # Frame for buttons in graph tab and info tab
        self.home_tab = None  # Home tab / storytelling
        self.info_tab = None  # Information showing tab
        self.stat_graph_tab = None  # Important statistic and graph tab
        self.any_graph_tab = None  # Showing graph depending on user choice
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

        # setup appearance changing menu
        appearance_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Appearance Mode', menu=appearance_menu)
        appearance_menu.add_command(label='System Default',
                                    command=lambda:
                                    ctk.set_appearance_mode("system"))
        appearance_menu.add_command(label='Dark Mode',
                                    command=lambda:
                                    ctk.set_appearance_mode("dark"))
        appearance_menu.add_command(label='Light Mode',
                                    command=lambda:
                                    ctk.set_appearance_mode("light"))

        self.config(menu=menubar)

    def init_component(self):
        """
        Setup all tabs and menubar function
        """
        self.tabs = ctk.CTkTabview(self)
        self.storytelling_tab()
        self.information_tab()
        self.stat_and_graph_tab()
        self.graphs_plotting_tab()
        self.tabs.configure(command=self.tab_changes_handler)
        self.tabs.pack(pady=10, expand=True, fill='both', side=ctk.TOP)

    def tab_changes_handler(self):
        """For clearing others widget, that is not TabView widget."""
        for widget in self.winfo_children():
            if not isinstance(widget, IMPORTANT_WIDGET):
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
        self.btn_frame.pack(side=ctk.TOP, fill='x', **OPTIONS)

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
        corr_btn = ctk.CTkButton(scroll_frame, text='Correlation')
        corr_btn.bind('<Button-1>', command=self.corr_btn_handler)
        corr_btn.pack(side=ctk.TOP, fill='both', **OPTIONS)

        # Create button for the histograms popup window
        bmi_btn = ctk.CTkButton(scroll_frame, text='BMI Range Histogram')
        bmi_btn.bind('<Button-1>', command=self.bmi_range_btn_handler)
        bmi_btn.pack(side=ctk.TOP, fill='both', **OPTIONS)

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

    def bmi_range_btn_handler(self, event=None):
        """
        Handler for histogram button to show histograms.
        :param event: Widget event handler that usually set as none.
        """
        if self.toplevel is None or not self.toplevel.winfo_exists():
            storytelling = ctk.CTkToplevel()
            storytelling.title('BMI Standard Range')
            storytelling.attributes('-topmost', True)

            frame = ctk.CTkFrame(storytelling)
            frame.pack(fill='both', **OPTIONS)
            self.model.load_bar_graph_bmi(frame)
            self.toplevel = storytelling
        else:
            self.toplevel.focus()

    @staticmethod
    def create_text_label(master, length, text):
        """Text label for """
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
            widget.configure(command=lambda name=widget.cget('text'):
            self.create_image(name))

    def create_image(self, name: str):
        """
        Create an image frame for showing selected button information.
        """
        try:  # Handle existed image frame to clear the previous image.
            image_frame = self.info_tab.winfo_children()[1]
            for image in image_frame.winfo_children():
                image.destroy()
        except IndexError:
            image_frame = ctk.CTkFrame(self.info_tab)
            image_frame.pack(side=ctk.TOP, fill='both', **OPTIONS)

        try:  # Handle missing information
            image = Image.open(f'data/information_photos/{name}_info.png')
        except FileNotFoundError:
            image = Image.open('data/information_photos/image-not-found.png')
        image_width, image_height = image.size

        def resize(event=None):
            new_width = image_frame.winfo_width()
            new_height = (image_height / image_width) * new_width
            self.current_image.configure(size=(new_width, new_height))

        self.current_image = ctk.CTkImage(light_image=image,
                                          dark_image=image,
                                          size=image.size)
        label = ctk.CTkLabel(image_frame, image=self.current_image, text='',
                             bg_color='transparent')
        label.pack(side=ctk.TOP)

        self.info_tab.bind('<Configure>', resize)

    def stat_and_graph_tab(self):
        """
        This tab let the user pick a graph from the provided button choosing
        between statistical data or histogram graph.
        In the future, there will be more types of graphs.
        """
        self.stat_graph_tab = self.tabs.add('Graphs')
        combo = ctk.CTkComboBox(self.stat_graph_tab, state='readonly',
                                values=['Histogram', 'Statistic'])
        combo.set('Histogram')
        combo.pack(side=ctk.TOP)
        self.create_buttons(self.stat_graph_tab)

        def bind_graph_tab_buttons(event=None):
            """Bind buttons when the combo box changes the function."""
            for widget in self.btn_frame.winfo_children():
                if combo.get() == 'Histogram':
                    widget.configure(command=
                                     lambda name=widget.cget('text'): (
                                         self.model.load_hist_outcome(
                                             self.stat_graph_tab, name)))
                elif combo.get() == 'Statistic':
                    widget.configure(command=
                                     lambda name=widget.cget('text'): (
                                         self.model.describe(
                                             self.stat_graph_tab, name)))

        combo.configure(command=bind_graph_tab_buttons)
        bind_graph_tab_buttons()

    def graphs_plotting_tab(self):
        """
        This tab let user freely choose any attribute inside a csv file to plot
        scatter or histogram.
        """
        self.any_graph_tab = self.tabs.add('Free Style')
        attributes = self.model.get_column()
        attributes.insert(0, "None")

        graph_choice = ctk.CTkComboBox(self.any_graph_tab, state='readonly',
                                       values=['Histogram', 'Scatterplot'])
        graph_choice.set('Histogram')
        graph_choice.pack(side=ctk.TOP)

        # Variables for combobox
        first_attr = ctk.StringVar()
        second_attr = ctk.StringVar()
        hue_attr = ctk.StringVar()

        # Frame for packing labels and combobox
        combo_frame = ctk.CTkFrame(self.any_graph_tab)
        combo_frame.pack(side=ctk.TOP, **OPTIONS, fill='both')

        # Create X label and combobox for getting the first attribute.
        x_label = ctk.CTkLabel(combo_frame, text='X-axis')
        x_combobox = ctk.CTkComboBox(combo_frame, state='readonly',
                                     variable=first_attr,
                                     values=attributes)

        # Create Y label and combobox for getting the first attribute.
        y_label = ctk.CTkLabel(combo_frame, text='Y-axis')
        y_combobox = ctk.CTkComboBox(combo_frame, state='disabled',
                                     variable=second_attr,
                                     values=attributes)

        # Create HUE label and combobox for getting the attribute for HUE.
        hue_label = ctk.CTkLabel(combo_frame, text='HUE')
        hue_combobox = ctk.CTkComboBox(combo_frame, state='readonly',
                                       variable=hue_attr,
                                       values=attributes)

        # Button for plotting
        plot_button = ctk.CTkButton(master=combo_frame, text='plot',
                                    command=lambda:
                                    self.model.load_hist(self.any_graph_tab,
                                                         first_attr.get()))

        x_label.grid(row=0, column=0, sticky=ctk.NW)
        y_label.grid(row=0, column=2, sticky=ctk.NE)
        hue_label.grid(row=0, column=1, sticky=ctk.NE)

        x_combobox.grid(row=1, column=0, sticky=ctk.NW)
        y_combobox.grid(row=1, column=2, sticky=ctk.NE)
        hue_combobox.grid(row=1, column=1, sticky=ctk.NE)

        plot_button.grid(row=2, column=0, sticky=ctk.EW, columnspan=3)

        for i in range(3):
            combo_frame.columnconfigure(i, weight=1)

        # TODO make this tab handle both histogram and scatterplot
        def set_type(event=None):
            if graph_choice.get() == 'Scatterplot':
                y_combobox.configure(state='readonly')
                plot_button.configure(command=lambda:
                                      self.model.load_correlations_scatter(
                                          self.any_graph_tab, first_attr.get(),
                                          second_attr.get(), hue_attr.get()))
            elif graph_choice.get() == 'Histogram':
                y_combobox.configure(state='disabled')
                plot_button.configure(command=lambda:
                                      self.model.load_hist(
                                          self.any_graph_tab,
                                          first_attr.get()))

        graph_choice.configure(command=set_type)

    def run(self):
        """
        Set up the menu bars and loop the main window.
        Set protocol for an exiting window
        as quit to stop any process after mainloop.
        """
        self.protocol("WM_DELETE_WINDOW", self.quit)
        self.setup_menubar()
        self.mainloop()
