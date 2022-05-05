from typing import Optional


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        start = 0
        trace = {}
        for index, ch in enumerate(s):
            if ch in trace and trace[ch] >= start:
                length = max(length, index-start)
                start = trace[ch] + 1
            trace[ch] = index
        return max(length, len(s) - start)


def main():
    s = Solution()
    print(s.lengthOfLongestSubstring("asdfasdfwefad"))


if __name__ == "__main__":
    main()
