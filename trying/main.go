package main

const (
	healthyThreshold = 50
	sampleScore      = 100
)

// CalculateStatus evaluates the system health.
func CalculateStatus(score int) string {
	if score > healthyThreshold {
		return "Healthy"
	}

	return "Warning"
}

func main() {
	_ = CalculateStatus(sampleScore)
}
