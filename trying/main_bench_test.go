package main

import "testing"

func BenchmarkBasic(b *testing.B) {
	for i := 0; i < b.N; i++ {
		// Basic benchmark test
		_ = i * 2
	}
}
