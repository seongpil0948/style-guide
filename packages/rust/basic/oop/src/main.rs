
/// ## rust is not use Inheritance
/// * inheritance Code wasted too much
/// 
/// ## bounded parametric polymophism
/// * Rust instead uses generics to abstract compatible types <br>
///     and uses trait bounds to impose(부과하다) constraints that types must provide.
/// - The purpose of trait obj is to provide an abstraction of common behavior
use gui::Draw;
use gui::{Screen, Button};

pub trait Draw {
    // must be implement
    fn draw(&self);
}

pub struct Screen {
    // Any type that implements Draw can be stored on Heap
    // dynamic dispatch not static dispatch(컴파일 타임에 정의되는 타입)
    pub components: Vec<Box<dyn Draw>>
}

impl Screen {
    pub fn run(&self) {
        for component in components.iter() {
            component.draw();
        }
    }
}
pub struct Button {
    pub width: u32,
    pub height: u32,
    pub label: String,
}

impl Draw for Button {
    // real draw buttton
    fn draw(&self) {

    }
}
pub struct SelectBox {
    pub width: u32,
    pub height: u32,
    pub options: Vec<String>,
}

impl Draw for SelectBox {
    fn draw(&self) { // real draw SelectBox

    }
}


fn main() {
    let screen = vec![
        Box::new(SelectBox {
            width: 100,
            height: 50,
            options: vec![
                String::from("예"),
                String::from("아니요"),
                String::from("모름"),
            ]
        }),
        Box::new(Button {
            width: 100,
            height: 50,
            options: String::from("버튼!")
        }),
    ];
    // trust me. each component are Must exist method: draw
    screen.run()
}
