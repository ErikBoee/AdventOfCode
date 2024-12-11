package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func extractSeeds(line string) []int {
	// Split line on space
	seedsString := strings.Split(line, "seeds:")[1]
	seedValues := strings.Split(seedsString, " ")
	
	// Get seeds
	seeds := []int{}
	cleanedSeedValues := []string{}
	for _, sV := range seedValues {
		if sV != "" {
			cleanedSeedValues = append(cleanedSeedValues, sV)
		}
	}

	amountOfSeeds := 0
	for i, _ := range cleanedSeedValues {
		if (i % 2 == 0) {
			amount, _ := strconv.Atoi(cleanedSeedValues[i + 1])
			amountOfSeeds += amount
		}
	}

	seeds = make([]int, amountOfSeeds)
	fmt.Println("Amount of seeds:", amountOfSeeds)
	k:=0
	for i, _ := range cleanedSeedValues {
		if (i % 2 == 1) {
			continue
		}
		startSeed, _ := strconv.Atoi(cleanedSeedValues[i])
		rangeForSeeds, _ := strconv.Atoi(cleanedSeedValues[i + 1])
		for j := 0; j < rangeForSeeds; j++ {
			seeds[k] = startSeed + j
			k++
		}
		fmt.Println("Seeds extracted", i)
	}
	return seeds
}

func populateMap(line string, m map[int]int, sourceValues []int) (map[int]int) {
	startingWithEmptyMap := len(m) == 0
	sourceToDestinationStrings := strings.Split(line, " ")
	if !(len(sourceToDestinationStrings) >= 3) {
		return m
	}
	destinationIndex, _ := strconv.Atoi(sourceToDestinationStrings[0])
	sourceIndex, _ := strconv.Atoi(sourceToDestinationStrings[1])
	rangeForIndices, _ := strconv.Atoi(sourceToDestinationStrings[2])

	for _, value := range sourceValues {
		if value >= sourceIndex && value < sourceIndex + rangeForIndices {
			m[value] = value + destinationIndex - sourceIndex
		} else if startingWithEmptyMap{
			m[value] = value
		}
	}
	return m
}

