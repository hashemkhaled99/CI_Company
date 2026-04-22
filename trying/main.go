package main

import (
	"errors"
	"log/slog"
)

// ErrSample represents a generic error for demonstration.
var ErrSample = errors.New("something went wrong")

func main() {
	// Using slog instead of fmt/log to comply with depguard
	slog.Info("Starting the Sijil-CI validated application...")

	if err := performTask(); err != nil {
		slog.Error("Task failed", "error", err)
	}
}

// performTask is a compliant function that returns an error.
func performTask() error {
	// Simple logic to demonstrate a successful pass
	return nil
}
