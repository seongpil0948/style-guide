use crate::List::{Cons, Nil}

/// Construct 하나의 값과 쌍이되는 인수로서 새로운 쌍을 생성한다.
/// 마지막 아이템은 Nil 이라는 값을 가진다
enum List {
    Cons(i32, List),
    Nil
}

/// How to Computed Non-Recursive size?
/// Enum 일 경우 각 필드의 크기 우선순위, 와 사이즈를 미리 계산하지만
/// 재귀함수 일 경우 무한한 재귀함수의 크기를 미리 계산 할 수 없다
/// 
let list = Cons(1, Cons(2, Cons(3, Nil)))