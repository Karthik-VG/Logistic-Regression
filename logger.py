import logging

class logger:
    def __init__(self,appl):
        self.appl=appl

    def getLog(self,file):
        self.file=file
        logger=logging.getLogger(self.appl)
        f=open("properties.txt","r")
        if f.mode == "r":
            loglevel=f.read()
        if loglevel == "ERROR":
            logger.setLevel(logging.ERROR)
        elif loglevel == "DEBUG":
            logger.setLevel(logging.DEBUG)

        formatter=logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler=logging.FileHandler(self.file+".log")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger
