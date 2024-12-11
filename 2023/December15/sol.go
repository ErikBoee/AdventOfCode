package main

import (
	"fmt"
	"os"
	"bufio"
	"strings"
	"strconv"
)

func removeKeyWithLabel(lenses []string, label string) []string {
	newLenses := []string{}
	for _, lens := range lenses {
		currentLabel, _ := getLabelAndOperation(lens)
		if currentLabel != label {
			newLenses = append(newLenses, lens)
		}
	}
	return newLenses
}

func addOrReplaceKeyWithLabel(lenses []string, label, newLens string) []string {
	for i, lens := range lenses {
		currentLabel, _ := getLabelAndOperation(lens)
		if currentLabel == label {
			lenses[i] = newLens
			return lenses
		}
	}
	return append(lenses, newLens)
}

func getLabelAndOperation(lens string) (string, string) {
	label := ""
	operation := ""
	if len(strings.Split(lens, "-")) > 1 {
		label = strings.Split(lens, "-")[0]
		operation = "-"
	} else {
		label = strings.Split(lens, "=")[0]
		operation = "="
	}
	return label, operation
}

func main() {
	boxes := make([][]string, 256)
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Scan();
	firstLine := scanner.Text()
	groups := strings.Split(firstLine, ",")
	totalValue := 0
	for _, group := range groups {
		initialValue := 0
		for _, char := range group {
			ascii := int(char)
			initialValue += ascii
			initialValue *= 17
			initialValue %= 256
		}
		totalValue += initialValue
	}
	fmt.Println(totalValue)

	for _, lens := range groups {
		boxKey := 0
		label, operation := getLabelAndOperation(lens)
		for _, char := range label {
			ascii := int(char)
			boxKey += ascii
			boxKey *= 17
			boxKey %= 256
		}
		if boxes[boxKey] == nil {
			boxes[boxKey] = []string{}
		}
		if operation == "-" {
			boxes[boxKey] = removeKeyWithLabel(boxes[boxKey], label)
		} else {
			boxes[boxKey] = addOrReplaceKeyWithLabel(boxes[boxKey], label, lens)
		}
	}

	totalValueBoxes := 0
	for i, box := range boxes {
		for j, lens := range box {
			intVal ,_ := strconv.Atoi(lens[len(lens)-1:])
			value := (i+1) * (j+1) * intVal
			totalValueBoxes += value
		}
	}
	fmt.Println(totalValueBoxes)

}
