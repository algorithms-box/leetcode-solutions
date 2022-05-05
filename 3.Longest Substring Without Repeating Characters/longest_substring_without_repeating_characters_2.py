

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start_cursor, max_length, char_dict = -1, 0, {}

        for index, ch in enumerate(s):
            if ch in char_dict and char_dict[ch] > start_cursor:
                # print the string without repeating chars for now
                # print(char_dict)
                # let start_cursor move to char ch last one position before this loop
                start_cursor = char_dict[ch]
                char_dict[ch] = index
            else:
                char_dict[ch] = index
                max_length = max(max_length, index-start_cursor)
        return max_length


def max(x: int, y: int) -> int:
    if x > y:
        return x
    return y


def main():
    s = Solution()
    print(s.lengthOfLongestSubstring("asdfasdfwefad"))


if __name__ == "__main__":
    main()
