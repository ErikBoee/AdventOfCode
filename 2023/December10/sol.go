package main

import (
	"fmt"
	"os"
	"bufio"
)

func tileContainedInLoop(i, j, numberOfRows, numberOfColumns int, verticalTilesInloop, horizontalTilesInloop map[string]string) bool {
	_, inVerticalTilesInloop := verticalTilesInloop[fmt.Sprintf("%d-%d", i, j)]
	_, inHorizontalTilesInloop := horizontalTilesInloop[fmt.Sprintf("%d-%d", i, j)]
	if inVerticalTilesInloop || inHorizontalTilesInloop {
		return false
	}

	intersectionsRight := false
	intersectionsLeft := false
	intersectionsUp := false
	intersectionsDown := false

	// Check right
	currentDirection := ""
	value := 0
	for k := j + 1; k < numberOfColumns; k++ {
		direction, ok := verticalTilesInloop[fmt.Sprintf("%d-%d", i, k)]
		if ok && direction != currentDirection {
			currentDirection = direction
			if direction == "down" {
				value++
			} else {
				value--
			}
		}
	}
	intersectionsRight = value != 0
	currentDirection = ""
	value = 0

	// Check left
	for k := j - 1; k > -1; k-- {
		direction, ok := verticalTilesInloop[fmt.Sprintf("%d-%d", i, k)]
		if ok && direction != currentDirection {
			currentDirection = direction
			if direction == "down" {
				value++
			} else {
				value--
			}
		}
	}
	intersectionsLeft = value != 0
	currentDirection = ""
	value = 0

	// Check up
	for k := i - 1; k > -1; k-- {
		direction, ok := horizontalTilesInloop[fmt.Sprintf("%d-%d", k, j)]
		if ok && direction != currentDirection {
			currentDirection = direction
			if direction == "right" {
				value++
			} else {
				value--
			}
		}
	}

	intersectionsUp = value != 0
	currentDirection = ""
	value = 0

	// Check down
	for k := i + 1; k < numberOfRows; k++ {
		direction, ok := horizontalTilesInloop[fmt.Sprintf("%d-%d", k, j)]
		if ok && direction != currentDirection {
			currentDirection = direction
			if direction == "right" {
				value++
			} else {
				value--
			}
		}
	}
	intersectionsDown = value != 0
	
	return intersectionsRight && intersectionsLeft && intersectionsUp && intersectionsDown
}

func main() {
	loopMap := []string{}
	startingPosition := []int{}
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	i := 0
	for scanner.Scan() {
		line := scanner.Text()
		for j, char := range line {
			if char == 'S' {
				startingPosition = []int{i, j}
			}
		}
		loopMap = append(loopMap, line)
		i++
	}

	// Iterate loop from starting position
	currentPosition := []int{startingPosition[0], startingPosition[1]}
	verticalTilesInloop := map[string]string{}
	horizontalTilesInloop := map[string]string{}
	currentDirection := "down"
	currentValue := 0
	for {
		fmt.Println(currentPosition)
		if currentValue > 0 && currentPosition[0] == startingPosition[0] && currentPosition[1] == startingPosition[1] {
			fmt.Println(currentValue)
			fmt.Println("Longest distance", currentValue/2)
			break
		}
		if currentDirection == "down" {
			currentPosition[0]++
		} else if currentDirection == "up" {
			currentPosition[0]--
		} else if currentDirection == "right" {
			currentPosition[1]++
		} else {
			currentPosition[1]--
		}
		currentTile := loopMap[currentPosition[0]][currentPosition[1]]
		if currentTile == '|' {
			verticalTilesInloop[fmt.Sprintf("%d-%d", currentPosition[0], currentPosition[1])] = currentDirection
		} else if currentTile == '-' {
			horizontalTilesInloop[fmt.Sprintf("%d-%d", currentPosition[0], currentPosition[1])] = currentDirection
		} else if currentTile == 'L' {
			if currentDirection == "down" {
				verticalTilesInloop[fmt.Sprintf("%d-%d", currentPosition[0], currentPosition[1])] = currentDirection
				currentDirection = "right"
				horizontalTilesInloop[fmt.Sprintf("%d-%d", currentPosition[0], currentPosition[1])] = currentDirection
			} else {
				horizontalTilesInloop[fmt.Sprintf("%d-%d", currentPosition[0], currentPosition[1])] = currentDirection
				currentDirection = "up"
				verticalTilesInloop[fmt.Sprintf("%d-%d", currentPosition[0], currentPosition[1])] = currentDirection
			}
		} else if currentTile == 'J' {
			if currentDirection == "down" {
				verticalTilesInloop[fmt.Sprintf("%d-%d", currentPosition[0], currentPosition[1])] = currentDirection
				currentDirection = "left"
				horizontalTilesInloop[fmt.Sprintf("%d-%d", currentPosition[0], currentPosition[1])] = currentDirection
			} else {
				horizontalTilesInloop[fmt.Sprintf("%d-%d", currentPosition[0], currentPosition[1])] = currentDirection
				currentDirection = "up"
				verticalTilesInloop[fmt.Sprintf("%d-%d", currentPosition[0], currentPosition[1])] = currentDirection
			}
		} else if currentTile == '7' {
			if currentDirection == "right" {
				horizontalTilesInloop[fmt.Sprintf("%d-%d", currentPosition[0], currentPosition[1])] = currentDirection
				currentDirection = "down"
				verticalTilesInloop[fmt.Sprintf("%d-%d", currentPosition[0], currentPosition[1])] = currentDirection
			} else {
				verticalTilesInloop[fmt.Sprintf("%d-%d", currentPosition[0], currentPosition[1])] = currentDirection
				currentDirection = "left"
				horizontalTilesInloop[fmt.Sprintf("%d-%d", currentPosition[0], currentPosition[1])] = currentDirection
			}
		} else if currentTile == 'F' {
			if currentDirection == "left" {
				horizontalTilesInloop[fmt.Sprintf("%d-%d", currentPosition[0], currentPosition[1])] = currentDirection
				currentDirection = "down"
				verticalTilesInloop[fmt.Sprintf("%d-%d", currentPosition[0], currentPosition[1])] = currentDirection
			} else {
				verticalTilesInloop[fmt.Sprintf("%d-%d", currentPosition[0], currentPosition[1])] = currentDirection
				currentDirection = "right"
				horizontalTilesInloop[fmt.Sprintf("%d-%d", currentPosition[0], currentPosition[1])] = currentDirection
			}
		}
		currentValue++
	}
	numberOfRows := len(loopMap)
	numberOfColumns := len(loopMap[0])
	tilesWithinLoop := 0
	for i := 0; i < numberOfRows; i++ {
		for j := 0; j < numberOfColumns; j++ {
			if tileContainedInLoop(i, j, numberOfRows, numberOfColumns, verticalTilesInloop, horizontalTilesInloop) {
				fmt.Println(i, j)
				tilesWithinLoop++
			}
		}
	}
	fmt.Println("Tiles within loop", tilesWithinLoop)
}

