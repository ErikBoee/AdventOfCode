package main

import (
	"fmt"
	"os"
	"bufio"
	"math"
	"regexp"
	"strconv"
	"strings"
)

type Race struct {
	time float64
	distance float64
}


func getLimitsDiff(race Race) (int){
	upperLimit := math.Floor((race.time + math.Sqrt(math.Pow(race.time,2) - 4*race.distance)) / 2)
	lowerLimit := math.Ceil((race.time - math.Sqrt(math.Pow(race.time,2) - 4*race.distance)) / 2)
	return int(upperLimit) - int(lowerLimit) + 1
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	times := []float64{}
	distances := []float64{}
	k := 0
	for scanner.Scan() {
		line := scanner.Text()
		re := regexp.MustCompile(`\d+`)
		// Find all matches in the line
		matches := re.FindAllString(line, -1)
		match := strings.Join(matches, "")
		intVal, _ := strconv.Atoi(match)
		if k == 0 {
			times = append(times, float64(intVal))
		} else {
			distances = append(distances, float64(intVal))
		}
		k++
	}
	totalDiff := 1
	for i := 0; i < len(times); i++ {
		totalDiff *= getLimitsDiff(Race{times[i], distances[i]})
	}
	fmt.Println(totalDiff)
}