package main

import (
	"fmt"
	"os"
	"bufio"
	"math"
)

type GalaxyPosition struct {
	x int
	y int
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	galaxyPositions := []GalaxyPosition{}

	emptyRows := map[int]bool{}
	emptyColumns := map[int]bool{}
	i := 0
	for scanner.Scan() {
		emptyRows[i] = true
		line := scanner.Text()
		if i == 0 {
			for j, _ := range line {
				emptyColumns[j] = true
			}
		}
		for j, char := range line {
			if string(char) == "#" {
				emptyColumns[j] = false
				emptyRows[i] = false
				galaxyPositions = append(galaxyPositions, GalaxyPosition{x: j, y: i})
			}
		}
		i++
	}
	numberOfRowShifts := 0
	for i := 0; i < len(emptyRows); i++ {
		if emptyRows[i] {
			for j, gp := range galaxyPositions {
				if gp.y > i + numberOfRowShifts * 999_999 {
					galaxyPositions[j].y += 999_999
				}
			}
			numberOfRowShifts++
		}
	}
	numberOfColumnShifts := 0
	for i := 0; i < len(emptyColumns); i++ {
		if emptyColumns[i] {
			for j, gp := range galaxyPositions {
				if gp.x > i + numberOfColumnShifts * 999_999 {
					galaxyPositions[j].x += 999_999
				}
			}
			numberOfColumnShifts++
		}
	}
	sumShortestPaths := 0.0
	// Find shortest paths and add
	for i,  pos := range galaxyPositions {
		for j := i + 1; j < len(galaxyPositions); j++ {			
			sumShortestPaths += math.Abs(float64(pos.x - galaxyPositions[j].x)) + math.Abs(float64(pos.y - galaxyPositions[j].y))
		}
	}
	fmt.Println(int(sumShortestPaths))
}

