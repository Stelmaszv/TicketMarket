from datetime import timedelta
class abstractTime:
    def __init__(self,item):
        self.item=item
class newTime(abstractTime):
    def time(self):
        objc={}
        objc['hours']=houer(self.item)
        objc['minutes'] = minutes(self.item)
        objc['weeks'] = weeks(self.item)
        objc['days'] = weeks(self.item)
        objc['seconds'] = weeks(self.item)
        return objc[self.item.cyclycetype.name].setTime()
class houer(abstractTime):
    def setTime(self):
        return timedelta(hours=self.item.cyclycetvalue)
class minutes(abstractTime):
    def setTime(self):
        return timedelta(minutes=self.item.cyclycetvalue)
class weeks(abstractTime):
    def setTime(self):
        return timedelta(weeks=self.item.cyclycetvalue)
class days(abstractTime):
    def setTime(self):
        return timedelta(days=self.item.cyclycetvalue)
class seconds(abstractTime):
    def setTime(self):
        return timedelta(seconds=self.item.cyclycetvalue)