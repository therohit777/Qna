class Questions:
    count=0
    def __init__(self,ans,response):
        self.ans=ans
        self.response=response
    def check(self):
        if(self.response==self.ans):
            return 1
        else:
            return 0
        

