# DT249 - Programming and Algorithms 2
# Conor O'Donovan
# Labs - Week 1 - Clock


class Clock:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    def get_hours(self):
        return self._hours

    def get_minutes(self):
        return self._minutes

    def get_seconds(self):
        return self._seconds

    def __str__(self):
        return "00:00:00am"

    def __repr__(self):
        return "{}({},{},{})".format(self.__class__.__name__, self._hours, self._minutes, self._seconds)

    def str_update(self, new_time_str = "00:00:00"):
        self._hours = int("{}{}".format(new_time_str[0], new_time_str[1]))
        self._minutes = int("{}{}".format(new_time_str[3], new_time_str[4]))
        self._seconds = int("{}{}".format(new_time_str[6], new_time_str[7]))

    def print_clock(self):
        if self._hours > 24:
            return "Not a valid time!"

        if self._hours > 59:
            return "Not a valid time!"

        if self._hours > 59:
            return "Not a valid time!"

        if self._hours > 12:
            morning_evening = "pm"
            self._hours -= 12
        else:
            morning_evening = "am"

        if self._hours < 10:
            hours_str = "0{}".format(self._hours)
        else:
            hours_str = "{}".format(self._hours)

        if self._minutes < 10:
            minutes_str = "0{}".format(self._minutes)
        else:
            minutes_str = "{}".format(self._minutes)

        if self._seconds < 10:
            seconds_str = "0{}".format(self._seconds)
        else:
            seconds_str = "{}".format(self._seconds)

        print("{}:{}:{}{}".format(hours_str, minutes_str, seconds_str, morning_evening))

    def add_clocks(self, other_clock):
        hours = 0
        minutes = 0
        seconds = 0

        if self._seconds + other_clock.get_seconds() < 60:
            seconds += self._seconds + other_clock.get_seconds()
        else:
            seconds = 59
            minutes = 1

        if self._minutes + other_clock.get_minutes() < 60:
            minutes += self._minutes + other_clock.get_minutes()
        else:
            minutes = 59
            hours += 1

        if self._hours + other_clock.get_hours() > 23:
            hours = 23
        else:
            hours += self._hours + other_clock.get_hours()

        new_clock = Clock(hours, minutes, seconds)

        return new_clock


if __name__ == "__main__":

    # Create a new clock instance
    my_clock = Clock(20, 4, 12)

    # Print what the __str__ function returns
    print(my_clock)

    # Print what the __repr__ function returns
    print(repr(my_clock))

    # Print the clock's current values in a readable format
    my_clock.print_clock()

    # Take a string in the format "XX:XX:XX" and update the clock values accordingly
    my_clock.str_update("05:33:08")

    # Print the clock's current time again to check that it has been updated by the previous line
    my_clock.print_clock()

    # Create a new clock to add it to the existing clock
    clock1 = Clock(15, 12, 4)

    # Add the two clocks - this creates a new clock with the new values
    my_new_clock = my_clock.add_clocks(clock1)

    # Print the values of the new clock
    my_new_clock.print_clock()
