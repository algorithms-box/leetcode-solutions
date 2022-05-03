from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, num in enumerate(nums):
            if target - num in hashMap:
                return [hashMap[target - num], i]
            hashMap[num] = i
            # Note: have to judgement goes firt, then put it into hashMap
            # think of the test case: [3,2,4] 6
        return []


def main():
    # nums = [1, 5, 3, 15, 33]
    # target = 8
    nums = [3, 2, 4]
    target = 6
    s = Solution()
    result = s.twoSum(nums, target)
    print(result)


if __name__ == "__main__":
    main()
