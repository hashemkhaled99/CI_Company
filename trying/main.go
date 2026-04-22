package main

import (
	"log/slog"
)

// CalculateStatus needs to be here for the test to find it!
func CalculateStatus(score int) string {
	if score > 50 {
		return "Healthy"
	}
	return "Warning"
}

func main() {
	status := CalculateStatus(100)
	slog.Info("System Status", "value", status)
}
