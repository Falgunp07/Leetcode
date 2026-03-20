class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

        def get_day(date):
            month = int(date[:2])
            day = int(date[3:])
            return sum(days_in_month[:month-1]) + day

        a_start = get_day(arriveAlice)
        a_end = get_day(leaveAlice)
        b_start = get_day(arriveBob)
        b_end = get_day(leaveBob)

        start = max(a_start, b_start)
        end = min(a_end, b_end)

        if start > end:
            return 0

        return end - start + 1