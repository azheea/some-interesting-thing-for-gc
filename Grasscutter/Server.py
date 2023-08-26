class GCServer:
    def __init__(self,url:str="127.0.0.1",port:int=443,token:str="azhegod"):
        self.console_token = token
        self.port = port
        self.url = url
        return self.port,self.url,self.console_token
        
        
    def url(link:str="127.0.0.1") -> str:
        return str(link)

    def console_token(token:str="azhegod") -> str:
        return str(token)

    def port(port:int=443) -> int:
        return int(port)