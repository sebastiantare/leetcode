function removeDuplicates(nums: number[]): number {
    let hashmap: { [key: string]: number } = {};
    let count = 0;

    for (let n of nums) {
        let nk = n.toString();

        if (hashmap[nk] === undefined) {
            hashmap[nk] = 1;
            nums[count] = n;
            count++;
        } else {
            hashmap[nk] = hashmap[nk] + 1;
        }
    }

    nums.length = count;
    return count;
};

function testRemoveDuplicates() {
    let arrtest:number[] = [1, 1, 1, 2, 2, 3];
    console.log(arrtest);
    console.log(removeDuplicates(arrtest));
    console.log(arrtest);
}

testRemoveDuplicates();
