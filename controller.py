from diabetes_view import DiabetesUI
from diabetes_model import DiabetesModel


class Controller:
    def __init__(self, view: DiabetesUI, model: DiabetesModel):
        self.view = view
        self.model = model
        self.init_component()

    def init_component(self):
        self.view.run()
