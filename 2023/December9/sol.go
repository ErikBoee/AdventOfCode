package main

import (
	"fmt"
	"os"
	"bufio"
	"strings"
	"strconv"
)

func allElementsZero(numbers []int) bool {
	for _, number := range numbers {
		if number != 0 {
			return false
		}
	}
	return true
}

func addLastNumbersOflists(numbersIntListFirst []int, numbersIntListSecond []int) int {
	newValue := numbersIntListFirst[len(numbersIntListFirst) - 1] + numbersIntListSecond[len(numbersIntListSecond) - 1]
	return newValue
}

func subtractFirstNumbersOflists(numbersIntListFirst []int, numbersIntListSecond []int) int {
	newValue := numbersIntListFirst[0] - numbersIntListSecond[0]
	return newValue
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	rightSum := 0
	leftSum := 0
	for scanner.Scan() {
		line := scanner.Text()
		numbers := strings.Split(line, " ")
		numbersIntLists := [][]int{}
		currentNumbersInt := make([]int, len(numbers))
		for i := 0; i < len(numbers); i++ {
			currentNumbersInt[i], _ = strconv.Atoi(numbers[i])
		}
		numbersIntLists = append(numbersIntLists, currentNumbersInt)
		for !allElementsZero(currentNumbersInt){
			newNumbersInt := make([]int, len(currentNumbersInt) - 1)
			for i := 0; i < len(currentNumbersInt) - 1; i++ {
				newNumbersInt[i] = currentNumbersInt[i + 1] - currentNumbersInt[i]
			}
			numbersIntLists = append(numbersIntLists, newNumbersInt)
			currentNumbersInt = newNumbersInt
		}
		for i := len(numbersIntLists) - 2; i > -1; i--{
			numbersIntLists[i] = append(numbersIntLists[i], addLastNumbersOflists(numbersIntLists[i], numbersIntLists[i + 1]))
			numbersIntLists[i] = append([]int{subtractFirstNumbersOflists(numbersIntLists[i], numbersIntLists[i + 1])}, numbersIntLists[i]...)
		}
		rightSum += numbersIntLists[0][len(numbersIntLists[0]) - 1]
		leftSum += numbersIntLists[0][0]
	}
	fmt.Println(rightSum)
	fmt.Println(leftSum)

	
}

