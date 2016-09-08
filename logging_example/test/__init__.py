import logging

try:
    from logging import NullHandler
except:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass
        
logging.getLogger(__name__).addHandler(NullHandler())