bool isUgly(int n){
    // true if n's prime factors are only 2, 3, 5
    // we try the three factor by dividing until we cannot divide any further
    // if at the end, the value of n is 1, it means that its an ugly number,
    // otherwise it is not.
    
    if (n <= 0) {
        return false;
    }
    
    while (n % 2 == 0) {
        n /= 2;
    }
    
    while (n % 3 == 0) {
        n /= 3;
    }
    
    while (n % 5 == 0) {
        n /= 5;
    }
    
    return n == 1;
}