

function solution(X, Y, D) {

    if (X == D && X == 1 && X != Y) return Y-1    
    if (X == Y) return 0
    
    let temp_length = (Y-X)/D;
    if (temp_length == Math.trunc(temp_length)) return temp_length    
    else return Math.trunc(temp_length)+1   
    
    
    // while(X >= Y) {
    //     X=X+D;
    //     counter++;
    // }
}

