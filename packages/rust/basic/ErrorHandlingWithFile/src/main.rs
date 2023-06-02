use std::fs::File;
use std::io::{ ErrorKind, Read };

fn read_from_file() -> Result<String, io::Error> {
    let mut s = String::new();
    // what is ? is immediatly return if Enum type: Error through From Func
    // From convert from Error type to Function Error Type
    // must using in return Result func
    File::open("example.txt")?.read_to_string(&mut s)?;
    Ok(s)
}
// or

fn read_from_file() -> Result<String, io::Error> {
    std::fs::read_to_string("example.txt")
}


// Why Can't it Compile?
fn main() {
    // if Result return value is Error(Enum), call Panic
    // Un Expected Error
    let f_1 = File::open("example.txt").unwrap();
    // same above but, control message
    let f_2 = File::open("example.txt").expect("File Open Error");
    // for match
    let f = File::open("example.txt");

    let f = match f {
        Ok(file) => file,
        Err(ref error) => match error.kind() {
            ErrorKind::NotFound => match File::create("example.txt") {
                Ok(fc) => fc,
                Err(e) => panic!("File not Created: {:?}", e)
            },
            other_error => panic!("Not Recoverable Error Panic!! : {:?}", other_error)
        },
    };
}
