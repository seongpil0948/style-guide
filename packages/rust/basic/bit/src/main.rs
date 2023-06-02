/// https://m.blog.naver.com/PostView.nhn?blogId=mayu-story&logNo=220500544894&proxyReferer=https:%2F%2Fwww.google.com%2F
/// https://jhnyang.tistory.com/162
fn main() {
    let a:u8 = 100;
    let b:u8 = 103;
    // 1100100 1100111
    println!("{:b} {:b}", a, b);
    // 1 = 10
    // 1100101 1100110
    // XOR
    println!("{:b} {:b}", a ^ 1, b ^ 1);
    // 101 100
    println!("{} {}", a ^ 1, b ^ 1);

    
    // a /= 2; //25 / 2 = 12 not 12.5
    // a %= 5; //12 % 5 = 2
    
    // a &= 2; //10 && 10 -> 10 -> 2
    // a |= 5; //010 || 101 -> 111 -> 7
    // a ^= 2; //111 != 010 -> 101 -> 5
    // a <<= 1; //'101'+'0' -> 1010 -> 10
    // a >>= 2; //101̶0̶ -> 10 -> 2
}
