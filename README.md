# Diabetes-Checker

A visualization program designed to help users check their risk levels for
diabetes. This tool can provide valuable insights into potential health risks
and assist users in making informed decisions about their well-being.

## Resource

This project uses dataset
from [kaggle.com](https://www.kaggle.com/datasets/akshaydattatraykhare/diabetes-dataset/data)

Information table image sources
[BMI](https://www.kreedon.com/what-is-bmi-body-mass-index-calculate-bmi/),
[Blood pressure](https://www.heart.org/en/health-topics/high-blood-pressure/understanding-blood-pressure-readings),
[Age](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.researchgate.net%2Ffigure%2FAge-intervals-and-age-groups_tbl1_228404297&psig=AOvVaw3OkQXMJjInrDlRpMVaMnzg&ust=1715171432250000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCOirrNHF-4UDFQAAAAAdAAAAABAx),
and
[Glucose](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.breathewellbeing.in%2Fblog%2Fchart-of-normal-blood-sugar-levels-for-adults-with-diabetes%2F&psig=AOvVaw1KA7FeBxHNuOHrIE0pD0hM&ust=1715172721579000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCJiUmrvK-4UDFQAAAAAdAAAAABBi)

## Files

| file              | Description                                                                        |
|-------------------|------------------------------------------------------------------------------------|
| application.py    | The class for controlling both UI and Model.                                       |
| diabetes_model.py | The model class that load and compute data.                                        |
| diabetes_view.py  | The GUI class for user interface.                                                  |
| main.py           | Main script to run the program.                                                    |
| data              | Folder that contain both pictures and data for model to compute and UI to display. |

## Example UI

Windows and macOS have only slightly different when it comes to menubar.

| Tab(Windows)  | Example                                     |
|---------------|---------------------------------------------|
| Home(Windows) | ![Windows home](/snapshots/window_home.png) |

| Tab(macOS)                  | Example                                                                                  |
|-----------------------------|------------------------------------------------------------------------------------------|
| Storytelling(Home)          | ![macOS home](/snapshots/storytelling.png)                                               |
| Histogram and statistic tab | ![histogram](/snapshots/important_hist.png) ![statistic](/snapshots/important_stat.png)  |
| Freestyle tab               | ![histogram](/snapshots/freestyle_hist.png) ![scatter](/snapshots/freestyle_scatter.png) |

## Diagrams

### UML Class Diagram

![UML Class Diagram](/data/uml_diagram/diabetes_class_diagram.png)

### UML Sequence Diagram

#### Storytelling tab after clicks a correlation button and closes both windows

![UML Sequence Diagram](/data/uml_diagram/diabetes_sequence_diagram.png)

## Installation and How to run

### Installation

1. Open Terminal (macOS/Linux) or Powershell/Command Prompt (Windows).

2. Clone files from GitHub repository.

```commandline
git clone https://github.com/PeanutPK/Diabetes-Analysis.git
```

3. After cloning changes your directory to the existing folder.

```commandline
cd Diabetes-Analysis
```

4. Install all requirements in requirements.txt.

```commandline
pip install -r requirements.txt
```

5. Run main.py file

```commandline
python main.py
```

### Creating Virtual Environment

1. Open Terminal (macOS/Linux) or Powershell/Command Prompt (Windows).
2. Change directory to the project

```
cd Diabetes-Analysis
```

3. Create a Virtual Environment.

- for macOS/Linux

```
python -m venv env
```

- or for Windows

```
python3 -m venv env
```

### Activate Virtual Environment

1. Open Terminal (macOS/Linux) or Powershell/Command Prompt (Windows).
2. Change directory to the project

```
cd Diabetes-Analysis
```

3. Activating venv

- for macOS/Linux

```
source env/bin/activate
```

- or for Windows

```
env\Scripts\activate
```

Deactivating venv

```
deactivate
```