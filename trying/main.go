package main

import (
	"context"
	"errors"
	"log/slog"
	"os"
)

// ErrProcessingFailed represents a custom error to demonstrate proper error handling.
var ErrProcessingFailed = errors.New("internal processing error")

func main() {
	// Initialize a structured JSON logger to stdout.
	logger := slog.New(slog.NewJSONHandler(os.Stdout, nil))
	slog.SetDefault(logger)

	ctx := context.Background()
	slog.InfoContext(ctx, "Sijil-CI: Starting compliant Go service")

	if err := runSystemCheck(ctx); err != nil {
		slog.ErrorContext(ctx, "System check failed", "error", err)
		os.Exit(1)
	}

	slog.InfoContext(ctx, "System check passed. Service is healthy.")
}

// runSystemCheck simulates a task that complies with strict linting rules.
func runSystemCheck(ctx context.Context) error {
	// Logic goes here. Returning nil to simulate success.
	slog.DebugContext(ctx, "Performing health check...")

	return nil
}
