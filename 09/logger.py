import logging


class NoCacheFilter(logging.Filter):
    def filter(self, record):
        return "cache" not in record.msg


def add_stream_handler(logger):
    format_stdout = logging.Formatter("%(asctime)s\t%(levelname)s\t[stdout]\t%(message)s")

    stdout_handler = logging.StreamHandler()
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(format_stdout)

    logger.addHandler(stdout_handler)
    return logger


def add_filter(logger):
    for handler in logger.handlers:
        handler.addFilter(NoCacheFilter())

    return logger


def get_logger():
    format_file = logging.Formatter("%(asctime)s\t%(levelname)s\t[file]\t%(message)s")

    file_handler = logging.FileHandler("cache.log")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(format_file)

    logger = logging.getLogger("logger")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)

    return logger
