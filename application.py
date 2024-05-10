"""Module to initialize two of the module and also work as an application."""
from diabetes_view import DiabetesUI
from diabetes_model import DiabetesModel


class DiabetesController:
    """A class that initializes two modules that is used in the program."""
    def __init__(self):
        """
        Initialize a class for this application.
        """
        self.model = DiabetesModel()
        self.view = DiabetesUI()
        self.view.setup_menubar()

    def run(self):
        """
        Run class view mainloop.
        """
        self.view.mainloop()
