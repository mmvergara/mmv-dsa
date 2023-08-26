class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        n = len(seats)
        seats = sorted(seats)
        students = sorted(students)

        moves = 0

        for i in range(n):
            moves+=abs(seats[i]-students[i])

        return moves

