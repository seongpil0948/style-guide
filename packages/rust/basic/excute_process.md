1. Program Compile from Rust Compiler
    - $ __cargo build__ _if you make package from $ __cargo new {package_name}__
    - $ __rustc main.rs__
    
    - _rust is ahead-of-time(미리) Compile Language <br>
        if you deliver the binary file create by the above to someone,<br>
        the recipient can run without Rust_
    - cargo.lock <br>
    package dependency freeze

    

2. $ __target/debug/from_cargo__(binary) or $ __cargo run__ 
    - rebuild if you adjust file
    - just binary excute if you any adjusted
    - $ __cargo check__ is just check whether Compile


3. if you ready to release project $ __cargo build --release__
    - file create path to  __target/release__ 
