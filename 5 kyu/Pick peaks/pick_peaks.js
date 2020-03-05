


function pickPeaks(arr) {
    return arr.reduce(
        (prev, cur, index) => {
            if (cur > arr[index - 1] && cur > arr.slice(index).find(el => el !== cur)) {
                prev.pos.push(index), prev.peaks.push(cur);
            }
            return prev;
        },
        { pos: [], peaks: [] }
    );
}


console.log(pickPeaks([1,2,3,4,4,4,3,3,2,5,2]))
