use std::rc::{Rc, Weak};
// mutable, dyn borrow
use std::cell::RefCell;


#[derive(Debug)]
struct Node {
    value: i32,
    /// 부모노드는 자식노드를 소유 해야만 한다
    /// 자식 노드는 부모노드를 소유 하지 않아도 된다
    /// 즉 부모 노드 해제시 자식 노드 또한 해제 되어야 한다
    /// 자식 노드가 해제 되더라도 부모 노드는 존재 해야만 한다.
    /// Circular reference 만약 Rc로 구현 할 경우 ref_count 가 0이 될수가 없다
    /// 이경우 약한 참조를 사용한다
    parent: RefCell<Weak<Node>>,
    child: RefCell<Vec<Rc<Node>>>,
}

fn main() {
    let leaf = Rc::new(Node {
        value: 3,
        parent: RefCell::new(Weak::new()),
        child: RefCell::new(vec![]),
    });
    // 만약 부모노드가 삭제 되었거나 없다면 None 반환
    println!("leaf parent = {:?} \n ====================", leaf.parent.borrow().upgrade());
    println!(
        "1. leaf strong = {}, weak = {}\n ===============",
        Rc::strong_count(&leaf),
        Rc::weak_count(&leaf)
    );
    {
        let branch = Rc::new( Node {
            value: 5,
            parent: RefCell::new(Weak::new()),
            child: RefCell::new(vec![Rc::clone(&leaf)]),
        });
        // create new Weak Pointer
        *leaf.parent.borrow_mut() = Rc::downgrade(&branch);
        println!(
            "2. branch strong = {}, weak = {}\n ===============",
            Rc::strong_count(&branch),
            Rc::weak_count(&branch)
        );            
        println!(
            "3. leaf strong = {}, weak = {} \n ===============",
            Rc::strong_count(&leaf),
            Rc::weak_count(&leaf)
        );   
    }
    println!(
        "4. leaf strong = {}, weak = {} \n ===============",
        Rc::strong_count(&leaf),
        Rc::weak_count(&leaf)
    );   
    // 무한히 출력되지 않는 다면 순환 참조가 발생 하지 않는다는 뜻.
    println!("leaf parent = {:?} \n ====================", leaf.parent.borrow().upgrade());



}
