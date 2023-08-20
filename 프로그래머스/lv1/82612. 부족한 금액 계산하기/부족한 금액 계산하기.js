function solution(price, money, count) {
    var answer = 0;
    let m = 0;
    
    for(let i = 1; i <= count; i++){
        m += price * i;
    }
    
    if(money - m < 0) {
        return Math.abs(money - m)
    }
    

    return answer;
}