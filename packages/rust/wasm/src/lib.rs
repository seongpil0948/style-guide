// import external library
extern crate wasm_bindgen;

use wasm_bindgen::prelude::*;

// [attribute]
#[wasm_bindgen]
// call extenal func
// attribute know how find it
extern {
    // js function
    pub fn alert(s: &str);
}

#[wasm_bindgen]
pub fn greet(name: &str) {
    alert(&format!("Hello, {}!", name));
}