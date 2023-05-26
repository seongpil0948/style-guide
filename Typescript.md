# Dev Guide for Typescript

이 문서는 [구글 타입스크립트 스타일 가이드](https://google.github.io/styleguide/tsguide.html)기반으로, 웹 개발자가 소스 코드 작성 시에 따라야 할 규칙과 그에대한 가이드를 기술합니다.
Typescript를 사용하는 것은 이제 필수입니다.

Prototype 스타일의 언어인 자바스크립트는 자유롭고 제한이 없다보니, 소스에 대한 검증이나 테스트가 다른 언어들 보다 어렵고, 타인의 소스를 읽는 것도 어렵습니다.

다시 말하자면 자유롭다는 것은 각각 개인들이 작성하는 소스도 규칙성이 많이 달라도 같은 목표를 달려갈 수 있지만, 반대로 남의 소스를 읽기 힘들다는 것입니다.

Typescript는 **Type**이 추가 되었고, 이로 인해 얻게 되는 이점도 강력해졌습니다.

. 만 누르면 자동으로 제안되는 가이드가 자바스크립트에서는 유추되어 나왔지만,정의된 타입이 있어야 하는 Typescript에서는 제대로 된 가이드가 가능해 집니다.

또한, 서버와 통신 시, DTO 레벨의 각각 Parameter들에 대한 검증도 할 수 있고, 내가 정의한 컴포넌트나 타입을 사용할 때, 사용하는 사람이 제대로, 뭔가를 빼먹어서 오동작 하는 것을 애초에 막아 줍니다.

## TODO
[ ] https://google.github.io/styleguide/tsguide.html#file-encoding-utf-8
[ ] https://gist.github.com/anichitiandreea/e1d466022d772ea22db56399a7af576b

## Table of Contents
- [Dev Guide for Typescript](#dev-guide-for-typescript)
  - [TODO](#todo)
  - [Table of Contents](#table-of-contents)
- [1. 구문](#1-구문)
  - [1.1 식별자(identifiers)](#11-식별자identifiers)
    - [1.1.1 약어 (Abbreviations)](#111-약어-abbreviations)
    - [1.1.2 $](#112-)
    - [1.1.3 테스트 케이스(test name)](#113-테스트-케이스test-name)
    - [1.1.4 \_ 접두/미사(prefix/suffix)](#114-_-접두미사prefixsuffix)
    - [별칭(Aliases)](#별칭aliases)
- [Interface 선언](#interface-선언)
    - [서버와 통신하는 컨텍스트에서 프론트/백엔드가 같은 인터페이스를 준수하는 것은 매우 중요합니다.](#서버와-통신하는-컨텍스트에서-프론트백엔드가-같은-인터페이스를-준수하는-것은-매우-중요합니다)
  - [Interface 사용 방법](#interface-사용-방법)
  - [Enum 선언](#enum-선언)
  - [Enum 사용 방법](#enum-사용-방법)
- [Union 과 Intersection 타입](#union-과-intersection-타입)
  - [Union 타입](#union-타입)
    - [Union을 사용하지 않는 경우](#union을-사용하지-않는-경우)
  - [Interaction 타입](#interaction-타입)


# 1. 구문 
## 1.1 식별자(identifiers)
- 변수, 상수, 함수명 혹은 특정 코드 스코프에 대한 레이블 생성 및 지정을 위한 
  자료형 혹은 저장매커니즘과 함께 혹은 독단적으로 사용하는 텍스트.
- 반드시 ASCII letters, digits(숫자), underscores(언더바)로 구성되어,
  정규식 `[\)\w]+` 을 만족해야 합니다.

|스타일|카테고리|
|---|---|
|PascalCase| 클래스/ 인터페이스/ 커스텀타입/ 데코레이터/ 타입파라미터|
|lowerCamelCase|일반 변수, 파라미터, 함수이름, 메소드, property, 모듈 등 |
|CONSTANT_CASE|전역 constant 변수, enum values 를 포함한 변수|

**상수**
``` typescript
const UNIT_SUFFIXES = {
  'milliseconds': 'ms',
  'seconds': 's',
};
// constant can also be a static readonly property of a class.

class Foo {
  private static readonly MY_SPECIAL_NUMBER = 5;

  bar() {
    return 2 * Foo.MY_SPECIAL_NUMBER;
  }
}
```
**타입 파라미터 (Type parameters)**
``` typescript
Array<T> | interface Map<Key, Value> {}
```


### 1.1.1 약어 (Abbreviations)
두문자어와 같은 어휘에 대한 약어를 통해 선언할 camelCase를 사용하십시오. 
``` typescript
// bad
const loadHTTPURL = "..."
// good
const loadHttpUrl = "..."
// ok, if reserved(required by a platform)
XMLHttpRequest
```
### 1.1.2 $
서드파티 프레임워크/라이브러리에 의한 경우를 제외하고, 일반적으로 $는 사용하지 않아야 한다.

### 1.1.3 테스트 케이스(test name)
**example**
```typescript
describe('import vue components', () => {
    test('dynamic imports as expected', async () => {
    const name = 'Hello'
    const cmp = await import(`../components/${name}.vue`)
    expect(cmp).toBeDefined()}}
```
### 1.1.4 _ 접두/미사(prefix/suffix)
사용하지 않을 파라미터 또는 프로젝트 고유의 규칙(eslint, README등 문서 기재)를 제외하고
절대 접두사 혹은 접미사로 사용 하지마십시오.

### 별칭(Aliases)
기존 식별자를 로컬 스코프 식별자에 할당 할 때,
네이밍 규칙은 기존 식별자를 따르십시오.
``` typescript
const {Foo} = SomeType;
const CAPACITY = 5;

class Teapot {
  readonly BrewStateEnum = BrewStateEnum;
  readonly CAPACITY = CAPACITY;
}
```

# Interface 선언
Interface의 선언은 기본적으로 아래의 룰을 따르십시오.

* interface는 프로젝트 전체에서 사용되는 Component나 Utils에 대해서는 `~/types`에 정의합니다.
* 각 서비스 별 디렉토리에 `types` 디렉토리에서 정의합니다.
* `export`를 명시하여, 외부에서 사용할 수 있게 선언합니다.
* 사용될 요소들은 각 타입을 제대로 정의하여 사용합니다. `any` 형식의 사용은 지양합니다.
* 선언 시, 이름 앞에 `I`를 붙입니다.
* 정의된 interface를 import 할 경우 `import type`으로 가져와야 합니다.

> **tip** : `~` 는 `/src` 디렉토리를 의미합니다.


```typescript
// 사용 사례
export interface IAvatar {
  id: string
  name: string
  color?: string
  budget: number
  unit: string
  trans?: number
  useReport: boolean
}
```
### 서버와 통신하는 컨텍스트에서 프론트/백엔드가 같은 인터페이스를 준수하는 것은 매우 중요합니다.
`response.data` 가 절대 any 타입이 아니어야합니다.
```typescript
// bad
const res = axios.get(url)
const result = res.data as any
// good
const res = axios.get(url)
const authUser: IAvatar = res.data
emit("update:userId", authUser.id)
```

- `as` 키워드를 사용하여 캐스팅 하는 것을 지양하십시오. 타입스크립트의 추론으로 캐스팅 될 수 있습니다.

* `?`를 사용하는 경우는 그 값이 필수값이 아닐 경우이며, 이 기호가 없을 경우는 필수 값입니다.
* 필수 값을 경우 객체를 셋팅할 때, 값을 셋팅하지 않으면 안됩니다.
* interface 요소 안에 또 다른 interface나 enum을 사용할 수 있습니다.


```typescript
import type { FINANCIAL_TYPE, IN_OUT } from './enums'

export interface IFinancial {
  id: string
  parentType: FINANCIAL_TYPE | string
  childType: FINANCIAL_TYPE | string
  inout: IN_OUT
  amount: number
  worth: number
}
```

* `|` 기호를 통해 여러(Union) 타입을 지정할 수 있습니다.
* `enum` 형을 interface 선언하기 위해 type으로 사용하는 경우 `import type`으로 가져와 사용해야 합니다.


## Interface 사용 방법

Interface를 사용하는 건 독립적으로 제공되는 뭔가를 사용할 때 그 빛을 발합니다. 서버의 API 호출할 때, 이미 만들어진 컴포넌트를 호출할 때, 공통 함수를 호출할 때 등등 **이걸 사용하기 위해서는 어떤 파라미터를 전달해야 했지?** 라고 생각하며 항상 정의했던 대로 가서 확인했던 일은 현저히 줄어들 것입니다. 사용 할 때 `IDE`에서 가이드를 줄 것입니다. 필수 값을 정의하지 않았다면 않았다고 노티를 줄 것이고, 어떤 타입으로 넣어야 할지 가이드도 할 것입니다. Interface는 Framework내 `~/types` 디렉토리에서 적절한 namespace를 가진 파일안에 선언될 것이며, 이를 가져와 사용하면 됩니다. 각 서비스에서 사용되는 경우 `~/[서비스 명]/types`에 위치합니다.

```typescript
import { IAvatar } from '~/types'
// ...
// 일반적인 상수로 선언할 때,
const bank: IAvatar = {
  id: 'bank',
  name: '부자은행',
  color: 'bg-gray-500',
  budget: 0,
  unit: '',
  useReport: false,
}
// ref로 선언할 때,
// ref는 타입 정의를 ref<> 안에서 정의합니다.
const bank = ref < IAvatar > ({
  id: 'bank',
  name: '부자은행',
  color: 'bg-gray-500',
  budget: 0,
  unit: '',
  useReport: false,
})
// reactive로 선언할 때,
const bank: IAvatar = reactive({
  id: 'bank',
  name: '부자은행',
  color: 'bg-gray-500',
  budget: 0,
  unit: '',
  useReport: false,
})

// id 값은 string으로 parameter 셋팅 되고, return 되는 값은 IAvatar 일 경우,
const getPlayer = (id: string): IAvatar => {
  // ...
}
```


## Enum 선언

열거형은 상태 (ex: 문서 진행 간 각각의 상태 값을 정의, 각각 레포트의 수입/지출 상태 정의 등) 값을 정의할 때, 많이 사용 됩니다. Enum은 특이하게 Object 혹은 Type으로 사용이 가능합니다.

Enum의 선언은 기본적으로 아래의 룰을 따릅니다.

* Enum은 프로젝트 전체에서 사용되는 Component나 Utils에 대해서는 `~/types/enums/` 아래 파일들에 선언합니다.
* 각 서비스 별 디렉토리에 `types/enums` 디렉토리에서 정의합니다.
* `export`를 명시하여, 외부에서 사용할 수 있게 선언합니다.
* Enum은 상수 선언이므로, 대문자로 구성하며, 단어와 단어 사이는 `_`로 표현합니다.

  ```typescript
  // 일반적인 사용 방법
  // interface 정의에 사용될 경우
  import type { FINANCIAL_TYPE, IN_OUT } from './enums'

  export enum IN_OUT {
    IN = 'in',
    OUT = 'out',
  }

  // 값을 넣지 않으면 자동으로 0부터 숫자로 셋팅됨 (배열은 아닙니다.)
  export enum UNIT_POSITION {
    FRONT, // FRONT = 0
    BACK, // BACK = 1
  }

  export interface IFinancial {
    id: string
    parentType: FINANCIAL_TYPE | string
    childType: FINANCIAL_TYPE | string
    inout: IN_OUT
    amount: number
    worth: number
  }
  ```



> **참고** : Enum 선언 간 값을 셋팅하지 않으면, 자동으로 0부터 카운팅 되어 셋팅됩니다. Object 형태로 만들어 질 때, Key 값을 중복하여 생성됩니다. 정의한 내역이 2개라면, Key 값은 4개 생성됩니다. Enum에 정의한 값이 몇개인지 카운팅 할적에는 위의 예제에 IN_OUT과 같이 값을 정의한 항목만 `Object.keys()`로 key 값을 추출하여 카운팅 하면 됩니다.



## Enum 사용 방법

기존 상수 값을 좀 더 유려하게 처리하는 방법인 Enum의 사용 법은 그리 어렵지 않습니다. 단지 선언에서 차이가 있는데 Type으로 사용할 것인지, 아니면 정의된 값을 사용할 것인지에 따라 선언하는 방식이 다릅니다. 해당 내용은 Interface항목에 정의했으니 같이 확인하십시오.

```typescript
enum IN_OUT {
  IN = 'in',
  OUT = 'out',
}

// ...
const reportState: IN_OUT = IN_OUT.IN

// 이미 형이 정의된 내역이면 바로 값을 넣어도 자동으로 형이 셋팅
const reportState = IN_OUT.IN
```


# Union 과 Intersection 타입

## Union 타입

우리는 한개의 이상의 타입을 가진 파라미터를 다루어야 할때 다음과 같이 작성 할 수 있습니다.

```typescript
// BAD
function padLeft(value: string, padding: any) {
  if (typeof padding === "number") {
    return Array(padding + 1).join(" ") + value;
  }
  if (typeof padding === "string") {
    return padding + value;
  }
  throw new Error(`Expected string or number, got '${typeof padding}'.`);
}
 
padLeft("Hello world", 4); // returns "    Hello world"

```

위 코드의 문제는 padding이 __any__ 라는 것입니다.
그리고 다음의 상황은 타입 체크시 에러가 발생하지 않지만 런타임에서 오류를 반환 합니다.

```typescript
let indentedString = padLeft("Hello world", true);
```

이에 우리는 다음과 같이 Union 타입 선언을 통해 에러를 방지 할 수 있습니다.

```typescript
// BAD
function padLeft(value: string, padding: string | number) {
  ...
}
```

### Union을 사용하지 않는 경우

```typescript
// trinomial boolean
// bad
type TriBoolean = "Yes" | "No" | "Normal";
// good
enum TriBoolean {
  YES="YES",
  NO="NO",
  NORMAL="NORMAL",
}
```

## Interaction 타입

Intersection 타입은 Union 타입과 비슷하지만
여러개 타입을 한개의 타입으로 합치는 기능에서 다릅니다.

예시로 여러 종류의 네트워크 에러들에 대한 일관성 있는 핸들링이 필요 할 때
여러 에러 타입에 공통 필드가 정의된 인터페이스(ErrorHandling) 를 merge 하여 사용 하십시오.

```typescript
interface ErrorHandling {
  success: boolean;
  error?: { message: string };
}
 
interface ArtworksData {
  artworks: { title: string }[];
}
 
interface ArtistsData {
  artists: { name: string }[];
}
 
// These interfaces are composed to have
// consistent error handling, and their own data.
 
type ArtworksResponse = ArtworksData & ErrorHandling;
type ArtistsResponse = ArtistsData & ErrorHandling;
 
const handleArtistsResponse = (response: ArtistsResponse) => {
  if (response.error) {
    console.error(response.error.message);
    return;
  }
 
  console.log(response.artists);
};
```
