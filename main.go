package main

import "time"

func main() {
	start := time.Now()
	time.Sleep(1 * time.Second)
	t := time.Now()
	elapsed := t.Sub(start)
	println(elapsed.Milliseconds() / 10)
}
