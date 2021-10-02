def byte_size(string):
    return(len(string.encode('utf-8')))
    
    
byte_size('😀') 
byte_size('Hello World')    
