import sys  

def error_message_detail(error,error_details:sys):
    _,_,exc_tb = error_details.exc_info()  ## all the expection message store here
    file_name =exc_tb.tb_frame.f_code.co_filename    
    error_message= "error occured in python script name [{0}] line no [{1}] error message[{2}]".format(
    file_name,exc_tb.tb_lineno,str(error)
    
    return error_message
    )
    
class CustomException(): 
    def __init__(self,error_message,error_detail:sys):
        super.__init__(error_message)
        self.error_message = error_message_detail(error_message,error_details=error_detail)
        
        
        def __str__(self):
            return self.error_message