package main

import (
	"fmt"
	"os"
	"bufio"
)

type LeftRight struct {
	left string
	right string
}

type LeftRightMap map[string]LeftRight


func numberOfKeysApproved(keys []string) int {
	approved := 0
	for _, key := range keys {
		if string(key[2]) == "Z" {
			approved++
		}
	}
	return approved
}

func allKeysApproved(keys []string) bool {
	for _, key := range keys {
		if string(key[2]) != "Z" {
			return false
		}
	}
	return true
}

func allLoopsFound(loopLengthsForKeys map[int]int) bool {
	for _, loopLength := range loopLengthsForKeys {
		if loopLength == 0 {
			return false
		}
	}
	return true
}


// greatest common divisor (GCD) via Euclidean algorithm
func GCD(a, b int) int {
	for b != 0 {
			t := b
			b = a % b
			a = t
	}
	return a
}

// find Least Common Multiple (LCM) via GCD
func LCM(a, b int, integers ...int) int {
	result := a * b / GCD(a, b)

	for i := 0; i < len(integers); i++ {
			result = LCM(result, integers[i])
	}

	return result
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	instructions := ""
	leftRightMap := LeftRightMap{}
	currentKeys := []string{}
	i:=0
	for scanner.Scan() {
		line := scanner.Text()
		if i == 0 {
			instructions = line
			i++;
			continue
		}
		if line == "" {
			i++;
			continue
		}
		key := line[0:3]
		if string(key[2]) == "A" {
			currentKeys = append(currentKeys, key)
		}
		left := line[7:10]
		right := line[12:15]
		fmt.Println(key, left, right)
		leftRightMap[key] = LeftRight{left, right}
	}
	counter := 0
	loopLengthsForKeys := map[int]int{}
	formerCounter := map[int]int{}
	for j, _ := range currentKeys {
		loopLengthsForKeys[j] = 0
		formerCounter[j] = 0
	}
	for !allKeysApproved(currentKeys) && !allLoopsFound(loopLengthsForKeys){
		instructionsPosition := counter % len(instructions)
		for j, key := range currentKeys {
			if string(key[2]) == "Z"{
				loopLengthsForKeys[j] = counter - formerCounter[j]
				formerCounter[j] = counter
				if loopLengthsForKeys[j] > 0 {
					fmt.Println("LoopFound", loopLengthsForKeys[j], j, key)
				}
			}
		}
		currentInstruction := instructions[instructionsPosition]
		counter++
		for j, key := range currentKeys {
			if currentInstruction == 'L' {
				currentKeys[j] = leftRightMap[key].left
			} else {
				currentKeys[j] = leftRightMap[key].right
			}
		}

	}
	loops := []int{}
	for _, loopLength := range loopLengthsForKeys {
		if loopLength > 0 {
			loops = append(loops, loopLength)
		}
	}
	fmt.Println(loops)
	fmt.Println(LCM(loops[0], loops[1], loops[2], loops[3], loops[4], loops[5]))
	fmt.Println(counter)
}

