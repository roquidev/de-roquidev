from getdata.getdata import KaggleConnection
from utils.utils import download_data
from constants import Constants
import logging

# Configurar el nivel de log global
logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":
    constants = Constants()

    # Crear una instancia de la clase
    kaggle_con = KaggleConnection()

    logging.info(":::::: Setting Kagle API connection...")
    setted = kaggle_con.set_kaggle_json(constants.KAGGLE_PROJECT_CONFIG_PATH, constants.KAGGLE_USER_ROOT_PATH)  # noqa: E501

    # Download the data
    logging.info(":::::: Downloading data...")
    api_command = input("::::::::: Enter the Kaggle Api Command: ")
    download_data(api_command, constants.ZIP_FILE_PATHS, constants.ROW_DATA_PATH)  # noqa: E501
