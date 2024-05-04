from diabetes_view import DiabetesUI
from diabetes_model import DiabetesModel


class Controller:
    """Controller for applying a design pattern in the future"""
    def __init__(self):
        self.view = DiabetesUI()
        self.model = DiabetesModel()

    def start(self):
        self.view.run()
