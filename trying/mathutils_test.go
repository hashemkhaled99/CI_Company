package mathutils

import "testing"

func TestAdd(t *testing.T) {
	if got := Add(2, 3); got != 5 {
		t.Errorf("Add(2,3) = %d; want 5", got)
	}
}

func TestSubtract(t *testing.T) {
	if got := Subtract(5, 3); got != 2 {
		t.Errorf("Subtract(5,3) = %d; want 2", got)
	}
}

func TestMultiply(t *testing.T) {
	if got := Multiply(4, 5); got != 20 {
		t.Errorf("Multiply(4,5) = %d; want 20", got)
	}
}

func TestDivide(t *testing.T) {
	got, err := Divide(10, 2)
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if got != 5 {
		t.Errorf("Divide(10,2) = %d; want 5", got)
	}
}

func TestDivideByZero(t *testing.T) {
	_, err := Divide(5, 0)
	if err == nil {
		t.Fatal("expected error for division by zero")
	}
}

func TestFactorial(t *testing.T) {
	tests := []struct {
		input    int
		expected int
	}{
		{0, 1},
		{1, 1},
		{5, 120},
	}
	for _, tc := range tests {
		got, err := Factorial(tc.input)
		if err != nil {
			t.Fatalf("Factorial(%d) error: %v", tc.input, err)
		}
		if got != tc.expected {
			t.Errorf("Factorial(%d) = %d; want %d", tc.input, got, tc.expected)
		}
	}
}

func TestFactorialNegative(t *testing.T) {
	_, err := Factorial(-1)
	if err == nil {
		t.Fatal("expected error for negative input")
	}
}

func TestIsEven(t *testing.T) {
	if !IsEven(4) {
		t.Error("IsEven(4) should be true")
	}
	if IsEven(3) {
		t.Error("IsEven(3) should be false")
	}
}

func BenchmarkAdd(b *testing.B) {
	for i := 0; i < b.N; i++ {
		Add(1000, 2000)
	}
}

func BenchmarkFactorial(b *testing.B) {
	for i := 0; i < b.N; i++ {
		Factorial(10)
	}
}
