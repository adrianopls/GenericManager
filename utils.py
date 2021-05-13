# -*- coding: utf-8 -*-
"""
Created on Thu May 13 16:07:20 2021

@author: Adriano
"""

import timeit
import importlib


def get_function_from_string(fullpath_function):
    try:
        #print ('\nget_function_from_string:', fullpath_function)
        module_str = '.'.join(fullpath_function.split('.')[:-1]) 
        function_str = fullpath_function.split('.')[-1]
        #print ('importing module:', module_str)
        module_ = importlib.import_module(module_str)
        #print ('getting function:', function_str, '\n')
        function_ = getattr(module_, function_str)
        return function_    
    except Exception as e:
        msg = 'ERROR in function app.app_utils.get_function_from_string({}).'.format(fullpath_function)
#        log.exception(msg)
        print (msg)
        raise e        
             
        
        
        
class Chronometer(object):
    
    def __init__(self):
        self.start_time = timeit.default_timer()
    
    def end(self):
        self.total = timeit.default_timer() - self.start_time
        return 'Execution in {:0.3f}s'.format(self.total)        
                  