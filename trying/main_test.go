package main

import "testing"

func TestCalculateStatus(t *testing.T) {
	// Test the "Healthy" path
	res1 := CalculateStatus(100)
	if res1 != "Healthy" {
		t.Errorf("Expected Healthy, got %s", res1)
	}

	// Test the "Warning" path
	res2 := CalculateStatus(10)
	if res2 != "Warning" {
		t.Errorf("Expected Warning, got %s", res2)
	}
}
