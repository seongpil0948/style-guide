/// Algorithm crate
/// Played the role is called Module Tree Root
/// use extern crate algorithm;
pub mod collections;


// macros3.rs
// Make me compile, without taking the macro out of the module!
// Execute `rustlings hint macros3` for hints :)

// I AM NOT DONE
#[macro_use]
mod macros {
    macro_rules! my_macro {
        () => {
            println!("Check out my macro!");
        };
    }
}

fn main() {
    my_macro!();
}
