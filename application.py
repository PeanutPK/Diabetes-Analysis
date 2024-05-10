from diabetes_view import DiabetesUI
from diabetes_model import DiabetesModel


class DiabetesController:
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
