function likes(names) {
    // TODO
    if (names.length == 0) {
      return "no one likes this"
    }
    else if (names.length == 1) {
        return `${names[0]} likes this`
    }
    else if (names.length <= 3) {
      message = ""
      for (let i = 0; i < names.length - 1; i++) {
        if (i + 1 < names.length - 1) {
            message += `${names[i]}, `
        }
        else{
            message += `${names[i]} and ${names[i + 1]} like this`
        }
      }
      return message
    }
    else{
        return `${names[0]}, ${names[1]} and ${names.length - 2} others like this`
    }
}

names = ["carlos", "gabriel", "silva", "machado"]
console.log(likes(names))