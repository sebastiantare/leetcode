function majorityElement(nums: number[]): number {
    let hashmap: { [key: string]: number } = {};

    let mid:number = Math.round(nums.length / 2);

    for (let n of nums) {
        if (hashmap[n] === undefined) {
            hashmap[n] = 1;
        } else {
            hashmap[n] = hashmap[n] + 1;
            if (hashmap[n] >= mid) return n;
        }
    }

    return -1;
};

function testMajorityElement() {
    let arrtest:number[] = [2,2,1,1,1,2,2];
    console.log(arrtest);
    console.log(majorityElement(arrtest));
    console.log(arrtest);
}

testMajorityElement();
