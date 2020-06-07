class Time(object):
    sec:int = 0
    min:int = 0
    hr:int = 0

    def setSec(self, s):
        self.sec = s
    def setMin(self, m):
        self.min = m
    def setHour(self, h):
        self.hr = h

    def getSec(self):
        return self.sec
    def getMin(self):
        return self.min
    def getHour(self):
        return self.hr

    def __str__(self):
        return str(self.getHour()) + ":" + str(self.getMin()) + ":" + str(self.getSec())

class Date(object):
    day:int = 0
    mon:int = 0
    yr:int = 0

    def setDay(self, d):
        self.day = d
    def setMon(self, m):
        self.mon = m
    def setYear(self, y):
        self.yr = y

    def getDay(self):
        return self.day
    def getMon(self):
        return self.mon
    def getYear(self):
        return self.yr

    def __str__(self):
        return str(self.getDay()) + "/" + str(self.getMon() + ":" + str(self.getYear())

class Reminders(object):
    time:Time = null
    date:Date = null
    task:str = ""

    def setTime(self, tm):
        self.time = tm
    def setDate(self, dt):
        self.date = dt
    def setTask(self, tsk):
        self.task = tsk

    def getTime(self):
        return self.time
    def getDate(self):
        return self.date
    def getTask(self):
        return self.task

    def __str__(self):
        output = str(self.getDate()) + "  - " + str(self.getTime())
        output += "\n" + self.getTask()
        return output

#Main
qtd = int(input())

for i in range(qtd)
    dayData = Date()
