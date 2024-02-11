function removeElement(nums: number[], val: number): number {
    let count = 0;
    for (let n of nums) {
        if (n !== val) {
            nums[count] = n;
            count++;
        }
    }
    nums.length = count;
    return count;
};

function testRemoveElement() {
    let arrtest:number[] = [3,2,2,3];
    console.log(arrtest);
    console.log(removeElement(arrtest, 3));
    console.log(arrtest);
}

testRemoveElement();
