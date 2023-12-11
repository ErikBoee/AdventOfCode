const fs = require("fs");

const filePath = "input.txt";

const lines = fs.readFileSync(filePath, "utf-8").split("\n");

let approvedGames = 0;
let powerSum = 0;
let i = 1;
for (const line of lines) {
  const redMatches = line.match(/\d+\sred/g);
  const blueMatches = line.match(/\d+\sblue/g);
  const greenMatches = line.match(/\d+\sgreen/g);
  approvedGame = true;
  let maxRedValue = 0;
  let maxBlueValue = 0;
  let maxGreenValue = 0;

  for (const match of redMatches) {
    const redValue = parseInt(match.split(" ")[0]);
    if (redValue > 12) {
      approvedGame = false;
    }
    if (redValue > maxRedValue) {
      maxRedValue = redValue;
    }
  }
  for (const match of blueMatches) {
    const blueValue = parseInt(match.split(" ")[0]);
    if (blueValue > 14) {
      approvedGame = false;
    }
    if (blueValue > maxBlueValue) {
      maxBlueValue = blueValue;
    }
  }
  for (const match of greenMatches) {
    const greenValue = parseInt(match.split(" ")[0]);
    if (greenValue > 13) {
      approvedGame = false;
    }
    if (greenValue > maxGreenValue) {
      maxGreenValue = greenValue;
    }
  }
  const power = maxRedValue * maxBlueValue * maxGreenValue;
  powerSum += power;
  if (approvedGame) {
    approvedGames += i;
  }
  i++;
}

console.log(approvedGames);
console.log(powerSum);
