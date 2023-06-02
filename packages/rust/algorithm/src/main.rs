extern crate algorithm as c;
use c::collections::graph::Graph;
// use c::collections::stack::Stack;


fn main() {
    println!("HELLO WORLD");
    let MAX_INPUT: usize = 10;
    let mut g = Graph::new(MAX_INPUT, MAX_INPUT * 10);
    // let s: Stack<usize> = Stack::with_capacity(MAX_INPUT);
    g.add_arc(1, 2);
    println!("{:?}", g);
    g.add_arc(3, 4);
    println!("{:?}", g);
    g.add_arc(3, 5);
    g.add_arc(3, 6);
    g.add_arc(3, 7);
    println!("{:?}", g);
    g.adj_list(3).collect::<Vec<_>>().iter().for_each(move |data| {
        println!("adj {:?}", data);
    });

}
