from application import DiabetesController
from diabetes_view import DiabetesUI
from diabetes_model import DiabetesModel

if __name__ == '__main__':
    model = DiabetesModel()
    view = DiabetesUI()
    app = DiabetesController(model, view)
    app.run()
