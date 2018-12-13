import datetime as dt
import os
import sys


class Error(object):
    """CLASS: take care of all error logging for card game

    METHODS
        >> log_error(error, f_name)
            STATIC: makes a log entry for the error and function name passed to it

        >> __build_file()
            STATIC: builds a file when it doesn't already exist.

    """

    @staticmethod
    def log_error(error, f_name):
        """METHOD: logs the error and funtion name passed to it along with the current datetime

        PARAMETERS
            @error(string): the error which occured
            @f_name(string): the function in which the error occured

        RETURNS
            @filename(string): the name of the file which logs were writted to

        """
        filename = "ErrorLogs/GameErrorLog%s" % str(dt.datetime.today().strftime("%y-%m-%d"))
        if not os.path.isfile(filename):
            Error.__build_file()

        with open(filename, "a") as file:
            file.write("%s ::: in function [%s] ::: %s\n" % (error, f_name, dt.datetime.now()))
        return filename

    @staticmethod
    def __build_file():
        """METHOD: builds a log file when one doesn't exist

        RETURNS
            None
        """
        filename = "ErrorLogs/GameErrorLog%s" % str(dt.datetime.today().strftime("%y-%m-%d"))
        with open(filename, "w") as file:
            file.write("Error log for game instantiation made on %s\n\n" % (dt.datetime.today().strftime("%y-%m-%d")))


def main():
    date = dt.datetime.today().strftime("%y-%m-%d")
    filename = "ErrorLogs/GameErrorLog%s" % date
    Error.log_error("ValueError", "Error.build_file")
    try:
        john = int("ggh")
    except:
        Error.log_error(sys.exc_info()[1], "Error.main()")
    print("To Use Error Logging, please place a call to Error.log_error()\n")
    print("This function takes 2 parameters: 1. the error which occured (sys.exc_info()[1])\n")
    print("2.The name of the function as Class.function_name()\n")


if __name__ == "__main__":
    main()