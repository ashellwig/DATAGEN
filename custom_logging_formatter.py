import logging


class Colors:
    grey = "\x1b[0;37m"
    green = "\x1b[1;32m"
    yellow = "\x1b[1;33m"
    red = "\x1b[1;31m"
    purple = "\x1b[1;35m"
    blue = "\x1b[1;34m"
    light_blue = "\x1b[1;36m"
    reset = "\x1b[0m"
    blink_red = "\x1b[5m\x1b[1;31m"


class CustomFormatter(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors"""

    def __init__(self, auto_colorized=True):
        super(CustomFormatter, self).__init__()
        self.auto_colorized = auto_colorized
        self.formats = self.define_format()

    def define_format(self):
        # Levels
        # CRITICAL = 50
        # FATAL = CRITICAL
        # ERROR = 40
        # WARNING = 30
        # WARN = WARNING
        # INFO = 20
        # DEBUG = 10
        # NOTSET = 0


        format_prefix = f"{Colors.purple}%(asctime)s{Colors.reset} " \
                        f"{Colors.blue}%(name)s{Colors.reset} " \
                        f"{Colors.light_blue}(%(filename)s:%(lineno)d)" \
                        f"{Colors.reset} "

        format_suffix = "%(levelname)s - %(message)s"

        return {
            logging.DEBUG:
            format_prefix + Colors.green + format_suffix + Colors.reset,
            logging.INFO:
            format_prefix + Colors.grey + format_suffix + Colors.reset,
            logging.WARNING:
            format_prefix + Colors.yellow + format_suffix + Colors.reset,
            logging.ERROR:
            format_prefix + Colors.red + format_suffix + Colors.reset,
            logging.CRITICAL:
            format_prefix + Colors.blink_red + format_suffix + Colors.reset
        }

    def format(self, record):
        log_fmt = self.formats.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
