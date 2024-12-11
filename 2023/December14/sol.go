package main

import (
	"fmt"
	"os"
	"bufio"
)

var cache = map[string]int{}

func tiltUp(board []string) []string {
	newBoard := []string{}
	for _, line := range board {
		newLine := ""
		stoneCount := 0
		hashTagPositions := map[int]bool{}
		stonePositions := map[int]bool{}
		for i, char := range line {
			if char == '#' {
				hashTagPositions[i] = true
				stoneCount = i + 1
			} else if char == 'O' {
				stonePositions[stoneCount] = true
				stoneCount++
			}
		}
		for i := 0; i < len(line); i++ {
			if stonePositions[i] {
				newLine += "O"
			} else if hashTagPositions[i] {
				newLine += "#"
			} else {
				newLine += "."
			}
		}
		newBoard = append(newBoard, newLine)
	}
	return newBoard
}

func tiltDown(board []string) []string {
	newBoard := []string{}
	for _, line := range board {
		newLine := ""
		stoneCount := len(line) - 1
		hashTagPositions := map[int]bool{}
		stonePositions := map[int]bool{}
		for i := len(line) - 1; i >= 0; i-- {
			char := line[i]
			if char == '#' {
				hashTagPositions[i] = true
				stoneCount = i-1
			} else if char == 'O' {
				stonePositions[stoneCount] = true
				stoneCount--
			}
		}
		for i := 0; i < len(line); i++ {
			if stonePositions[i] {
				newLine += "O"
			} else if hashTagPositions[i] {
				newLine += "#"
			} else {
				newLine += "."
			}
		}
		newBoard = append(newBoard, newLine)
	}
	return newBoard
}

func switchDirection(direction []string) []string {
	newDirection := []string{}
	for _, line := range direction {
		if len(newDirection) == 0 {
			for i := 0; i < len(line); i++ {
				newDirection = append(newDirection, "")
			}
		}
		for i, char := range line {
			newDirection[i] += string(char)
		}
	}
	return newDirection
}

func oneCycle(board []string) []string {
	tiltUpBoard := tiltUp(board)
	rowTopBoard := switchDirection(tiltUpBoard)
	tiltLeftBoard := tiltUp(rowTopBoard)
	columnLeftBoard := switchDirection(tiltLeftBoard)
	tiltDownBoard := tiltDown(columnLeftBoard)
	rowBottomBoard := switchDirection(tiltDownBoard)
	tiltRightBoard := tiltDown(rowBottomBoard)
	columnRightBoard := switchDirection(tiltRightBoard)
	return columnRightBoard
}

func printBoard(board []string, direction string) {
	if direction == "row" {
		for _, line := range board {
			fmt.Println(line)
		}
	} else {
		for _, line := range switchDirection(board) {
			fmt.Println(line)
		}
	}
	fmt.Println()
}

func calculateLoad(board []string) int {
	load := 0
	for _, line := range board {
		initialLoad := len(line)
		for i, char := range line {
			if char == 'O' {
				load += initialLoad - i
			}
		}
	}
	return load
}


func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	columns := []string{}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		if len(columns) == 0 {
			for i := 0; i < len(line); i++ {
				columns = append(columns, "")
			}
		}
		for i := 0; i < len(line); i++ {
			columns[i] += string(line[i])
		}
	}
	columns = oneCycle(columns)
	limit := 1_000_000_000
	for i := 0; i < limit; i++ {
		cacheKey := ""
		for _, line := range columns {
			cacheKey += line
		}
		if val, ok := cache[cacheKey]; ok {
			// Jump all cycles possible
			i = limit - (limit - val) % (i - val)
			cache = map[string]int{}
			continue
		}
		columns = oneCycle(columns)
		cache[cacheKey] = i
	}
	fmt.Println(calculateLoad(columns))
}
