这道题，如果用传统思维就是两个for循环，然后找出对应的两个数字的index即可。但是这种方式显然是O(n2)的。
那么题目中提示到了不提倡使用O(n2)， 那么我们就考虑用哈希表来实现。思路是：list中的index作为key，list的value 作为哈希表中对应value, 如果values 相加为target,直接返回对应keys即可。
要注意的是： 需要先if判断，再进行hash赋值操作，可以考虑下这个test case， nums = [3,2,4], target = 6, 就明白这么作的意图了。
