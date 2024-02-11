function removeDuplicates_2(nums: number[]): number {
    let hashmap: { [key: string]: number } = {};
    let count = 0;

    for (let n of nums) {
        if (hashmap[n] === undefined) {
            hashmap[n] = 1;
            nums[count] = n;
            count++;
        } else if (hashmap[n] < 2) {
            nums[count] = n;
            count++;
            hashmap[n] = hashmap[n] + 1;
        }
    }

    nums.length = count;
    return count;
};

function testRemoveDuplicates_2() {
    let arrtest:number[] = [1, 1, 1, 2, 2, 3];
    console.log(arrtest);
    console.log(removeDuplicates_2(arrtest));
    console.log(arrtest);
}
