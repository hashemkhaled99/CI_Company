package main

import "testing"

func TestRunSystemCheck(t *testing.T) {
	err := runSystemCheck()
	if err != nil {
		t.Errorf("expected nil, got %v", err)
	}
}
