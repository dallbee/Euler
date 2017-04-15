package main

import "fmt"

func Generate(limit int, muls ...int) (sum int) {
	for i := 0; i < limit; i++ {
		for _, m := range muls {
			if i%m == 0 {
				sum += i
				break
			}
		}
	}
	return sum
}

func main() {
	fmt.Println(Generate(1000, 3, 5))
}
