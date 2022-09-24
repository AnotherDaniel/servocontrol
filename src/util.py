#!/usr/bin/python3
import inspect
import logging

def log_info( func ):
    def wrapper( *args, **kwargs ):
        frm = inspect.stack()[1]
        mod = inspect.getmodule(frm[0])
        logger = logging.getLogger(mod.__name__)
        logger.info( "Called "+func.__name__+" with " + " ".join([str(arg) for arg in args]) )
        val = func(*args, **kwargs) 
        return val
    return wrapper