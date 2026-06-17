import logging

logging.basicConfig(level=logging.DEBUG,filename="v_log.log", format="%(asctime)s - %(levelname)s - %(message)s")
x="log files are used to track events occured"
logging.debug(f"x shows:{x}")

