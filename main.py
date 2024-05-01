from controller import Controller
from diabetes_view import DiabetesUI
from diabetes_model import DiabetesModel

if __name__ == '__main__':
    view = DiabetesUI()
    model = DiabetesModel()
    app = Controller(view, model)
    app.start()
