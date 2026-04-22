package main

import "testing"

func TestRunSystemCheck(t *testing.T) {
	t.Parallel() // Satisfies paralleltest linter

	err := runSystemCheck()
	if err != nil {
		t.Errorf("expected nil, got %v", err)
	}
}
