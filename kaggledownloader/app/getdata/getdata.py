import json


class KaggleConnection:
    # :return: Dictionary with kaggle credentials (username & api key)
    def set_kaggle_json(self, source_path, target_path):
        # Read kaggle.json from project path (KAGGLE_PROJECT_CONFIG_PATH)
        with open(source_path, 'r', encoding='utf-8') as data:
            credentials = json.load(data)
        # Write kaggle.json on user root path (KAGGLE_USER_ROOT_PATH)
        with open(target_path.joinpath("kaggle.json"), "w", encoding='utf-8') as file:  # noqa: E501
            json.dump(credentials, file)

        pass
