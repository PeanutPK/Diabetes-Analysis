from diabetes_view import DiabetesUI
from diabetes_model import DiabetesModel


class Controller:
    def __init__(self):
        self.view = DiabetesUI()
        self.model = DiabetesModel()

    def start(self):
        self.view.run()
