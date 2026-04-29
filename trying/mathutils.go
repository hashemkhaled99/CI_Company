// Package mathutils provides simple mathematical utilities.
package mathutils

import "fmt"

// Add returns the sum of two integers.
func Add(a, b int) int {
	return a + b
}

// Subtract returns a minus b.
func Subtract(a, b int) int {
	return a - b
}

// Multiply returns the product of two integers.
func Multiply(a, b int) int {
	return a * b
}

// Divide returns a divided by b. Returns error on division by zero.
func Divide(a, b int) (int, error) {
	if b == 0 {
		return 0, fmt.Errorf("cannot divide by zero")
	}
	return a / b, nil
}

// Factorial returns n! (factorial of n).
func Factorial(n int) (int, error) {
	if n < 0 {
		return 0, fmt.Errorf("factorial not defined for negative numbers")
	}
	if n == 0 || n == 1 {
		return 1, nil
	}
	result := 1
	for i := 2; i <= n; i++ {
		result *= i
	}
	return result, nil
}

// IsEven checks if a number is even.
func IsEven(n int) bool {
	return n%2 == 0
}
