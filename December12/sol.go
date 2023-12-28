package main

import (
	"fmt"
	"os"
	"bufio"
	"strings"
	"strconv"
)

var cache = map[string]int{}

func sum(numbers []int) int {
	sum := 0
	for _, number := range numbers {
		sum += number
	}
	return sum
}

func possibleGroupPlacementsBaseCase(field string, number int) int {
	placements := 0
	for i := 0; i < len(field) - (number-1); i++ {
		approved := true
		for j:= 0; j < len(field); j++ {
			if j >= i && j < i + number{
				if string(field[j]) == "." {
					approved = false
				}
			} else if string(field[j]) == "#" {
				approved = false
			}
		}
		if approved {
			placements++
		}
	}
	return placements
}

func possibleGroupPlacements(field string, numbers []int) int {
	cacheKey := fmt.Sprintf("%s-%v", field, numbers)
	if cacheValue, ok := cache[cacheKey]; ok {
		return cacheValue
	}
	if len(numbers) == 1 {
		return possibleGroupPlacementsBaseCase(field, numbers[0])
	}
	placements := 0
	for i := 0; i < len(field) - (sum(numbers)+len(numbers[1:]) - 1); i++ {
		approved := true
		for j := 0; j < i + numbers[0]; j++ {
			if j < i {
				if string(field[j]) == "#" {
				approved = false
				}
			} else if (string(field[j]) == ".") {
				approved = false
			}
		}
		if i + numbers[0] < len(field) && string(field[i + numbers[0]]) == "#" {
			approved = false
		}
		if approved {
			placements += possibleGroupPlacements(field[i + numbers[0] + 1:], numbers[1:])
		}
	}
	cache[cacheKey] = placements
	return placements
}


func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	sumOfPossibilities := 0
	k := 0
	for scanner.Scan() {
		line := scanner.Text()
		field := strings.Split(line, " ")[0]
		numbersString := strings.Split(line, " ")[1]
		numbers := strings.Split(numbersString, ",")
		numbersInt := []int{}
		for _, number := range numbers {
			numberInt, _ := strconv.Atoi(number)
			numbersInt = append(numbersInt, numberInt)
		}
		expandedNumbersInt := []int{}
		expandedField := field
		for i := 0; i < 5; i++ {
			expandedNumbersInt = append(expandedNumbersInt, numbersInt...)
			if i != 4 {
				expandedField += "?"
				expandedField += field
			}
		}

		pGPL := possibleGroupPlacements(expandedField, expandedNumbersInt)
		fmt.Println(k, pGPL)
		k++
		sumOfPossibilities += pGPL
	}
	fmt.Println(sumOfPossibilities)
}

