use std::cmp::Ordering::{Less, Greater, Equal};
use std::mem;

// A type implementing Indexed<K> that is used as value in a BinaryTree may be indexed by K,
// that is, lookup functions can take a key: K instead of the full value. This is necessary for
// implementing associative containers.
pub trait Indexed<K: ?Sized> {
    fn key(&self) -> &K;
}

impl<T> Indexed<T> for T
    where T: Ord
{
    fn key(&self) -> &T { self }
}

type Link<T> = Option<Box<Node<T>>>;

struct Node<T> {
    value: T,
    left: Link<T>,
    right: Link<T>,
}

impl<T> Node<T> {
    fn new(value: T) -> Self {
        Node { value: value, left: None, right: None }
    }
}

pub struct BinaryTree<T> {
    root: Link<T>,
}

impl<T> BinaryTree<T> {
    pub fn new() -> Self {
        BinaryTree { root: None }
    }

    // Get a reference to the link at which `key` is or should be located
    fn locate<K>(&self, key: &K) -> &Link<T>
        where T: Indexed<K>,
              K: Ord
    {
        let mut anchor = &self.root;
        while let Some(ref node) = *anchor {
            match node.value.key().cmp(key) {
                Less => anchor = &node.left,
                Greater => anchor = &node.right,
                Equal => return anchor,
            }
        }
        // No such entry, anchor is pointing to the insert position of value
        anchor
    }

    fn locate_mut<K>(&mut self, key: &K) -> &mut Link<T>
        where T: Indexed<K>,
              K: Ord
    {
        let mut anchor = &mut self.root;
        loop {
            // Not as simple as `locate`: The binding of `anchor` must
            // be removed before destructuring and re-assigning it in
            // order to avoid duplicate &muts
            match {anchor} {
                &mut Some(ref mut node) if key != node.value.key() => {
                    anchor = if key < node.value.key() {
                        &mut node.left
                    } else {
                        &mut node.right
                    }
                },

                other @ &mut Some(_) |
                other @ &mut None => return other
            }
        }
    }

    pub fn lookup<K>(&self, key: &K) -> Option<&T>
        where T: Indexed<K>,
              K: Ord
    {
        self.locate(key).as_ref().map(|node| &node.value)
    }

    pub fn insert(&mut self, value: T) -> bool
        where T: Ord
    {
        let anchor = self.locate_mut(&value);
        match *anchor {
            Some(_) => false,
            None    => {
                *anchor = Some(Box::new(Node::new(value)));
                true
            }
        }
    }

    pub fn delete<K>(&mut self, key: &K)
        where T: Indexed<K>,
              K: Ord
    {
        delete_node(self.locate_mut(key));
    }

    pub fn iter(&self) -> Iter<T> {
        Iter { current: &self.root, stack: Vec::new() }
    }
}

// Returns the next in-order successor in a subtree
fn successor<T>(mut next: &mut Link<T>) -> &mut Link<T> {
    loop {
        match {next} {
            &mut Some(ref mut node) if node.left.is_some() => next = &mut node.left,
            other @ &mut Some(_) => return other,
            _ => unreachable!(),
        }
    }
}

// Removes a node by discarding it if it is a leaf, or by swapping it
// with its inorder successor (which, in this case, is always in a
// leaf) and then deleting the leaf.
fn delete_node<T>(link: &mut Link<T>) {
    if let Some(mut boxed_node) = link.take() {
        match (boxed_node.left.take(), boxed_node.right.take()) {
            (None, None) => (),
            (leaf @ Some(_), None) |
            (None, leaf @ Some(_)) => *link = leaf,
            (left, right) => {
                // take() followed by re-assignment looks like an awful hackjob, but appears
                // to be the only way to satisfy all cases in the match

                boxed_node.left = left;
                boxed_node.right = right;

                {
                    let node = &mut *boxed_node; // unbox
                    let next = successor(&mut node.right);
                    mem::swap(&mut node.value, &mut next.as_mut().unwrap().value);
                    delete_node(next);
                }
                *link = Some(boxed_node);
            }
        }
    }
}

impl<'a, T: 'a> IntoIterator for &'a BinaryTree<T> {
    type Item = &'a T;
    type IntoIter = Iter<'a, T>;

    fn into_iter(self) -> Self::IntoIter {
        self.iter()
    }
}

pub struct Iter<'a, T: 'a> {
    current: &'a Link<T>,
    stack: Vec<&'a Node<T>>
}

impl<'a, T: 'a> Iterator for Iter<'a, T> {
    type Item = &'a T;

    fn next(&mut self) -> Option<Self::Item> {
        while let Some(node) = self.current.as_ref() {
            self.stack.push(node);
            self.current = &node.left;
        }
        self.stack.pop().map(|node| {
            self.current = &node.right;
            &node.value
        })
    }
}

// fn pre_order (&self, vector: CV) {
//     match self {
//         Self::Empty => return,
//         Self::Leaf {
//             ref v, ref l, ref r
//         } => {
//             vector.push(*v);
//             l.pre_order(vector);
//             r.pre_order(vector);
//         }
//     }
// }
// fn in_order (&self) {
//     match self {
//         Self::Empty => return,
//         Self::Leaf {
//             ref v, ref l, ref r
//         } => {
//             l.in_order();
//             println!("{} ", v);
//             r.in_order();
//         }
//     }        
// }
// fn post_order (&self) {
//     match self {
//         Self::Empty => return,
//         Self::Leaf {
//             ref v, ref l, ref r
//         } => {
//             l.post_order();
//             r.post_order();
//             println!("{} ", v);
//         }
//     }  
// }

// fn lv_order (&self) {
//     let mut q = std::collections::VecDeque::new();
//     q.push_front(self);
//     while !q.is_empty() {
//         let node = q.pop_front().unwrap();
//         if let Some(v) = node.get_data() {
//             println!("{} ", v)
//         }
//         if let Some(l) = node.get_left() {
//             q.push_back(l);
//         }
//         if let Some(r) = node.get_right() {
//             q.push_back(r);
//         }
//     }         
// }  

fn main() {
    let mut set = BinaryTree::new();
    for &value in &[100, 5, 1, 10, -1] {
        set.insert(value);
    }
    for value in &[5, 1, 151] {
        set.delete(value);
    }
    for value in &set {
        println!("{}", value);
    }
}