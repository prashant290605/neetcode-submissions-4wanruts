class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(speed)):
            cars.append((position[i],speed[i]))
        cars = sorted(cars)
        cars = cars[::-1]
        time = [0]*len(cars)
        for i in range(len(cars)):
            time[i] = float((target-cars[i][0])/cars[i][1])

        stack = []
        stack.append(time[0])
        for i in range(1,len(time)):
            if time[i] > stack[-1]:
                stack.append(time[i])
        return len(stack)