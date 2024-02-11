function romanToInt(s: string): number {
    const symbols = new Map();
    symbols.set('I', 1);
    symbols.set('V', 5);
    symbols.set('X', 10);
    symbols.set('L', 50);
    symbols.set('C', 100);
    symbols.set('D', 500);
    symbols.set('M', 1000);

    let result = 0;

    for (let i = 0; i < s.length; i++) {
        if (i < s.length - 1 && s[i] === 'I' && (s[i + 1] === 'V' || s[i + 1] === 'X')) result -= symbols.get(s[i]);
        else if (i < s.length - 1 && s[i] === 'X' && (s[i + 1] === 'L' || s[i + 1] === 'C')) result -= symbols.get(s[i]);
        else if (i < s.length - 1 && s[i] === 'C' && (s[i + 1] === 'D' || s[i + 1] === 'M')) result -= symbols.get(s[i]);
        else result += symbols.get(s[i]);
    }

    return result;
};

console.log(romanToInt('XIV'));
