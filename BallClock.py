import time

class BallClock:
    def __init__(self, ballCount):
        self.ballCount = ballCount
        self.halfDays = 0
        self.main = self.createBallSet()
        # createQueue is for comparisons
        self.createQueue = self.createBallSet()
        self.minutes = []
        self.fiveMinutes = []
        self.hours = []

    def startClock(self):
        startTime = time.time()
        while True:
            self.addMinute(self.main.pop(0))
            if self.isBallBackToStart() == True:
                break
        endTime = time.time()

        message = "%s balls cycle after %s days." %(self.ballCount, self.halfDays / 2)
        print message

        print "Completed in %s milliseconds (%s seconds)" %(((endTime-startTime) * 1000), endTime-startTime)

        return message

    # creates the balls in an array for both main and the comparison row/track: createQueue
    def createBallSet(self):
        queue = []
        for ball_number in range(1, self.ballCount + 1):
            queue.append(ball_number)
        return queue

    # this function checks to see if main has returned to it's initial state created in createQueue
    def isBallBackToStart(self):
        if len(self.main) != self.ballCount:
            return False
        for i in range(self.ballCount):
            if self.main[i] != self.createQueue[i]:
                return False
        return True

    # this function adds a ball to the minute row/track
    def addMinute(self, ball):
        if len(self.minutes) < 4:
            self.minutes.append(ball)
        else:
            self.clearMinutesRow()
            self.addFiveMinutes(ball)

    # this function adds a ball to the five minute row/track
    def addFiveMinutes(self, ball):
        if len(self.fiveMinutes) < 11:
            self.fiveMinutes.append(ball)
        else:
            self.clearFiveMinutesRow()
            self.addHour(ball)

    # this function adds a ball to the hour row/track
    def addHour(self, ball):
        if len(self.hours) < 11:
            self.hours.append(ball)
        else:
            self.clearHoursRow()
            self.main.append(ball)
            self.halfDays += 1

    # this function clears the minutes row/track
    def clearMinutesRow(self):
        while len(self.minutes) > 0:
            self.main.append(self.minutes.pop())

        return self.minutes

    # this function clears the five minute row/track
    def clearFiveMinutesRow(self):
        while len(self.fiveMinutes) > 0:
            self.main.append(self.fiveMinutes.pop())

        return self.fiveMinutes

    # this function clears the hours row/track
    def clearHoursRow(self):
        while len(self.hours) > 0:
            self.main.append(self.hours.pop())

        return self.hours

# BallClockMinutes creates a ball clock with x number of balls and a minute_count to track the time elapsed
class BallClockMinutes(BallClock):
    def __init__(self, ballCount, minute_count):
        BallClock.__init__(self, ballCount)
        self.minute_count = minute_count

    def startClock(self):
        for i in range(1, self.minute_count + 1):
            self.addMinute(self.main.pop(0))
        json_var = {"Min": self.minutes, "FiveMin": self.fiveMinutes, "Hour": self.hours, "Main": self.main}
        print json_var




a = BallClock(45)
a.startClock()

b = BallClockMinutes(30, 325)
b.startClock()