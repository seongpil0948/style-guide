# 1. Coding Guide
* 순수 함수를 사용할 경우, `parameter`와 `return` 되는 값은 **Type** 정의 하십시오. 일반적인 함수도 `parameter`가 있는 경우 필수로 **Type**을 정의해야합니다.

* `import`를 할 때, `.js`, `.ts`, `.vue` 등 확장자를 입력하지 않아도 Framework에서는 접근하여 사용 가능합니다. 

* 확장자를 입력하지 않으면 좋은 한가지 점은, 내부적으로 분리가 필요할 경우 디렉토리로 파일명과 동일하게 디렉토리 명을 작성하여 대치하는데, 그 안에 `index`파일을 만들어 놓으면, `import` 수정 없이 바로 접근이 가능합니다.

* 싱글톤 패턴으로 구성된 요소들을 만들 경우 네이밍은 대게 `use`를 앞에 붙여 함수형의 리턴 형으로 오브젝트를 가져와 사용할 수 있게 합니다. 대표적으로 `useRouter`, `useStore` 등이 있습니다.

* 웹앱 URL/URI 는 `https://axios-http.com/kr/docs/handling_errors` 와 같이 상위경로와 관계를 잘 표현 할 수 있도록 하십시오.

* 가장 이상적인 개발 방법은 if 가 적은 코드를 작성하는 것입니다. (API를 사용)
  * if 가 선언된 순간 그 코드는 분기점이 생기며, 복잡도가 올라갑니다.


