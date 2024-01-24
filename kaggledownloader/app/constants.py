from pathlib import Path
from pyprojroot import here


class Constants:
    # Project root path
    PROJECT_ROOT_PATH = here()
    # Ruta de almacenamiento row de la data
    ROW_DATA_PATH = PROJECT_ROOT_PATH.joinpath("data", "raw")
    # Ruta de almacenamiento master de la data
    MASTER_DATA_PATH = PROJECT_ROOT_PATH.joinpath("data", "master")
    # Ruta de archivos .zip comprimidos descargados en ROW
    ZIP_FILE_PATHS = ROW_DATA_PATH.glob("*.zip")
    # Crear el archivo JSON en la raíz del Usuario
    KAGGLE_USER_ROOT_PATH = Path().home().joinpath(".kaggle")
    # Archivo kaggle.json en Proyecto
    KAGGLE_PROJECT_CONFIG_PATH = PROJECT_ROOT_PATH.joinpath("kaggle.json")
