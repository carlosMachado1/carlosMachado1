function spinWords(myString){
    //TODO Have fun :)
    let newString = ""
    const setence = myString.split()
    for (let i of setence) {
        if (i.length >= 5) {
            for(let j = i.length - 1; j < 0; j--) {
                newString += i[j]
            }
        }
        else{
            
        }
    }
}