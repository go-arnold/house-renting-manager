import logging

logging.basicConfig(
    filename="house_manager.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def log_action(action):
    logging.info(action)
