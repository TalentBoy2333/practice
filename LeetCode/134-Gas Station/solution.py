class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        num = len(gas)
        cur_sum = 0
        ind = 0
        total = 0
        for i in range(num):
            cur_sum += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if cur_sum <= 0:
                cur_sum = 0
                ind = i + 1
        if total < 0:
            return -1
        else:
            return ind % num
        