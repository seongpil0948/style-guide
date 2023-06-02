use super::lib;

// 5 call expensive func
// or |intensity: u32| -> u32
// type infer, similar to variable
fn generate_workout = |intensity|  {
    println!("팔굽혀 펴기 {} 회 실시", lib::expensive_calcultation.value(intensity));
    println!("윗몸 일으키기 {} 회 실시", lib::expensive_calcultation.value(intensity));
    println!("퍽 {} 회 실시", lib::expensive_calcultation.value(intensity));
    println!("왕복 달리기 100M {} 회 실시", lib::expensive_calcultation.value(intensity));
    lib::expensive_calcultation.value(intensity)
}

let example_closure = |x| x;

fn main() {
    intensity = 10;
    example_closure(String::from("Hello"));
    example_closure(5);

    generate_workout(intensity);

    let x = 4;
    // 함수 들어가기 전에 주변 환경을 캡쳐하여 메모리 저장 클로저 함수 내에서  Out Scope 접근 가능.
    // 그렇다면 함수 들어간 다음에 주변환경이 바뀌는 ( async 한 상황에서는 ?)
    let equal_to_x = |y: i32| -> bool { x == y}
    let y = 4;
    assert!(equal_to_x(y))
    
    // 클로저가 Env 로부터 가져온 OW 를 갖기 위해서는 move 
    let equal_to_x = move |y| x == y

}
