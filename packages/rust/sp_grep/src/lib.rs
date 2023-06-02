//! # My Crate
//! * 일부 연산을 더 쉽게 실행하기 위한 유틸리티 모음
use std::error::Error;
/// 주어진 숫자에 1을 더한다.
//ㄴ
use std::fs;


pub struct Config {
    query: String,
    filename: String,
}

impl Config {
    /// cloning is more Inefficient than  save Reference data
    /// because, arg's OW not parse config
    /// but, LT manage is more easy
    /// ```
    /// let query = args[1].clone();
    /// let filename = args[2].clone();
    /// ```    
    /// ` = LT variable
    ///   static = LT is until the end of program
    pub fn new(mut args: std::env::Args) -> Result<Config, &'static str> {
        args.next(); // args[0] is bin file name

        let query = match args.next() {
            Some(arg) => arg,
            None => return Err(" Args is not at all "),
        };

        let filename = match args.next() {
            Some(arg) => arg,
            None => return Err(" Insufficient(불만족) Num Of Arg"),
        };
        Ok(Config { query, filename })
    }
}

/*
    1. Box(dyn Error) from Error Trait>
        Return Various Error at Unexpected
    2. ? operator return Error instead panic from expect(func)

*/
pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.filename)?;

    for line in search(&config.query, &contents) {
        println!("Matching \n Result: {}", line)
    }

    Ok(())
}

// configure as $ cargo test
#[cfg(test)]
mod test {
    use super::*; // import from ../(super)

    #[test]
    fn one_result() {
        let query = "good";
        let contents = "\
        Rust is Good.. ><
        hahaha    
        ";

        assert_eq!(vec!["Rust is Good.. ><"], search(query, contents));
    }
}

// 'a : LT variable
// contents is must connect return LT
// contents 는 빌려온 데이터다. 그리고 수명이 이후로도 지속되어야 한다.
pub fn search<'a>(query: &str, contents: &'a str) -> Vec<&'a str> {
    // to_lowercase is create new String
    // shadowing and query become String(heap)(Clone) not str(string slice)
    // but contains accept only str
    let query = query;
    // iter by each line
    contents
        .lines() // return iterator
        .filter(|line| line.contains(query))
        .collect() // Re assembly (재조립 Array)
}
