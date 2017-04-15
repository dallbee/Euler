package main

import "testing"

func Test(t *testing.T) {
	sum := Generate(10, 3, 5)
	if sum != 23 {
		t.Errorf("Got %d, expected %d", sum, 23)
	}
}
