###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE
    nextYear = year
    if(day == 30):
        nextDay = 1
        nextMonth = month + 1
    else:
        nextDay = day + 1
        nextMonth = month
    if(month == 12):
        nextMonth = 1
        nextYear = year + 1
    else:
        nextMonth = month + 1
        nextYear = year
    return (nextYear,nextMonth, nextDay)
