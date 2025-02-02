"use strict";

function solution(numbers, hand) {
    return new Solution().solution(numbers, hand);
}
class Pair {
    constructor(x, y) {
        this.distanceTo = (num) => {
            const x = num == 0 ? 1 : (num - 1) % 3;
            const y = num == 0 ? 3 : Math.floor((num - 1) / 3);
            return Math.abs(x - this.x) + Math.abs(y - this.y);
        };
        this.x = x;
        this.y = y;
    }
    setNumber(num) {
        this.x = num == 0 ? 1 : (num - 1) % 3;
        this.y = num == 0 ? 3 : Math.floor((num - 1) / 3);
    }
}
class Solution {
    constructor() {
        this.leftHand = new Pair(0, 3);
        this.rightHand = new Pair(2, 3);
        this.answer = "";
        this.leftNum = [1, 4, 7];
        this.rightNum = [3, 6, 9];
        this.solution = (numbers, hand) => {
            for (const num of numbers) {
                if (this.leftNum.includes(num))
                    this.appendAnswer_Left(num);
                else if (this.rightNum.includes(num))
                    this.appendAnswer_Right(num);
                else {
                    const leftDistance = this.leftHand.distanceTo(num);
                    const rightDistance = this.rightHand.distanceTo(num);
                    if (leftDistance > rightDistance)
                        this.appendAnswer_Right(num);
                    else if (leftDistance < rightDistance)
                        this.appendAnswer_Left(num);
                    else {
                        if (hand === "left")
                            this.appendAnswer_Left(num);
                        else if (hand === "right")
                            this.appendAnswer_Right(num);
                    }
                }
            }
            return this.answer;
        };
        this.appendAnswer_Right = (num) => {
            this.rightHand.setNumber(num);
            this.answer += "R";
        };
        this.appendAnswer_Left = (num) => {
            this.leftHand.setNumber(num);
            this.answer += "L";
        };
    }
}