func minLocationForSeeds(seeds []int, lines []string) int {
	isPopulatingSeedToSoilMap := false
	isPopulatingSoilToFertilizerMap := false
	isPopulatingFertilizerToWaterMap := false
	isPopulatingWaterToLightMap := false
	isPopulatingLightToTemperatureMap := false
	isPopulatingTemperatureToHumidityMap := false
	isPopulatingHumidityToLocationMap := false

	seed_to_soil_map := make(map[int]int)
	soil_to_fertilizer_map := make(map[int]int)
	fertilizer_to_water_map := make(map[int]int)
	water_to_light_map := make(map[int]int)
	light_to_temperature_map := make(map[int]int)
	temperature_to_humidity_map := make(map[int]int)
	humidity_to_location_map := make(map[int]int)

	for i, line := range lines {
		if i == 0 {
			continue
		}
		// If line contains seeds: split line and use rest of line splitted on space as seeds
		if (strings.Contains(line, "seed-to-soil map:")) {
			isPopulatingSeedToSoilMap = true
		} else if (strings.Contains(line, "soil-to-fertilizer map:")) {
			isPopulatingSoilToFertilizerMap = true
		} else if (strings.Contains(line, "fertilizer-to-water map:")) {
			isPopulatingFertilizerToWaterMap = true
		} else if (strings.Contains(line, "water-to-light map:")) {
			isPopulatingWaterToLightMap = true
		} else if (strings.Contains(line, "light-to-temperature map:")) {
			isPopulatingLightToTemperatureMap = true
		} else if (strings.Contains(line, "temperature-to-humidity map:")) {
			isPopulatingTemperatureToHumidityMap = true
		} else if (strings.Contains(line, "humidity-to-location map:")) {
			isPopulatingHumidityToLocationMap = true
		} else if (isPopulatingHumidityToLocationMap){
			humidities := make([]int, len(seeds))
			for i, seed := range seeds {
				humidities[i] = temperature_to_humidity_map[light_to_temperature_map[water_to_light_map[fertilizer_to_water_map[soil_to_fertilizer_map[seed_to_soil_map[seed]]]]]]
			}
			humidity_to_location_map = populateMap(line, humidity_to_location_map, humidities)
		} else if (isPopulatingTemperatureToHumidityMap){
			temperatures := make([]int, len(seeds))
			for i, seed := range seeds {
				temperatures[i] = light_to_temperature_map[water_to_light_map[fertilizer_to_water_map[soil_to_fertilizer_map[seed_to_soil_map[seed]]]]]
			}
			temperature_to_humidity_map = populateMap(line, temperature_to_humidity_map, temperatures)
		} else if (isPopulatingLightToTemperatureMap){
			lights := make([]int, len(seeds))
			for i, seed := range seeds {
				lights[i] = water_to_light_map[fertilizer_to_water_map[soil_to_fertilizer_map[seed_to_soil_map[seed]]]]
			}
			light_to_temperature_map = populateMap(line, light_to_temperature_map, lights)
		} else if (isPopulatingWaterToLightMap){
			waters := make([]int, len(seeds))
			for i, seed := range seeds {
				waters[i] = fertilizer_to_water_map[soil_to_fertilizer_map[seed_to_soil_map[seed]]]
			}
			water_to_light_map = populateMap(line, water_to_light_map, waters)
		} else if (isPopulatingFertilizerToWaterMap){
			fertilizers := make([]int, len(seeds))
			for i, seed := range seeds {
				fertilizers[i] = soil_to_fertilizer_map[seed_to_soil_map[seed]]
			}
			fertilizer_to_water_map = populateMap(line, fertilizer_to_water_map, fertilizers)
		} else if (isPopulatingSoilToFertilizerMap){
			soils := make([]int, len(seeds))
			for i, seed := range seeds {
				soils[i] = seed_to_soil_map[seed]
			}
			soil_to_fertilizer_map = populateMap(line, soil_to_fertilizer_map, soils)
		} else if (isPopulatingSeedToSoilMap){
			seed_to_soil_map = populateMap(line, seed_to_soil_map, seeds)
		}
	}

	locations := []int{}
	for _, seed := range seeds {
		soil := seed_to_soil_map[seed]
		fertilizer := soil_to_fertilizer_map[soil]
		water := fertilizer_to_water_map[fertilizer]
		light := water_to_light_map[water]
		temperature := light_to_temperature_map[light]
		humidity := temperature_to_humidity_map[temperature]
		location := humidity_to_location_map[humidity]
		locations = append(locations, location)
	}
	minLocation := locations[0]
	for _, location := range locations {
		if location < minLocation {
			minLocation = location
		}
	}
	return minLocation
}

func main() {
	seeds := []int{}

	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	lines := []string{}
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	seeds = extractSeeds(lines[0])
	minLocation := minLocationForSeeds(seeds[0:1], lines)
	rangeForSeeds := len(seeds) / 10000
	fmt.Println("Range for seeds:", rangeForSeeds)
	fmt.Println("MinLocation", minLocation)
	k := 0
	for j := 1; j < len(seeds);{
		k++;
		currentMinLocation := minLocationForSeeds(seeds[j:j+rangeForSeeds], lines)
		if j + rangeForSeeds > len(seeds) {
			rangeForSeeds = len(seeds) - j
		}
		j += rangeForSeeds
		if currentMinLocation < minLocation {
			minLocation = currentMinLocation
		}
		fmt.Printf("Progress: %d/%d \n", k, 10000)
		fmt.Println("MinLocation", minLocation)
		fmt.Println("currentMinLocation", currentMinLocation)
	}
	fmt.Println("Min location:", minLocation)
}
