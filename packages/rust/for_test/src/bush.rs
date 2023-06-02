use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

fn main() {
    // f: 102, .
    let mut input_line = String::new(); io::stdin().read_line(&mut input_line).unwrap();
    let n = parse_input!(input_line, i32);
    let fires = vec!["fff", "ff", "f"];

    let mut result: Vec<i32> = Vec::new();
    for _i in 0..n as usize {
        let mut input_line = String::new(); io::stdin().read_line(&mut input_line).unwrap();
        let mut line = input_line.trim_matches('\n').to_string();
        let mut count = 0;

        eprintln!("line before = {} count: {}",line, count);
        for fire in fires.iter() {
            while line.contains(fire) {
                count += 1;
                line = line.replacen(fire, ".", 1)
            }    
        }
        eprintln!("line after = {} count: {}",line, count);
        result.push(count);
    }
    for i in 0..n as usize {
        println!("{}", result[i]);
    }
}
