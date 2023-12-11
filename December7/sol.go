package main

import (
	"fmt"
	"os"
	"bufio"
	"strings"
	"strconv"
	"sort"
)

type PokerHand struct {
	cards string
	score int
}

var cardStringToInt = map[string]int{
	"2": 2,
	"3": 3,
	"4": 4,
	"5": 5,
	"6": 6,
	"7": 7,
	"8": 8,
	"9": 9,
	"T": 10,
	"J": 1,
	"Q": 12,
	"K": 13,
	"A": 14,
}

func sortPokerHands(pokerHands []PokerHand){
	sort.Slice(pokerHands, func(j, i int) bool {
		if pokerHands[i].cards[0] != pokerHands[j].cards[0] {
			return cardStringToInt[string(pokerHands[i].cards[0])] > cardStringToInt[string(pokerHands[j].cards[0])]
		} else if pokerHands[i].cards[1] != pokerHands[j].cards[1] {
			return cardStringToInt[string(pokerHands[i].cards[1])] > cardStringToInt[string(pokerHands[j].cards[1])]
		} else if pokerHands[i].cards[2] != pokerHands[j].cards[2] {
			return cardStringToInt[string(pokerHands[i].cards[2])] > cardStringToInt[string(pokerHands[j].cards[2])]
		} else if pokerHands[i].cards[3] != pokerHands[j].cards[3] {
			return cardStringToInt[string(pokerHands[i].cards[3])] > cardStringToInt[string(pokerHands[j].cards[3])]
		} else {
			return cardStringToInt[string(pokerHands[i].cards[4])] > cardStringToInt[string(pokerHands[j].cards[4])]
		}
	})
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	pokerHandsFiveAlike := []PokerHand{}
	pokerHandsFourAlike := []PokerHand{}
	pokerHandsTwoPairs := []PokerHand{}
	pokerHandsThreeAlike := []PokerHand{}
	pokerHandsFullHouse := []PokerHand{}
	pokerHandsTwoAlike := []PokerHand{}
	pokerHandsOneAlike := []PokerHand{}
	for scanner.Scan() {
		line := scanner.Text()
		pokerHand := strings.Split(line, " ")[0]
		pokerHandScore, _ := strconv.Atoi(strings.Split(line, " ")[1])

		pokerHandMap := make(map[string]int)
		for i := 0; i < len(pokerHand); i++ {
			_, ok := pokerHandMap[string(pokerHand[i])]
			if !ok {
				pokerHandMap[string(pokerHand[i])] = 1
			} else {
				pokerHandMap[string(pokerHand[i])]++
			}
		}
		maxVal := 0
		secondMaxVal := 0
		for _, val := range pokerHandMap {
			if val > maxVal {
				secondMaxVal = maxVal
				maxVal = val
			} else if val > secondMaxVal {
				secondMaxVal = val
			}
		}

		jokers, haveJokers := pokerHandMap["J"]
		if maxVal == 5 {
			pokerHandsFiveAlike = append(pokerHandsFiveAlike, PokerHand{pokerHand, pokerHandScore})
		} else if maxVal == 4 {
			if haveJokers {
				pokerHandsFiveAlike = append(pokerHandsFiveAlike, PokerHand{pokerHand, pokerHandScore})
			} else {
				pokerHandsFourAlike = append(pokerHandsFourAlike, PokerHand{pokerHand, pokerHandScore})
			}
		} else if maxVal == 3 {
			if secondMaxVal == 2 {
				if haveJokers {
					pokerHandsFiveAlike = append(pokerHandsFiveAlike, PokerHand{pokerHand, pokerHandScore})
				} else {
					pokerHandsFullHouse = append(pokerHandsFullHouse, PokerHand{pokerHand, pokerHandScore})
				}
			} else {
				if haveJokers {
					pokerHandsFourAlike = append(pokerHandsFourAlike, PokerHand{pokerHand, pokerHandScore})
				} else {

					pokerHandsThreeAlike = append(pokerHandsThreeAlike, PokerHand{pokerHand, pokerHandScore})
				}
			}
		} else if maxVal == 2 {
			if secondMaxVal == 2 {
				if haveJokers {
					if jokers == 2 {
						pokerHandsFourAlike = append(pokerHandsFourAlike, PokerHand{pokerHand, pokerHandScore})
					} else {
						pokerHandsFullHouse = append(pokerHandsFullHouse, PokerHand{pokerHand, pokerHandScore})
					}
				} else {
				pokerHandsTwoPairs = append(pokerHandsTwoPairs, PokerHand{pokerHand, pokerHandScore})
				}
			} else {
				if haveJokers {
					pokerHandsThreeAlike = append(pokerHandsThreeAlike, PokerHand{pokerHand, pokerHandScore})
				} else {
					pokerHandsTwoAlike = append(pokerHandsTwoAlike, PokerHand{pokerHand, pokerHandScore})
				}
			}
		} else {
			if haveJokers {
				pokerHandsTwoAlike = append(pokerHandsTwoAlike, PokerHand{pokerHand, pokerHandScore})
			} else {
				pokerHandsOneAlike = append(pokerHandsOneAlike, PokerHand{pokerHand, pokerHandScore})
			}
		}
	}

	sortPokerHands(pokerHandsFiveAlike)
	sortPokerHands(pokerHandsFourAlike)
	sortPokerHands(pokerHandsFullHouse)
	sortPokerHands(pokerHandsThreeAlike)
	sortPokerHands(pokerHandsTwoPairs)
	sortPokerHands(pokerHandsTwoAlike)
	sortPokerHands(pokerHandsOneAlike)

	sortedPokerHands := []PokerHand{}
	sortedPokerHands = append(sortedPokerHands, pokerHandsOneAlike...)
	sortedPokerHands = append(sortedPokerHands, pokerHandsTwoAlike...)
	sortedPokerHands = append(sortedPokerHands, pokerHandsTwoPairs...)
	sortedPokerHands = append(sortedPokerHands, pokerHandsThreeAlike...)
	sortedPokerHands = append(sortedPokerHands, pokerHandsFullHouse...)
	sortedPokerHands = append(sortedPokerHands, pokerHandsFourAlike...)
	sortedPokerHands = append(sortedPokerHands, pokerHandsFiveAlike...)


	for i := 0; i < len(sortedPokerHands); i++ {
		fmt.Println(sortedPokerHands[i].cards)
	}

	sumOfScoreProduct := 0
	for i := 0; i < len(sortedPokerHands); i++ {
		sumOfScoreProduct += sortedPokerHands[i].score * (i+1)
	}
	fmt.Println(sumOfScoreProduct)

}