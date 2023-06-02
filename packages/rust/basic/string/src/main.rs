fn main() {
    // ## distingush  between String and str slice 
    let mut a: String = String::from("나는 도비에요 ㅎㅎ");
    let b: &str = "^_^";
    a.push_str(b);
    let c: char = '@'; // use '
    a.push(c);

    let one: &str = "나는 성필이에요";
    let two: String = one.to_string();

    // Indexing
    for c in a.chars() {
        println!("{}", c)
    }

    for b in two.bytes() {
        println!("{}", b)
    }
    
}
