class Alert:
    def __init__(self):
        import datetime
        today=list(str(datetime.datetime.now()).split())[0]
        path="./Logs/logs"+str(today)+".txt"
        with open(path, "a+") as f1:
            f1.seek(0,0)
            x=f1.readlines()
            arr=x[-5:-2:]
            for i in arr:
                if("Intruder_Alert" in i):
                    # print("send mail")
                    import sendAlert as SA
                    SA.SendAlert("Security Alert: Suspicious activity detected. Immediate attention required.\n\n"+i)
                    print("Send Alert to Admin, done..................")
                    break
    def test(sub="test subject", msg="test messsage"):
        print(sub,"\n",msg)