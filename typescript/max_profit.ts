function maxProfit(prices: number[]): number {
    let min = Number.MAX_VALUE;
    let result = 0;

    for (let i = 0; i < prices.length; i++) {
        if (min > prices[i]) min = prices[i];
        else if ((prices[i] - min) > result) result = prices[i] - min;
    }

    return result;
};


// Test
function testMaxProfit() {
    const testCases = [
        {prices: [7,1,5,3,6,4], expected: 5},
        {prices: [7,6,4,3,1], expected: 0},
    ];
    for (const testCase of testCases) {
        const {prices, expected} = testCase;
        const actual = maxProfit(prices);
        console.log(`For prices ${prices}, expected max profit to be ${expected}, got ${actual}`);
    }
}

testMaxProfit();
