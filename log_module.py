import logging;

logger = logging.getLogger(__name__);

logger.setLevel('DEBUG');

logger.propagate = False
logger.handlers.clear() 

formatter = logging.Formatter(
    "{asctime} - {levelname} - {message}",
     style="{",
     datefmt="%Y-%m-%d %H:%M",)


#logs to consol 
console_handler = logging.StreamHandler();
console_handler.setLevel('DEBUG');#optional
console_handler.setFormatter(formatter);
logger.addHandler(console_handler);

#logs to file
file_handler = logging.FileHandler(filename = 'logfile.log',
                                   mode = 'a',
                                   encoding="utf-8");
file_handler.setLevel('DEBUG');#optional
file_handler.setFormatter(formatter)
logger.addHandler(file_handler); 