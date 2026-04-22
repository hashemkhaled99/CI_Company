package main

import "testing"

func TestRunSystemCheck(t *testing.T) {
	// Tells the linter this test can run alongside others
	t.Parallel()

	err := runSystemCheck()
	if err != nil {
		t.Errorf("expected nil, got %v", err)
	}
}
