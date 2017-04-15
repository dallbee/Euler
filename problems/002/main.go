package main

import "fmt"

func main() {
	var sum, a, b int64
	a, b = 1, 2
	for {
		a, b = b, a+b
		if a > 4000000 {
			break
		}
		if a%2 == 0 {
			sum += a
		}
	}

	fmt.Println(sum)
}
