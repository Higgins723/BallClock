class BallClock {
    constructor(ballsCount) {
        this.ballsCount = ballsCount;
        this.halfDay = 0;
        this.main = this.initBallArray();
        this.initQueue = this.initBallArray();
        this.mins = [];
        this.fiveMinutes = [];
        this.hoursAmount = [];
    }

    startClock() {
        // # also I needed to make sure that it was added one to the minute track, changed to while true
        var startTime = performance.now()
        while (true) {
            this.addOneMin(this.main.shift());
            if (this.checkReachedStart() === true) {
                break;
            }
        }
        var endTime = performance.now()

        var message = this.ballsCount + " balls cycle after " + (this.halfDay / 2) + " days.";
        console.log(message);

        var timeToRun = "Completed in " +  (endTime - startTime) + " milliseconds (" + ((endTime-startTime)/1000) + " seconds)";
        console.log(timeToRun);

        return message;
    }

    checkReachedStart() {
        if (this.main.length !== this.ballsCount) {
            return false;
        }

        for (var i = 0; i < this.ballsCount; i++) {
            if (this.main[i] !== this.initQueue[i]) {
                return false;
            }
        }
        return true;
    }

    // # the error existed here: I was not doing <= so it was off by one
    initBallArray() {
        var ballArray = [];
        for (var i = 1; i <= this.ballsCount; i++) {
            ballArray.push(i);
        }
        return ballArray;
    }

    addOneMin(ball) {
        if (this.mins.length < 4) {
            this.mins.push(ball)
        } else {
            this.clearMins();
            this.addFiveMin(ball);
        }
    }

    addFiveMin(ball) {
        if (this.fiveMinutes.length < 11) {
            this.fiveMinutes.push(ball);
        } else {
            this.clearFiveMins();
            this.addOneHour(ball);
        }
    }

    addOneHour(ball) {
        if (this.hoursAmount.length < 11) {
            this.hoursAmount.push(ball);
        } else {
            this.clearHours();
            this.main.push(ball);
            this.halfDay = this.halfDay + 1;
        }
    }

    clearMins() {
        while (this.mins.length > 0) {
            this.main.push(this.mins.pop());
        }
    }

    clearFiveMins() {
        while (this.fiveMinutes.length > 0) {
            this.main.push(this.fiveMinutes.pop());
        }
    }

    clearHours() {
        while (this.hoursAmount.length > 0) {
            this.main.push(this.hoursAmount.pop());
        }
    }
}

class BallClockMins extends BallClock {
    constructor(ballsCount, minCount) {
        super(ballsCount);
        this.minCount = minCount;
    }

    startClock() {
        for (var i = 0; i < this.minCount; i++) {
            this.addOneMin(this.main.shift());
        }

        var json = {"Min": this.mins, "FiveMin": this.fiveMinutes, "Hour": this.hoursAmount, "Main": this.main};
        console.log(json);
    }
}

function runClock() {
    new BallClock(45).startClock();
    new BallClockMins(30, 325).startClock();
}