## 2. Naming
- 애버커스에서 고민한 네이밍 목록으로 모든프로젝트에서 일관된 네이밍을 위해 제작 중입니다.
  - 반드시 링크를 클릭하여 참여하십시오. [네이밍 History](https://abacus02-my.sharepoint.com/:x:/g/personal/seongpil0948_abacus02_onmicrosoft_com/EXwU2uVs3KxGqedcAflMackBXXZU43JtCS0IpRQduX7PNg?e=8rzSeT)

- 모든 선언 declare identity는 합성어 형태로 선언되어야 합니다. 
- 함수명은 (동사 + 명사)로 구성되며, 일반적으로 능동태를 사용하되 이벤트 등에 반응하는 기능인 경우 수동태를 사용하세요.

- 단수와 복수를 반드시 구별 하십시오. 
```typescript 
workers = new Worker (X)
worker = new Worker (O)
```
- 팀원들이 서로 어떻게 네이밍 하였는지 관심을 갖고, 피드백을 하십시오. 
- 누가 코드를 작성 하였는지 유추 할 수 없도록 코드의 모습이 유사해야 합니다.

- 코드는 네이밍만으로도 어떤 역할/동작/타입을 추론 할 수 있어야합니다.
`selectedAuthList -> selectedAuthIds`
- 프로젝트내에서는 특정단어는 하나의 역할을 의미해야 합니다.
```typescript
const auth = new Auth()
const authList = [new User(), new User()]
```
### 2.5 스토리 위주로 살펴보아 네이밍에 있어 흐름이 잘 이어지는지 판단 하십시오.
### 2.6 모든 선언 declare identity는 합성어 형태로 선언되어야 합니다.
```typescript
// bad
const user = new User()
const update = () => ...
// good
const userMe = new User()
const updateUser = () => ...
```

### 2.7 변수, 클래스는 능동적인 기능을 수행하므로, 명사를 사용하십시오.
```
// bad
class: FeatureExtract (X)
var: work (X)

// good
class: FeatureExtractor (O)
var: subWorker (O)
var: logger (O)
```
### 2.8 Data와 같은 범용 변수명을 피하십시오
```typescript
// bad
const userData = new User()
const userData = [new User(), new User()]
// good
const userMe = new User()
const userOthers = [new User(), new User()]
```


## 3. 순수함수 refactor
* 함수에서 함수를 **또 그안에서 함수를 호출**하는 형식보다 함수 안에서 순서대로 함수들이 실행하게 끔 하십시오. 
<br />
* 함수 사용이 tree 구조 처럼 깊어지게 된다면, 찾는 것도 디버깅 하는 것도 어려워 집니다. 또한, **재사용성**이 있는 함수라면 순수함수 형태로 만드는 것이 좋습니다.
<br />
* 오직 한개의 동작을 담당하고. 어떤 동작을 하는지 **추론이** 되거나, 명확하게 **리턴값**을 알 수 있습니다.
<br />
* 이벤트에 따라 수행하는 함수를 제외하고, **재사용성 있게 함수를 만들 경우**에는 순수 함수 형태로 만드는 것이 좋습니다. 
<br />
* 갑자기, 로직이 변경되어 함수를 수정해야 할 경우, **순수 함수일 때** 변경하거나 재 작성하기 편합니다.
<br />
* **이게 가장 중요합니다.** 개발을 하다 보면, 설계된 그대로 구현되어 차후 수정이 없다면 문제가 없지만, 수정이 잦아지면 순수 함수로 만들어야 할 이유를 자연스레 후회와 함께 깨닫게 됩니다. 그래서, 순수 함수로 만들어 놓는 것이 좋습니다. 
<br />
* 물론, 순수 함수로 만들 수 없는 경우도 있습니다. 그럴 경우에는 **최대한** 순수 함수로 만들 수 있도록 노력하십시오.


```js
// 이렇게 개발하지 마십시오.
function c() {
  d()
}
function a() {
  c()
}
function b() {
  a()
}

// 이런 형식으로 사용할 수 있게 하십시오.
function a() {
  // 실행함수
  b()
  c()
  d()
}

// 순수 함수 형식이라면 실행함수는 
// 그저 순수함수들을 실행만 시키면 됩니다.
function a() {
  bbb.value = b(bb)
  ccc.value = c(cc)
  ddd.value = d(dd)
}
```
```typescript
// 이것은 순수함수가 아닙니다.
// 인자가 명확하지않고, 리턴값도 없습니다.
// 옵션에 종속성이 있어서 외부에서 opt이 바뀔경우 이함수에 영향을 미칩니다.
// 우리는 이것을 실행함수라고 부르기로 했습니다.
export const getTodoList1 = async () => {
  const res = await fetch(`api/v1/todo?page=${opt.page}`);
  todoList = await res.json();
};

// 인자와 리턴값이 명확합니다.
// API 주소가 바뀌었을때, 주소만 바꾸면 당신의 서비스는 문제가 없을 것입니다.
export const getTodoList2 = async (page: string) => {
  const res = await fetch(`api/v1/todo?page=${page}`);
  return await res.json();
};

```
## 조건문
### else if 가 아닌 다중 if를 사용하는 경우
폼 검사와 같이 반드시 모든 if 스코프가 실행 되어야 하는경우, 혹은
가독성 면에서 다중 if가 나을 것이라 판단 할 때,
else if 문을 사용하지 마십시오.

### 2dept 이상의 if 문은 지양해야 합니다.
[3.1 파일 작성 방법](#순수함수-refactor)
## API
Front에서 API호출에 사용될 Backend 경로는 상수로 저장하지 않습니다.
api 모듈의 base url 혹은 proxy 기능을 사용합니다.
```typescript
// bad 
BASE_URL = "https://abacus.co.kr/api/path/1"
axios.get(BASE_URL)

// good
axios.get('/api/path/1')
```
  

## 주석
주석을 작성할 경우, 소스에 맞게 제대로 작성해야 합니다. 잘못된 주석은 소스를 읽기 힘들게 하는 주범입니다. 특히, Copy & Paste 경우 주석과 함께 할 경우, 주석을 그대로 두지 마십시오. 꼭 확인하여 수정이 필요하면 수정을 해야 합니다. 또한, 주석은 아래와 같이 작성 가이드를 따릅니다.

```js
// ! 크리티컬한 설명일 경우, 꼭 알아야 할 내용

// * 중요한 내용을 설명일 경우

// TODO: 향후 해야할 일을 설명 경우

// FIXME: 향후 수정이 필요한 내용일 경우 (하드 코딩 등)

// ? 소스를 볼 다른 개발자에게 문의할 경우

// 일반적인 주석
```


# CI&CD
## CI-Git
### Issue Flow
문제가 발생 하였을때 이슈 진행 Flow로 아래 형식을 따르십시오.
1. 이슈 티켓 생성
   1. Title: [{ issue type }]  { title }
2. 이슈에 대한 브랜치 생성 (create branch)
   1. 브랜치 이름은 kebab case 를 준수한다.
   2. [{issue number}]-[{issue type}]-[{issue name}]
3. Remote 저장소에 자동 생성된 브랜치의 fetch or pull(origin) 진행한다.
4. 로컬 저장소에서 코드 수정 및 커밋을 진행한다.
5. Git squash 로 커밋 메시지 정리한다. [rebase 를 이용한 squash](https://meetup.nhncloud.com/posts/39)
7. Git rebase 로 로컬 작업 결과를 최신화 한다.
8. 병합 대상 브랜치로 Merge Request를 생성한다.
9. maintainer 권한을 가진 인원( 최소 1명 이상)의  리뷰 이후  approve를 진행한다.
10. 병합을 확인하고 자신의 원격 브랜치가 삭제 되었는지 확인한다.

### Commit
**커밋 메시지 포맷**: `{Commit Type}(Summary): { Detail Content }`  
**예시**
<hr />

```
- 컴포넌트는 대문자로 시작
    - 🎨Design(Login): padding bottom 추가
- 페이지는 소문자로 시작
    - ✨Feat(editor): 복사하기 버튼 기능 추가
- store, function 등 소문자로 시작
    - ✨Feat(goToSelectedTab): 유틸 함수 추가
```
커밋 명령은 git에서 스테이징한 후 변경 사항을 로컬 리포지터리에 저장하는 데 사용됩니다. 
그러나 git에서 변경 사항을 저장하기 전에 수많은 변경 사항을 적용했을 수 있으므로 저장할 변경 사항을 git에 알려야 합니다. 
가장 좋은 방법은 커밋 메시지를 추가하여 변경 사항을 식별하는 것이기 때문에 커밋 메시지를 사용합니다.
#### Commit/Issue Type
- Feat: 특정 애플리케이션에 추가하는 새로운 기능
- Fix : 버그 또는 에러 수정 
	- issue type에서는 경우: **Bug**로 사용합니다.
- Hotfix: 이미 배포된 버전에 문제가 생긴경우
  - 파생된 브랜치로 PR을 통해 병합 되어야 합니다.
  - 핫픽스를 생성하기 전에 원격 저장소에서 fetch를 통하여 최신 상태로 유지해주는 것이 좋습니다.
- Style : 코드 포맷팅, 코드 오타, 함수명 수정 등 스타일 수정
- Refactor : 코드 리팩토링(똑같은 기능인데 코드만 개선)
- File(페이지 경로 또는 컴포넌트): 파일 이동 또는 제거, 파일명 변경
- Comment: 주석 수정 및 삭제
- Docs : 문서와 관련된 모든 것
- Chore : 정기적인 코드 유지 관리

# Refer
- https://insight.infograb.net/blog/2023/04/21/why-commit-convention-is-important/
