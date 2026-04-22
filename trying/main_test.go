package main

import "testing"

func TestCalculateStatus(t *testing.T) {
	t.Parallel() // Satisfies paralleltest

	// Test the "Healthy" path
	res1 := CalculateStatus(DefaultTestScore)
	if res1 != "Healthy" {
		t.Errorf("Expected Healthy, got %s", res1)
	}

	// Test the "Warning" path
	res2 := CalculateStatus(10)
	if res2 != "Warning" {
		t.Errorf("Expected Warning, got %s", res2)
	}
}
