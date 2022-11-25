"""

There is a chess round that starts every 15 minutes.
The first round of the day starts at 00:00
Given:
loginTime is the time you will login to the game
logoutTime is the time you will logout from the game.

logoutTime < loginTime it means one complete day

Return the number of full chess rounds you have played in the tournament.

Examples
Input: loginTime = "09:31", logoutTime = "10:14"
Input: loginTime = "21:30", logoutTime = "03:00"

15
30
60
75
90
...
1290
570
571
Constraints:

loginTime and logoutTime are in the format hh:mm.
00 <= hh <= 23
00 <= mm <= 59
loginTime and logoutTime are not equal.

TODO verify complexity
Complexity : On
Space : On

"""


class Solution:

    def nearest_down(self, number):
        mo = number % 15
        return number - mo

    def nearest_up(self, number):
        mo = number % 15
        if mo == 0:
            return number
        else:
            divi = (number - mo) / 15
            return (divi + 1) * 15

    def to_minutes(self, time):
        info = time.split(":")
        return (int(info[0]) * 60) + int(info[1])

    def rest_in_minutes(self, h_in, m_in, h_out, m_out):
        if m_in > m_out:
            m_out += 60
            h_out -= 1
        if h_in > h_out:
            h_out += 24
        return (h_out - h_in) * 60 + (m_out - m_in)

    def to_hour_minute(self, time):
        minut = time % 60
        time = time - minut
        hour = time / 60
        return int(hour), int(minut)

    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        login_in_min = self.to_minutes(loginTime)
        logout_in_min = self.to_minutes(logoutTime)

        if login_in_min < logout_in_min and logout_in_min - login_in_min < 15:
            return 0

        login_in_min = self.nearest_up(login_in_min)
        logout_in_min = self.nearest_down(logout_in_min)

        login_hour, login_min = self.to_hour_minute(login_in_min)
        logout_hour, logout_min = self.to_hour_minute(logout_in_min)

        res = self.rest_in_minutes(login_hour, login_min, logout_hour, logout_min)
        return int(res // 15)


if __name__ == '__main__':
    s = Solution()
    r = s.numberOfRounds("00:47", "00:57")
    print(r)
