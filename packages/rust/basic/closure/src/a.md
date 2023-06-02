# Closure
* 변수에 저장 가능한 함수 형식의 구조
* 주변환경 캡쳐
* JS의 Arrow Function 과 유사.. 동일?
* Anonymous Function
* 한번인자가 들어가면 그때 타입이 정해져 다음에도 같은 타입을 이용해야한다
* 클로저 들어가기 전에 주변 환경을 캡쳐하여 메모리 저장 
    - 클로저 내에서  Out Scope 접근 가능 (Closure Env).
    - 주변 값이 많을땐 함수사용
    - 함수가 매개변수를 저장 할때와 동일하게 캡처 (2가지)
    1. Ownership(OW)
    2. Borrow as Mutable/Imutable
* 그렇다면 함수 들어간 다음에 주변환경이 바뀌는 ( async 한 상황에서는 ?)