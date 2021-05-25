
import logging 
import timeit
import importlib


def get_function_from_string(fullpath_function):
    try:
        module_str = '.'.join(fullpath_function.split('.')[:-1]) 
        function_str = fullpath_function.split('.')[-1]
        module_ = importlib.import_module(module_str)
        function_ = getattr(module_, function_str)
        return function_    
    except:
        msg = 'ERROR in function app.app_utils.get_function_from_string({}).'.format(fullpath_function)
        logging.exception(msg)
      
             
class Chronometer(object):
    
    def __init__(self):
        self.start_time = timeit.default_timer()
        self.total = None
  
    def finish(self):  
        self.total = timeit.default_timer() - self.start_time
        self.start_time = None
                    
    def get_message(self):
        return 'Execution in {:0.3f}s'.format(self.total)  