import { readFileSync } from "fs";

const stringNumbers = [
  "one",
  "two",
  "three",
  "four",
  "five",
  "six",
  "seven",
  "eight",
  "nine",
];

function findIntegers(line: string): number {
  // replace string values with numbers in the middle of the string
  for (const stringNumber of stringNumbers) {
    line = line.replaceAll(
      stringNumber,
      stringNumber[0] +
        (stringNumbers.indexOf(stringNumber) + 1).toString() +
        stringNumber[stringNumber.length - 1]
    );
  }
  const numbers = line.match(/\d/g);
  if (!numbers) {
    throw new Error("No numbers found");
  }
  const concatenatedValue = numbers[0] + numbers[numbers.length - 1];
  return parseInt(concatenatedValue);
}

function findAndAddIntegers(filePath: string): number {
  const fileContent = readFileSync(filePath, "utf-8");
  const lines = fileContent.split("\n");
  let sum = 0;
  for (const line of lines) {
    sum += findIntegers(line);
  }

  return sum;
}

const filePath = "input.txt";
const result = findAndAddIntegers(filePath);
console.log(result);
