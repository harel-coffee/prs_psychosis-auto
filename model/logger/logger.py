import logging
import logging.config
from pathlib import Path
from utils import read_json


def setup_logging(save_dir,
                  name_file,
                  log_config='./logger/logger_config.json',
                  default_level=logging.INFO):
    """
    Setup logging configuration
    """
    log_config = Path(log_config)
    if log_config.is_file():
        config = read_json(log_config)
        config["handlers"]["info_file_handler"]["filename"] = f"{save_dir}/{name_file}"

        logging.config.dictConfig(config)
    else:
        print("Warning: logging configuration file is not found in {}.".format(log_config))
        logging.basicConfig(level=default_level)
