package main

import (
	"context"
	"log/slog"
	"os"
)

func main() {
	// Initialize structured logger.
	logger := slog.New(slog.NewJSONHandler(os.Stdout, nil))
	slog.SetDefault(logger)

	ctx := context.Background()
	slog.InfoContext(ctx, "Sijil-CI: Starting compliant service")

	if err := runSystemCheck(); err != nil {
		slog.ErrorContext(ctx, "Check failed", "error", err)
		os.Exit(1)
	}
}

// runSystemCheck performs a simple health check.
func runSystemCheck() error {
	slog.Info("Performing health check...")

	return nil
}
