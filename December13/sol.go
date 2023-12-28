package main

import (
	"fmt"
	"os"
	"bufio"
)

func exactlyOneDifferent(str1, str2 string) bool {
	different := false
	for i := 0; i < len(str1); i++ {
		if str1[i] != str2[i] {
			if different {
				return false
			}
			different = true
		}
	}
	return different
}

func findMirrorWithSmudge(board []string) int {
	for i := 0; i < len(board) - 1; i++ {
		oneDifferent := exactlyOneDifferent(board[i], board[i+1])
		isMirrorWithSmudge := board[i] == board[i+1] || oneDifferent
		if isMirrorWithSmudge {
			amountToCheck := i
			amountToCheckAfter := len(board) - i - 2
			if amountToCheckAfter < amountToCheck {
				amountToCheck = amountToCheckAfter
			}
			for j := 0; j < amountToCheck; j++ {
				if board[i-j-1] != board[i+j+2] {
					if exactlyOneDifferent(board[i-j-1], board[i+j+2]) {
						if oneDifferent {
							isMirrorWithSmudge = false
							break
						} else {
							oneDifferent = true
						}
					} else {
						isMirrorWithSmudge = false
						break
					}
				}
			}
			if isMirrorWithSmudge && oneDifferent{
				return i + 1
			}
		}
	}
	return -1
}

func findMirror(board []string) int {
	for i := 0; i < len(board) - 1; i++ {
		isMirror := board[i] == board[i+1]
		if isMirror {
			amountToCheck := i
			amountToCheckAfter := len(board) - i - 2
			if amountToCheckAfter < amountToCheck {
				amountToCheck = amountToCheckAfter
			}
			for j := 0; j < amountToCheck; j++ {
				if board[i-j-1] != board[i+j+2] {
					isMirror = false
					break
				}
			}
			if isMirror {
				return i + 1
			}
		}
	}
	return -1
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	rows := []string{}
	columns := []string{}
	sumOfMirrors := 0

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			rowMirror := findMirrorWithSmudge(rows)
			if rowMirror != -1 {
				fmt.Println("row mirror", rowMirror)
				sumOfMirrors += rowMirror * 100
			} else {
				columnMirror := findMirrorWithSmudge(columns)
				fmt.Println("column mirror", columnMirror)
				sumOfMirrors += columnMirror
			}
			rows = []string{}
			columns = []string{}
			continue
		}
		rows = append(rows, line)
		if len(columns) == 0 {
			for i := 0; i < len(line); i++ {
				columns = append(columns, "")
			}
		}
		for i := 0; i < len(line); i++ {
			columns[i] += string(line[i])
		}
	}
	if len(rows) > 0 {
		rowMirror := findMirrorWithSmudge(rows)
		if rowMirror != -1 {
			fmt.Println("row mirror", rowMirror)
			sumOfMirrors += rowMirror * 100
		} else {
			columnMirror := findMirrorWithSmudge(columns)
			fmt.Println("column mirror", columnMirror)
			sumOfMirrors += columnMirror
		}
	}
	fmt.Println(sumOfMirrors)
}

