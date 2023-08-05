package main

import (
	"fmt"
)

func getSum(a int, b int) int {
	for b != 0 {
		var tmp int = (a & b) << 1
		a = a ^ b
		b = tmp
	}

	return a
}

func main() {
	// Test cases
	testCases := [][]int{
		{2, 3},   // Expected output: 5
		{-1, 1},  // Expected output: 0
		{10, -5}, // Expected output: 5
		{0, 0},   // Expected output: 0
	}

	// Run test cases
	for _, testCase := range testCases {
		a, b := testCase[0], testCase[1]
		result := getSum(a, b)
		fmt.Printf("getSum(%d, %d) = %d\n", a, b, result)
	}
}
