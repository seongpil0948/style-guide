~~~
Create a String Instance using a string literal

{
    let mut s = String::from("hello")
    s.push_str(" world");
}
~~~
String is the dynamic heap string type, <br>
str is normally called "string slice"

https://stackoverflow.com/questions/24158114/what-are-the-differences-between-rusts-string-and-str
1. 문자열 리터럴
    - 컴파일 시점에 그 길이를 알 수 없다.
    - 사용할 메모리를 바이너리 형태로 미리 변환 불가.
    - 사용할 메모리를 런타임에 OS 에 요청( 함수 호출시 메모리 요청됌 )
    - 사용 완료 이후에는 OS에 메모리를 반환 해야한다
        - Garbage Collector 가 있는 언어는 더이상 참조되지 않는 메모리를 트리형태로 추적 및 해제 (개발자가 할 필요가 없다)
        - 메모리를 너무 일찍 해제하면 버그, 두번 해제 해도 버그 유발, 정확히 1 allocate 1 free 필요
    

2. String 타입
    - 컴파일 시점에 일정 부분의 메모리를 미리 할당 가능 


* 하지만 러스트는 다른방식으로 수행한다
    - Scope 를 벗어날때 자동 해제. 위 예제에서 } 밖으로 나가면 해제
        - String 인 경우 drop() 자동 호출
    - C++ 의 RAII Pattern have a lot of influence
        Resource Acquisition Is Innitialization

<br>
<br>

~~~
let s2 = s;
~~~

* C or C++ 
    - s 는 Pointer 이며  address, length, capacity 를 가지고 있으며  스택에 저장되며
    - 찐 데이터는 힙에 2컬럼 인덱스, 값 으로 이루어져 있다.
    - 위는 포인터를 복사한 상태이다.
    - 같은 힙 데이터를 바라본다.
    - 스택이 늘어난다
* Rust 에서 s 는
    - 스택(Pointer)을 복사한후 기존 변수를 버린다
    - RAII 패턴을 따르기 때문에 둘중 한변수가 해제되면 안되기 때문이다.
        - called Double Free Error, raise Memory Corruption
    - 데이터가 커도 경우 런타임 안빡세다
    - deep copy 와 비슷하지만 기존 변수를 버리기 때문에 Move 라고 친다
    - 만약 Heap 데이터 복사를 원한다면 공통 메소드 Clone 사용
~~~ 
let x = 5;
let y = x;
println!("{}, {}", x, y)
~~~
* 위와 반대로 동작하는 것 처럼 보인다
    - 컴파일 시점에 이미 크기를 알 수 있다. -> 둘다 컴파일때 메모리 할당
    - Clone 함수 실행해도 차이점 없당
    - 이 경우에는 Copy Trait 특성 제공 (증명서)
        - 이전 변수를 새변수에 할당해도 Literal 때처럼, 변수를 버리지 않는다
        - 하지만 Drop trait 특성이 있다면 버린다 -> 컴파일 에러 발생
        - 미리 길이를 알수 있는 타입은 다 Copy trait 가 있다
            - (i32, u32, f64) = O
            - (i32, u32, String) = X


~~~
    let s String::from("hello");  // m allocate (Drop Trait)
    func(s) // after now , s is not valid

    let x:f64 = 0.5;    // aleady allocate (Copy Trait)
    func(x) // x is valid
~~~

# 아 ㅈㄴ 복잡하다
<br>
<br>

## 참조와 대여

~~~
s3 = func(%s)

case 1
    let b1 = &mut s3; -- ok
    let b2 = &mut s3; -- second is error 하나만 참조 가능

case 2
    let b1 = s3; -- ok
    let b2 = s3; -- ok
    let b2 = mut s3; -- error
~~~
* &(ampersand) 참조(reference)로 가즈아
    - ampersand 의 반대는 dereferencing(역참조) = *
    - 힙에있는 데이터를 가져오는게 아니라 참조 ㅋ
    - 소유권이 없기 때문에 돌려줄 필요도없음
    - 매개변수로 참조를 전달하는 것을 대여 (borrowing)
* 제약, data races, race condition 컴파일 에러발생
    - 둘 이상의 포인터가 동시에 같은 데이터를 참조 혹은 수정 접근시
    - 포인터를 수정 할때 ㅋㅋ
    - 데이터에 대한 접근을 동기화 할 수 있는 Machanism/Logic 이 없거나 불안정할때

<br>
<br>
<br>

## 죽은 참조, refer Outdate Memory, Stale Memory, Static LifeTime

~~~
let a = func();
fn func() -> &String {
    let s = String::from("hello");
    &s // ?? s 는 밖에 나가면 메모리 반환 될텐데;;... 왜참조하니 ㅠㅠ
    s // ok -> s 의 ownership 이 함수를 호출한 코드로 이동하기 때문에 메모리 해제 X
}
~~~~
<br>
<br>

## Slice Type
<br>

~~~
fn first_word(s: &String) -> ?
~~~
* 인자가 소유권이 없기때문에 signiture 로 선언 해도 됌
<br>
<br>

~~~
fn first_word(s: &String) -> (usize, usize) {
    let bytes = s.as_bytes();
    let mut idx = 0;

    // destructing tuple from enumerate
    // and must not have ownership
    // call iterator from among bytes attribute
    for (i, &item) in bytes.iter().enumerate() {
        // comp byte literal
        if item == b' ' {
            idx = i;
        }
    }
    (s.len(), idx)

}
~~~
* 문자 중간에 공백 있는지 확인

<br><br>

~~~
let mut s = String::from("hello world");
let word = first_word(&s) // 5 할당(공백)

s.clear // s = 빈문자열 '' 
~~~
* 함수로 부터 공백 인덱스를 할당 받은 word 지만 s가 바뀐경우
    - 쓸모 없어졌다. -> 버그 유발
    - .. Slice 가 필요해!!

<br><br>
~~~
let len = s.len();
let slice = &s[3...len];
let slice = &s[3..];

fn first_word(s: &String) -> &str {
    let bytes = s.as_bytes();

    for (idx, &item) in bytes.iter().enumerate() {
        // comp byte literal
        if item == b' ' {
            return &s[0...i];
        }
    }

    &s[..]
}
~~~

<br><br>
~~~
fn func(s: &str) -> {}
    is better than
fn func(s: &String) -> {}

both String, slicing become &str
~~~

<br><br>
~~~
~~~

<br><br>
~~~
~~~

<br><br>
~~~
~~~