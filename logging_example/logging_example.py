import logging
import sys
from test import test1


if __name__=='__main__':
    logger= logging.getLogger() # root
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    
    stream_handler= logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    
    logger.addHandler(stream_handler)
    logger.setLevel(logging.DEBUG)
    
    test_logger = logging.getLogger('test')
    test_logger.addHandler(logging.NullHandler())
    test_logger.setLevel(logging.DEBUG)
    
    
    
    logger.debug("disable propagate")
    test_logger.propagate=False
    test1.test_log()
    
    logger.debug("enable propagate")
    test_logger.propagate=True
    test1.test_log()
    
    logger.debug("disable propagate not add stream handler")
    test_logger.propagate=False
    test1.test_log()
    
    logger.debug("disable propagate add stream handler")
    test_logger.propagate=False
    test_logger.addHandler(stream_handler)
    test1.test_log()
    
    logger.debug("disable propagate remove stream handler")
    test_logger.propagate=False
    test_logger.removeHandler(stream_handler)
    test1.test_log()