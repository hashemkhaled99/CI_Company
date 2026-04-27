package main

// CalculateStatus evaluates the system health.
func CalculateStatus(score int) string {
	if score > 50 {
		return "Healthy"
	}
	return "Warning"
}

func main() {
	_ = CalculateStatus(100)
}
