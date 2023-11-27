class Auth:
    def __init__(self, keyword, timestamp):
        self.alert=keyword
        self.timestamp=timestamp
        print(self.alert,self.timestamp)
        self.log()
    def log(self):
        import datetime
        today=list(str(datetime.datetime.now()).split())[0]
        path="./Logs/logs"+str(today)+".txt"
        with open(path, "a") as f1:
            log=self.alert+str(" ")+str(self.timestamp)+str("\n")
            f1.write(log)
    