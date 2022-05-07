class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        tmpMap = {}
        for left_cursor, ch in enumerate(s):
            tmpMap.clear()
            for right_cursor, c in enumerate(s):
                if right_cursor >= left_cursor:
                    # Note, if the substring without repeating chars is end with tail,
                    # then we need take care of that
                    if c in tmpMap or right_cursor == len(s):
                        break
                    # in fact, here we can store anything in tmpMap, we don't care the value
                    tmpMap[s[right_cursor]] = right_cursor
            print("length : {0}, dict is {1}".format(len(tmpMap), tmpMap))
            max_length = max(max_length, len(tmpMap))
        return max_length


def main():
    s = Solution()
    print(s.lengthOfLongestSubstring("asfdgdsfgsdffdgergsdfsadfwefdsacv"))


if __name__ == "__main__":
    main()
