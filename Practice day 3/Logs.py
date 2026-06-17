import logging
# By default, the logging module logs messages with a severity level of WARNING or above.
# so the warning, error, and debug messages will be logged, but the info and debug messages will not be logged.

logging.basicConfig(level=logging.DEBUG, filename="logfile.log", filemode="w"
                    ,format="%(asctime)s - %(levelname)s - %(message)s")
# To log messages with a lower severity level, you can set the logging level to DEBUG or INFO.
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

#logging into a file, you can specify the filename and filemode parameters in the basicConfig function. The filename parameter specifies the name of the log file, and the filemode parameter specifies the mode in which the log file is opened (e.g., "w" for write mode, "a" for append mode).

#we can also specify the format of the log messages using the format parameter in the basicConfig function. The #mat parameter allows you to customize the output of the log messages, including the timestamp, log level, and message content.
#for example , in logfile.log:
# logging.basicConfig(level=logging.DEBUG, filename="logfile.log", filemode="w", format="%(asctime)s - %(levelname)s - %(message)s")
#  the log messages will include the timestamp, log level, and message content in the specified format.