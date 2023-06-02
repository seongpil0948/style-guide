use std::rc::Rc;
use std::cell::RefCell;



/// * Each Vector must available to acceess Child Node
/// * Vec<Rc<Node>> for instance acquire OW(owner ship) and 
///     - The instance must be accessible to each node in the tree
///     - And RefCell<T> for modify (불변성인 변수를 런타임에 변경 할 수 있도록)
/// * Rc(reference count ) for shared 1 heap data
///     - if parent and child 가 강한참조(Rc)로 구현된다면 서로 소유권을 쥐고 있기때문에 
///       Reference Count 가 0이 되지 않는다(메모리 누수) = 순환참조 발생
/// * Weak Reference 
///     - 부모노드는 자식 노드를 소유한다(OW)
///     - 부모노드 해제시 자식노드 메모리도 해제
///     - Weak 로 선언시 RC가 0이 아니어도 해제 가능
///     - 소유권이 아닌 참조만 가져온다.
#[derive(Debug)]
struct Node {
    value: i32,
    parent: RefCell<Weak<Node>>,
    children: RefCell<Vec<Rc<Node>>>
}

fn go_tree () {

    // shared leaf's Node and accessible to leaf's Node 
    // leaf's Node Refenence count += 1
    let branch = Rc::new(Node {
        value: 5,
        parent: RefCell::new(Weak::new()),
        children: RefCell::new(vec![Rc::clone(&leaf)]),
    });

    // upgrade = 참조를 빌려온다
    println!("leaf Parent = {:?}", leaf.parent.borrow().upgrade());

    let leaf = Rc::new(Node {
        value: 3,
        parent: RefCell::new(Weak::new()), 
        children: RefCell::new(vec![]),
    });    

    *leaf.parent.borrow_mut() = Rc::downgrade(&branch);
    println!("leaf Parent = {:}", leaf.parent.borrow().upgrade());
}