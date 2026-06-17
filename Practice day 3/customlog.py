import logging
 
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
#we can also create custom loggers using using logger variable
logger = logging.getLogger(__name__)
logger.debug("detailed debug info")
logger.info("normal event")
logger.warning("something looks off")
logger.error("something failed")
logger.critical("serious failure")
#here the logger.debug() did not get print bacause :
#in the logging.basicConfig() we have set the level to start from logging.INFO 
#so it ignores all the logs that have less severity than INFO i.e. logger.debug()
#which is why it did not get logged to the console 