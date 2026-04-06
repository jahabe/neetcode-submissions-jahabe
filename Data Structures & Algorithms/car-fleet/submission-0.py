class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))  # pos 오름차순
        stack = []  # fleet 도착 시간들
        reversedCars = reversed(cars)

        for pos, spd in reversedCars:  # pos 큰 것부터 (target에 가까운 차부터)
            t = (target - pos) / spd

            # 새 fleet: 이전 fleet(앞차)보다 더 늦게 도착하면 못 잡음
            if not stack or t > stack[-1]:
                stack.append(t)
            # else: t <= stack[-1] 이면 catch up -> 같은 fleet (push 안 함)

        return len(stack)