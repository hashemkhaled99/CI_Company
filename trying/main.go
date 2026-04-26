package main

import (
	"log/slog"
)

// Constants to satisfy GOMND (mnd) and improve maintainability.
const (
	HealthyThreshold = 50
	DefaultTestScore = 100
)

// CalculateStatus evaluates the system health.
func CalculateStatus(score int) string {
	if score > HealthyThreshold {
		return "Healthy"
	}

	// Added a blank line here to satisfy nlreturn.
	return "Warning"
}

func main() {
	status := CalculateStatus(DefaultTestScore)
	slog.Info("System Status", "value", status)
}
