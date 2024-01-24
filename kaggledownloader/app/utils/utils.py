import subprocess
import zipfile
import logging

# Configurar el nivel de log global
logging.basicConfig(level=logging.INFO)


def download_data(api_command, zip_storage_path, row_data_path, zip_password=None):  # noqa: E501
    api_command = api_command + " --force"
    api_command_listed = api_command.split(" ")

    subprocess.run(api_command_listed)

    logging.info(":::::: Copying downloaded zip files to row data directory...")  # noqa: E501
    subprocess.run(["mv", f"{api_command_listed[4].split('/')[1]}.zip", "../data/raw"])  # noqa: E501

    # Abrimos el archivo ZIP
    for path in list(zip_storage_path):
        # :extractall: Extraer los archivos
        # :pwd: contraseña requerida
        logging.info(":::::: Unzipping the files...")
        with zipfile.ZipFile(path, "r") as zip_object:
            zip_object.extractall(path=row_data_path, pwd=zip_password)
        # Eliminar archivos .zip
        path.unlink()

    pass
