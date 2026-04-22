package main

import "log/slog"

func main() {
	slog.Info("Starting the secure application...")

	if err := doSomething(); err != nil {
		slog.Error("Failed to execute", "error", err)
	}
}

func doSomething() error {
	return nil
}
