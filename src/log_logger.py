
'''
Created on 2025-01-14 17:17:36

@author: MilkTea_shih

setup the logger for logging
'''

#%%    Packages
import inspect
import logging
import sys

from types import FrameType
from typing import cast
from typing import Optional, Self, TextIO

#%%    Variable
_LOG_MODE: str = "normal"

_LOG_STATUS: str = {
    "DEBUG": "logs/log.txt",
    "normal": "logs/main.log"
}[_LOG_MODE]

_LOG_LEVEL: int = {
    "DEBUG": logging.DEBUG,
    "normal": logging.INFO
}[_LOG_MODE]


#%%    Functions
class Logger(logging.Logger):
    #is_singleton: bool = True

    _handler_table: dict[tuple[str, TextIO] | tuple[str], int] = {
        #stream: (log_file, stream): index in self.logger.handlers
        #file:   (log_file,)       : index in self.logger.handlers
    }

    def __new__(cls, *args, **kwargs) -> Self:
        # `caller`: get the name of caller
        cls.caller: str = cast(
            FrameType, cast(FrameType, inspect.currentframe()).f_back
        ).f_code.co_name
        return super().__new__(cls)

    def __init__(self, file: str = _LOG_STATUS,
                 /,
                 level: int = _LOG_LEVEL,
                 detail: bool = False,
                 stream: Optional[TextIO] = sys.stderr,
                 *,
                 never_cover: bool = True
                 ) -> None:
        """The initialization of logger

        Args:
            file (str, optional): The place of logs. Defaults to `log.log`.
            level (int, optional): Refer to logging.Level. Defaults to `INFO`.
            detail (bool, optional): Option to log detailed. Defaults to False.
            stream (Optional[TextIO], optional): The place of stream. \
                Defaults to `sys.stderr`.
            never_cover (bool, optional): \
                The initialization will be called only once. Defaults to True.
        """
        self.logger: logging.Logger = logging.getLogger(file)

        # `never_cover`: True, skip checking the handler has been added.
        # `never_cover`: False, check existence with `Logger._handler_table`.
        if never_cover and (not never_cover or self.logger.hasHandlers()):
            return None

        #NOTICE: `is_singleton` can not distinguish the other `log_file`.
        #if Logger.is_singleton:
        #    Logger.is_singleton = False
        #    return None
        #

        # Set logger level directly while *initializing* or to the smaller.
        # *initializing* means there is no handler whatever stream or file.
        # [level] 10: DEBUG, 20: INFO, 30: WARNING, 40: ERROR, 50: CRITICAL
        if self.logger.hasHandlers():
            self.logger.setLevel(min(self.logger.getEffectiveLevel(), level))
        else:
            self.logger.setLevel(level)

        # Setup the format of logger
        formatter: logging.Formatter = logging.Formatter(
            "{asctime} - {filename} - {levelname} - {funcName} - {message}",
            "%m-%d-%Y %H:%M:%S",
            '{'
        ) if detail else logging.Formatter(
            "{asctime} - {filename} - {levelname} - {message}",
            "%m-%d %H:%M:%S",
            '{'
        )

        # Add the handlers about stream and file to logger.
        # Add stream handler after checking its existence with (file, stream).
        if stream is None:
            pass
        elif (file, stream) not in Logger._handler_table:
            streamer: logging.StreamHandler = logging.StreamHandler(stream)
            streamer.setFormatter(formatter)

            Logger._handler_table[(file, stream)] = len(self.logger.handlers)
            self.logger.addHandler(streamer)
        elif detail:    # `detail` is True has priority.
            self.logger.handlers[Logger._handler_table[(
                file, stream)]].setFormatter(formatter)

        # Add file handler after checking its existence with (file,).
        if (file,) not in Logger._handler_table:
            file_handler: logging.FileHandler = logging.FileHandler(file)
            file_handler.setFormatter(formatter)

            Logger._handler_table[(file,)] = len(self.logger.handlers)
            self.logger.addHandler(file_handler)
        elif detail:    # `detail` is True has priority.
            self.logger.handlers[Logger._handler_table[
                (file,)]].setFormatter(formatter)

    def __call__(self, *args, **kwargs):
        if args or kwargs:
            #NOTICE: Do something here if args or kwargs is not empty.
            pass

        # Get caller name from `kwargs` while passing `__file__` as `caller`.
        if kwargs.get("caller") is not None:
            Logger.caller = cast(str, (kwargs['caller'])).rsplit('\\')[-1]
        self.logger.debug(f"{Logger.caller} is called.")

        # Print the current handlers, ensure there are no duplicates.
        self.logger.debug(f"{self.logger.handlers=}")

        return self.logger

    #TODO: clear log file

    #TODO: move log


#%%    Main Function


#%%    Main
if __name__ == '__main__':
    _LOG_MODE = "DEBUG"    #for test/DEBUG

    logger: Logger = Logger(never_cover=False)()

    logger.info("Test")      #10

    logger.debug("Test")     #20

    logger.warning("Test")   #30

    logger.error("Test")     #40

    logger.critical("Test")  #50

    #NOTE:
    #logging.exception() is equal to logging.error(exc_info=True)

    another_logger: Logger = Logger(_LOG_STATUS, never_cover=False)()

    another_logger.info("Test")

    another_logger.debug("Test")

#%%
