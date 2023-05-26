# Table of Contents
INWORK
- [Table of Contents](#table-of-contents)
- [개념 및 예시](#개념-및-예시)
  - [문법, 흐름](#문법-흐름)
    - [문법 오류](#문법-오류)
- [에러 처리(Error Handling)](#에러-처리error-handling)
  - [에러의 표시와 발생(Representing and Throwing Errors)](#에러의-표시와-발생representing-and-throwing-errors)
  - [에러 처리(Handling Errors)](#에러-처리handling-errors)
    - [Schedules](#schedules)
    - [커스텀 객체](#커스텀-객체)
    - [Then Catch Finally 에서의 에러의 모습](#then-catch-finally-에서의-에러의-모습)
    - [Try Catch Finally 에서 에러의 모습](#try-catch-finally-에서-에러의-모습)


# 개념 및 예시
에러란 시스템의 패닉, 즉 실행중인 스크립트 파일 전체가 중지됩니다. 
[Dom parser](https://developer.mozilla.org/ko/docs/Web/API/DOMParser) 
다음 스크립트 태그를 찾아 실행 시킬 것이고 우리의 번들링된 앱은 멈추게 될 것 입니다.
개발 과정에서 만난 로컬환경 한정 친구인 에러에 대해 발생, 감지, 증식, 조작을 통해
더욱 안정적인 서비스를 제공 할 수 있겠습니다.

## 문법, 흐름
아래 예제는 try 안에서 어떤 에러가 발생하던 코드는 끝까지 실행됩니다.


```javascript
try {
  alert('try 블록 시작');  // (1) <--
  lalala; // 에러, 변수가 정의되지 않음!
  alert('try 블록 끝(절대 도달하지 않음)');  // (2)
} catch(err) {
  alert(`에러가 발생했습니다!`); // (3) <--
} finally {
  alert('그래도 이건 실행 될 걸')
}
alert('심지어 이것도')
```
자식 노드에서 부모 노드로 전파되는 이벤트 흐름을 연상하면, 당연합니다.
버블링을 `catch(err) {` 블록에서 멈추었고 더이상 전파되지 않았기 때문이죠
이부분을 바꿔보겠습니다.
```typescript
catch(err) {
  alert(`에러가 발생했습니다!`); // (3) <--
  throw err
} 
```
catch 블록을 변경 하였을때, 부모로 이벤트가 전파되어(호출 스택을 버블링), 
'심지어 이것도' 메세지가 표시되지 않았음을 알 수 있습니다.
### 문법 오류
```javascript
try {
  {{{{{{{{{{{{
} catch(e) {
  alert("유효하지 않은 코드이기 때문에, 자바스크립트 엔진은 이 코드를 이해할 수 없습니다.");
}
```
try..catch는 실행 가능한(runnable) 코드에만 동작합니다. 실행 가능한 코드는 유효한 자바스크립트 코드를 의미합니다.
중괄호 짝이 안 맞는 것처럼 코드가 문법적으로 잘못된 경우엔 try..catch가 동작하지 않습니다.


# 에러 처리(Error Handling)
예를들어, 디스크에서 파일을 읽어 데이터를 처리하는 일을 한다고 할 때 
이 작업이 실패할 경우의 수는 여러가지가 존재합니다. 파일이 특정 경로에 존재하지 않거나, 
읽기 권한이 없거나 혹은 파일의 데이터가 식별할 수 있는 포맷으로 적절히 인코딩 되지 않은 경우 등 말이죠. 
이런 종류별 에러 상황을 식별해 사용자에게 제공해 주면 
프로그램 실행중 발생할 각 에러별로 사용자가 적절히 대응할 수 있도록 도울 수 있습니다.

어떤 명령은 항상 완전히 실행되는 것이 보장되지 않는 경우가 있습니다. 
그런 경우에 옵셔널을 사용해 에러가 발생해 값이 없다는 것을 표시할 수 있지만, 
어떤 종류의 에러가 발생했는지 확인할 수는 없습니다. 
이럴 때는 구제적으로 발생한 에러를 확인할 수 있어야 코드를 작성하는 사람이 
각 에러의 경우에 따른 적절한 처리를 할 수 있습니다.

## 에러의 표시와 발생(Representing and Throwing Errors)
Javascript 에서 에러는 JS 런타임 스택을 추적할 수 있는
객체 Error를 상속 받는 클래스로 표현됩니다.
이런 부모 자식이 트리를 이루는 구조는 에러의 유연한 대처에 용이합니다.

## 에러 처리(Handling Errors)
에러가 발생하면 특정 코드영역이 해당 에러를 처리하도록 해야합니다. 
예를들어, 문제를 해결하거나, 혹은 우회할 수 있는 방법을 시도하거나 
아니면 사용자에게 실패 상황을 알리는 것이 에러 처리의 방법이 될 수 있습니다.


```
let error = new Error(message);
// or
let error = new SyntaxError(message);
let error = new ReferenceError(message);
```

### Schedules
### 커스텀 객체
### Then Catch Finally 에서의 에러의 모습
### Try Catch Finally 에서 에러의 모습