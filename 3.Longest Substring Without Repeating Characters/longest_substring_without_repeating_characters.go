package main

import "fmt"

func lengthOfLongestSubstring(s string) int {
	// boxleft := 0
	boxright := -1
	length := 0
	// use map keys cannot be same
	tmpMap := make(map[byte]int)

	for i := 0; i < len(s); i++ {
		if i != 0 {
			//every loop, let boxleft move one byte to right
			delete(tmpMap, s[i-1])
		}
		for boxright+1 < len(s) && tmpMap[s[boxright+1]] == 0 {
			tmpMap[s[boxright+1]]++
			boxright++
		}
		length = max(length, boxright-i+1)
	}

	return length

}

func max(x int, y int) int {
	if x >= y {
		return x
	}
	return y
}

func main() {
	s := "dfasdfwefwfe"
	rest := lengthOfLongestSubstring(s)
	fmt.Println(rest)
}
