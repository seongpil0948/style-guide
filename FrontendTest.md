# Frontend 테스트 시작하기
이 글은 프론트엔드 기본 테스트의 종류와 개념 그리고
단위 테스트에 대한 이해를 목적으로 작성되었습니다.


- [Frontend 테스트 시작하기](#frontend-테스트-시작하기)
  - [우리는 왜 테스트를 해야 할 까?](#우리는-왜-테스트를-해야-할-까)
  - [테스팅이란 무엇인가?](#테스팅이란-무엇인가)
  - [다양한 유형의 테스트](#다양한-유형의-테스트)
      - [수동 테스트](#수동-테스트)
      - [자동화 테스트](#자동화-테스트)
      - [단위 테스트](#단위-테스트)
      - [통합 테스트](#통합-테스트)
      - [엔드투엔드(E2E) 테스트](#엔드투엔드e2e-테스트)
      - [성능 테스트](#성능-테스트)
  - [주요 개념](#주요-개념)
    - [검증(Assertion)](#검증assertion)
    - [그룹화(describe)](#그룹화describe)
  - [정리](#정리)
- [Advanced](#advanced)
  - [테스트 도입에 대한 개발자 관점](#테스트-도입에-대한-개발자-관점)
    - [결국 QA, 개발팀의 검수가 필요하지 않을까?](#결국-qa-개발팀의-검수가-필요하지-않을까)
    - [변수 시나리오 Chaining에 대한 제한](#변수-시나리오-chaining에-대한-제한)
    - [리소스에 대한 보장의 어려움](#리소스에-대한-보장의-어려움)
  - [클라이언트 관점](#클라이언트-관점)
    - [클라이언트는 기술을 가진 회사를 신뢰합니다.](#클라이언트는-기술을-가진-회사를-신뢰합니다)
    - [클라이언트는 산출물이 필요합니다.](#클라이언트는-산출물이-필요합니다)
    - [결국 신뢰를 얻습니다.](#결국-신뢰를-얻습니다)
- [Refer](#refer)
- [적용 가능 개발 방법론](#적용-가능-개발-방법론)
  - [TODO XP(Extreme Programming)](#todo-xpextreme-programming)
  - [TDD(Test Driven Development)](#tddtest-driven-development)
    - [개발주기](#개발주기)
  - [Ref](#ref)


## 우리는 왜 테스트를 해야 할 까?
- 프론트 프로젝트 규모가 커질수록 기능을 추가할 때마다 사이드 이펙트가 생기는 일이 빈번합니다.    
- 피해는 금전적 손실, 시간 낭비, 비즈니스 이미지 손상 등 다양합니다.
- 테스팅은 이러한 문제를 최소화하기 위해 반드시 필요합니다.   
- 우리는 상시 자동 모니터링 환경을 구축, 테스트 결과를 신속하게 인지 할 수 있어야합니다.  
- 사람이 직접 매 배포마다 많은 양의 **단위 테스트**들을 테스트 하는 것은 어렵습니다.

## 테스팅이란 무엇인가?
1. 소프트웨어가 문제가 없다를 보이는 것이 아니라 문제가 있다를 코드로써 밝히는 과정이다.
2. “이 소프트웨어가 완벽하군요!” 라고 하는 것이 아니라, “이 소프트웨어는 결함이 없군요!” 라고 말할 수 있어야한다.

## 다양한 유형의 테스트
#### 수동 테스트
수동 테스트는 QA 및 개발자등 사람이 테스트를 수동으로 실행하는 소프트웨어 테스트입니다. 

#### 자동화 테스트
**수동 테스트**와 반대로 코드 실행 / 테스트 스크립트를 작성하여, 테스트 실행을 **자동화** 합니다.  
테스터는 적절한 자동화 도구를 사용하여 테스트 스크립트를 개발하고 소프트웨어의 **유효성**을 검사합니다.  
목표는 적은 시간에 테스트 실행을 완료하는 것입니다.

#### 단위 테스트
단위 테스트는 매우 낮은 수준이며 애플리케이션의 소스와 가깝습니다. 
소프트웨어에서 사용하는 클래스, 구성 요소 또는 모듈의 개별 메서드와 함수를 테스트하는 것으로 구성되어 있습니다.

#### 통합 테스트
통합 테스트는 애플리케이션에 사용되는 여러 모듈 또는 서비스가 잘 작동하는지 확인합니다. 
예를 들어, 데이터베이스와의 상호 작용을 테스트하거나 
마이크로서비스가 예상대로 함께 작동하는지 확인하는 것일 수 있습니다.

#### 엔드투엔드(E2E) 테스트
엔드투엔드 테스트는 전체 애플리케이션 환경에서 소프트웨어를 사용한 사용자의 행동(**Action**)을 복제합니다. 다양한 사용자 흐름이 예상대로 작동하는지 확인하며 웹 페이지를 로드하거나 로그인하는 것처럼 간단할 수도 있고 이메일 알림, 온라인 결제 등을 확인하는 훨씬 더 복잡한 시나리오일 수도 있습니다.
- 애플리케이션의 비즈니스 요구 사항에 초점을 맞춥니다. 
- 작업의 출력만 확인하며 작업을 수행할 때 시스템의 중간 상태는 확인하지 않습니다.

#### 성능 테스트
애플리케이션의 신뢰성, 속도, 확장성, 반응성 측정을 목적으로 하는 테스트입니다 . 
예를 들어, 성능 테스트는 많은 요청을 실행할 때의 응답 시간을 관찰하거나 시스템이 대량의 데이터에 대해 어떻게 동작하는지 확인할 수 있습니다. 애플리케이션이 성능 요구 사항을 충족하는지 확인하고 병목 현상을 찾아내고 트래픽이 가장 많은 시간대의 안정성을 측정하는 등의 작업을 할 수 있습니다.

## 주요 개념
많은 오픈소스에서 공통적으로 사용되는 개념들을 설명합니다.

### 검증(Assertion)
	주어진 함수가 잘 동작하고 제대로 된 값을 반환하는지 검증해주는 역할
(테스터)가 실제 결과를 예상 결과와 비교하도록 허용하며, 이 비교가 실패하는 경우 테스트 결과를 "실패(Failure)"로 반환합니다.  
아래 표에서 locator은 **Dom Element** 로 이해 할 수 있습니다.
<table>
  <thead>
    <tr>
      <th align="left">Assertion</th>
      <th align="left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left">
        <a
          href="https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-be-attached"
          >expect(locator).toBeAttached()</a
        >
      </td>
      <td align="left">요소의 DOM 마운트 검증</td>
    </tr>
    <tr>
      <td align="left">
        <a
          href="https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-be-checked"
          >expect(locator).toBeChecked()</a
        >
      </td>
      <td align="left">체크박스 요소의 체크 검증</td>
    </tr>
    <tr>
      <td align="left">
        <a
          href="https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-be-disabled"
          >expect(locator).toBeDisabled()</a
        >
      </td>
      <td align="left">요소가 사용 불가 검증</td>
    </tr>
    <tr>
      <td align="left">
        <a
          href="https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-be-editable"
          >expect(locator).toBeEditable()</a
        >
      </td>
      <td align="left">요소가 수정 가능한 상태인지 검증</td>
    </tr>
    <tr>
      <td align="left">
        <a
          href="https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-be-empty"
          >expect(locator).toBeEmpty()</a
        >
      </td>
      <td align="left">요소 하위 노드 미존재 검증</td>
    </tr>
    <tr>
      <td align="left">
        <a
          href="https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-be-enabled"
          >expect(locator).toBeEnabled()</a
        >
      </td>
      <td align="left">요소 사용 가능 상태 검증</td>
    </tr>
    <tr>
      <td align="left">
        <a
          href="https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-be-focused"
          >expect(locator).toBeFocused()</a
        >
      </td>
      <td align="left">요소의 포커싱 검증</td>
    </tr>
    <tr>
      <td align="left">
        <a
          href="https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-be-hidden"
          >expect(locator).toBeHidden()</a
        >
      </td>
      <td align="left">요소가 화면에 보이지 않는지 검증</td>
    </tr>
    <tr>
      <td align="left">
        <a
          href="https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-be-in-viewport"
          >expect(locator).toBeInViewport()</a
        >
      </td>
      <td align="left">화면 크기내의 요소 존재 검증 </td>
    </tr>
    <tr>
      <td align="left">
        <a
          href="https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-be-visible"
          >expect(locator).toBeVisible()</a
        >
      </td>
      <td align="left">요소가 보여지고 있는지 검증</td>
    </tr>
    <tr>
      <td align="left">
        <a
          href="https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-contain-text"
          >expect(locator).toContainText()</a
        >
      </td>
      <td align="left">요소내 특정 텍스트노드의 포함 여부 검증</td>
    </tr>
    <tr>
      <td align="left">
        <a
          href="https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-have-attribute"
          >expect(locator).toHaveAttribute()</a
        >
      </td>
      <td align="left">요소의 DOM 속성(attribute) 소유 검증</td>
    </tr>
    <tr>
      <td align="left">
        <a
          href="https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-have-class"
          >expect(locator).toHaveClass()</a
        >
      </td>
      <td align="left">요소의 class 소유 검증</td>
    </tr>
    <tr>
      <td align="left">
        <a
          href="https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-have-count"
          >expect(locator).toHaveCount()</a
        >
      </td>
      <td align="left">요소의 자식 요소 개수 검증</td>
    </tr>
    <tr>
      <td align="left">
        <a
          href="https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-have-css"
          >expect(locator).toHaveCSS()</a
        >
      </td>
      <td align="left">요소의 CSS 스타일 검증</td>
    </tr>
    <tr>
      <td align="left">
        <a
          href="https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-have-id"
          >expect(locator).toHaveId()</a
        >
      </td>
      <td align="left">요소의 ID 속성 검증</td>
    </tr>
    <tr>
      <td align="left">
        <a
          href="https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-have-js-property"
          >expect(locator).toHaveJSProperty()</a
        >
      </td>
      <td align="left">요소의 직렬화/기본 된 자바스크립트 객체 속성 검증, </td>
    </tr>
    <tr>
      <td align="left">
        <a
          href="https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-have-screenshot-1"
          >expect(locator).toHaveScreenshot()</a
        >
      </td>
      <td align="left">요소의 스크린샷 존재 검증</td>
    </tr>
    <tr>
      <td align="left">
        <a
          href="https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-have-text"
          >expect(locator).toHaveText()</a
        >
      </td>
      <td align="left">요소의 텍스트 검증(extract)</td>
    </tr>
    <tr>
      <td align="left">
        <a
          href="https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-have-value"
          >expect(locator).toHaveValue()</a
        >
      </td>
      <td align="left">input 요소의 값 검증</td>
    </tr>
    <tr>
      <td align="left">
        <a
          href="https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-have-values"
          >expect(locator).toHaveValues()</a
        >
      </td>
      <td align="left">select 요소의 선택된 값 검증</td>
    </tr>
    <tr>
      <td align="left">
        <a
          href="https://playwright.dev/docs/api/class-pageassertions#page-assertions-to-have-screenshot-1"
          >expect(page).toHaveScreenshot()</a
        >
      </td>
      <td align="left">페이지에 해당하는 스크린샷 존재 검증</td>
    </tr>
    <tr>
      <td align="left">
        <a href="https://playwright.dev/docs/api/class-pageassertions#page-assertions-to-have-title"
          >expect(page).toHaveTitle()</a
        >
      </td>
      <td align="left">페이지에 해당하는 title 검증</td>
    </tr>
    <tr>
      <td align="left">
        <a href="https://playwright.dev/docs/api/class-pageassertions#page-assertions-to-have-url"
          >expect(page).toHaveURL()</a
        >
      </td>
      <td align="left">페이지에 해당하는 URL 검증</td>
    </tr>
    <tr>
      <td align="left">
        <a
          href="https://playwright.dev/docs/api/class-apiresponseassertions#api-response-assertions-to-be-ok"
          >expect(apiResponse).toBeOK()</a
        >
      </td>
      <td align="left">API Response의 성공 여부 검증</td>
    </tr>
  </tbody>
</table>

### 그룹화(describe)
테스트 파일에 많은 수의 테스트 함수가 작성되어 있는 경우, 연관된 테스트 함수들을 그룹화 할 수 있습니다.
- 정리된 코드들로, 가독성이 향상됩니다.
- 데이터를 통해 관리가 용이하여 산출물(HTML, Excel)에서 그룹화된 테스트를 확인 할 수 있습니다.

## 정리
위 개념들을 토대로 간단한 예제를 살펴보겠습니다.
```javascript
// 1
function subtractAb(a, b) {
	return a - b
}
// 2
expect(subtractAb(10, 7)).toBe(3);
// 3
test.describe('Todo Page ', () => {
  test('check page title', async ({ page }) => {
		await page.goto('http://localhost:3333/guide/samp/el-todo')
		await expect(page.getByText('data-test-page-title')).toContainText("new page title");
  })
})
```

1. a 에서 b를 빼는 **subtractAb** 함수를 선언
2. expect(Assertion) API를 사용하여 10-7이 3이 맞는지 검증하는 단위 테스트.
3. `Todo Page`그룹 하위 테스트 `check page title`에서 페이지를 이동하고, 페이지 제목이 `new page title`인지 확인하는 E2E 테스트

# Advanced

## 테스트 도입에 대한 개발자 관점
### 결국 QA, 개발팀의 검수가 필요하지 않을까?
당연히 인간의 QA는 필수입니다. 하지만 수동/자동화 테스트코드는 완전한 교집합이 아닙니다.    
클라이언트 요구사항에 적합한지등 다양한 면에서,  
QA 테스트가 월등하지만 다음과 같은 한계가 있습니다.

### 변수 시나리오 Chaining에 대한 제한

예로 Cloud 사진관리에 대한 구현을 가정 하였을때  
1.  사진첩동기화  설정을 해둔 기기에서 사진을 기기에 저장 하였을때 원격 저장소 반영여부 확인
2. 곧 바로 네트워크 연결을 종료하고 해당 사진 삭제 
3. 다시 네트워크 연결 후 1분(또는 threshold)이내 원격저장소 동기화 여부확인
위 목록을 엑셀로 관리하고 매번 다른 인원의 테스트 하였을때 누락 될 가능성이 있습니다.

또한 위 2번 이후, 3번 항목이 변경되는 변수(ex 네트워크상태를 나타내는 텍스트 확인 테스트)를 10개로 가정하였을때,  
매 배포마다 진행해야 할 테스트 케이스는 10의 배수로 증가합니다.  
이처럼 유저 시나리오 관점의 테스트는 왠만한 QA테스트 만으로는 제한이 있습니다.
![screenshot_2023-06-01_at_10.28.49_am.png](/screenshot_2023-06-01_at_10.28.49_am.png)


###  리소스에 대한 보장의 어려움
	QA 테스트시 개발자 도구를 통해 ram 메모리 환경등 컴퓨팅 리소스를 낮추는 등의 설정이 가능하지만,  
	코드 자체에 대한 검증은 어렵습니다.
아래 예제를 버전 1.0.2의 사진을 저장하는 코드로 가정하겠습니다.
```typescript
// src/store/user.js
export const useAuthStore = defineStore("auth", () => {
  const unsubscribe = observeUser((act) => {
    if(act.behavior === 'savePicture') {
      onSavePicture(act.picture)
    }
  })
  async function userChange() {
    savePicture = true
    onSavePicture(act.picture)
  }
  async function onSavePicture(picture: File){
    if (await isValidPicture(picture)) {
      savePicture(picture)
    }
  }
}
```
위 코드는 유저의 행동을 감지하여, 사진을 저장한경우 유효성검사와 데이터를저장을 하는 역할입니다.

isValidPicture은 살인, 자살, 욕설등의 유해성 콘텐츠를 감지하는 API로 이용료는 장당 1원입니다.  

savePicture은 이미지 편집 API를 이용 기기 사이즈에 맞게(400, 800, 1200, 2400)px 총 4장으로 편집하는 API로 장당 1원  

그밖에 클라우드 함수일 경우 호출당, NoSQL DB일 경우 문서 저장 당, 추가로 저장시 구동되는 워크플로우가 있을 수 있습니다.  

아래는 버전 1.0.3의 다른 팀원의 머지되어버린 PR 입니다.
```typescript
...
// src/user/store/preference.js
const unsubscribeAuth = authStore.$onAction(
  ({ name, store, args, after, onError }) => {
    after(async () => {
      if (name === 'userChange' && store.state.savePicture) {
        savePicture(store.state.picture)
      }
    });
  },
  true
);
```
새로온 팀원이 userStore 의 action들을 subscribe 하던 store는 savePicture를 중복으로 호출하여,  

리소스를 낭비하는 코드를 작성 해버렸습니다.  

평소 보다 배수로 뛴 API 요금에 기겁하고 디버깅한 결과 원인을 발견, Fix(savePicture) 커밋까지.. 해결 했습니다.  

분명 유저의 사진저장 인터랙션이 진행되고 3초후 onSavePicture의 호출횟수를 테스트 했다면, 빠른 발견이 가능 했을겁니다.  


## 클라이언트 관점
### 클라이언트는 기술을 가진 회사를 신뢰합니다.
- 규모가 큰 회사 일수록 더욱 중요시 생각하는 __소프트웨어 테스트 자동화__ 기술은 소유한 업체에 대하여 각종 포트폴리오, 디자인등 문서에 더하여 큰 선정 고려요소이자, 신뢰를 제공 할 수 있는 대표적인 방법 중 하나입니다.


### 클라이언트는 산출물이 필요합니다.
- 개발업체를 선정하는 부분에 있어, 업체 별 산출물의 정리과정중 __소프트웨어 테스트__ 관련 문서는 고려대상이 아닐 수 없습니다.
클라이언트 입장에서, 테스트를 전적으로 우리회사에게 맡기는 경우는 거의 존재하지 않습니다.
각 회사는 개발팀부터 QA팀, PM, PL까지 많은 인력 소모를 감수하여, 매 배포시 테스트를 진행합니다.
우리는 __playwright__ 의 [reporter](#reporter) 기능을 통해,
고객에 맞는 산출물을 제공 할 수 있습니다.


### 결국 신뢰를 얻습니다.
**처음** 파트너쉽을 맺은 경우, 신중한 클라이언트들은 테스트의 결과를 믿지 못할 수 있습니다.
지속적인 검증을 통해 점차 테스트 결과서를 **신뢰하고**, 신뢰된 산출물을 바탕으로 소통 할 수 있다는 것은
- 커뮤니케이션 입장에서 매우 **효율적이고 안정적인 업무**가 가능합니다.
- 장기적인 파트너쉽 유지에 도움이 됩니다.

# Refer
- https://playwright.dev/docs/api/class-playwrightassertions#playwright-assertions-expect-generic
- https://playwright.dev/docs/test-assertions
- https://playwright.dev/docs/api/class-genericassertions
- https://doong-jo.github.io/posts/front-end_testing_strategy/

# 적용 가능 개발 방법론
## TODO XP(Extreme Programming)
## TDD(Test Driven Development)
소프트웨어가 완전히 개발되기 이전에 테스트 목록을 작성하는 프로세스.
먼저 자동화된 테스트코드를 작성이후 테스트를 통과하기 위한 소프트웨어를 개발하는 개발방식으로,
익스트림 프로그래밍과 반대되는 개념입니다.

### 개발주기
1. 테스트 추가
새로운 기능 추가는 사양 충족시 통과하는 테스트를 작성하는 것으로 시작합니다.
코드를 작성하기 이전 요구사항에 집중 할 수 있습니다.
2. 테스트 실행 및 실패확인
테스트를 통과하기 위해  새로운 코드가 필요함을 나타내고, 테스트 도구가 올바르게 작동하는지 확인해야합니다.
3. 새 테스트를 통과하는 코드 작성
새로운 기능을 추가하여 테스트를 통과하는지 확인합니다.
4. 기존 모든 테스트를 통과 해야합니다.
기존 테스트목록을 포함 모든 테스트가 통과 할 때까지 새 코드를 수정합니다.
이는 새로운 코드가 요구사항을 만족하며, 사이드이펙트를 발생하지 않음을 나타냅니다.
5. 리팩터링 및 테스트
필요시 가독성과 유지보수성을 위한 리팩터링을 진행, **4번** 과정을 반복합니다.
## Ref
- https://en.wikipedia.org/wiki/Test-driven_development#:~:text=Test%2Ddriven%20development%20(TDD),software%20against%20all%20test%20cases
- https://en.wikipedia.org/wiki/Behavior-driven_development
- https://portal.netobjectives.com/articles-public/test-driven-development-atdd-and-utdd/
- https://en.wikipedia.org/wiki/Extreme_programming
