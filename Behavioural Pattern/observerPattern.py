# Observer patterns are nothing but a publisher subscriber model


class DataChannel:
    def __init__(self,name):
        self.name = name
        self.subscriber = []
    
    def subscribe(self,sub):
        self.subscriber.append(sub)
    
    def notify(self, events):
        for sub in self.subscriber:
            sub.sendNotification(self.name,events)



from abc import ABC, abstractmethod

class DataUsers(ABC):
    def __init__(self,name):
        self.name = name
    
    def sendNotification(self,channel, event):
        print(f" User {self.name} received notification for {channel} : {event}")


channel = DataChannel("Buy Apple Stocks")
channel.subscribe(DataUsers("sub1"))
channel.subscribe(DataUsers("sub2"))
channel.subscribe(DataUsers("sub3"))


channel.notify("New fund data received")