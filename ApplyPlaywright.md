# Playwright Vue 현업 도입 가이드
테스트 Convention, 산출물, 현업용 가이드로 구성된 글입니다.

- [Playwright Vue 현업 도입 가이드](#playwright-vue-현업-도입-가이드)
  - [시작하기 전에](#시작하기-전에)
    - [소프트웨어 테스트가 처음이라면](#소프트웨어-테스트가-처음이라면)
    - [Playwright 가 처음이시라면](#playwright-가-처음이시라면)
  - [기본 테스트 파일 구조](#기본-테스트-파일-구조)
  - [산출물(스크린샷) 제공 방법](#산출물스크린샷-제공-방법)
    - [결과물](#결과물)
    - [참고문서](#참고문서)
  - [테스트 자동화 우선순위](#테스트-자동화-우선순위)
    - [1. 산출물을 우선하여 구현하십시오.](#1-산출물을-우선하여-구현하십시오)
      - [1.1 참조 산출물 목록](#11-참조-산출물-목록)
    - [2. 단순하지만 오래 걸리는 작업을 선정](#2-단순하지만-오래-걸리는-작업을-선정)
    - [3.  위험도/복잡도 기반 우선순위 결정](#3--위험도복잡도-기반-우선순위-결정)
- [적용 가능 개발 방법론](#적용-가능-개발-방법론)
  - [TODO XP(Extreme Programming)](#todo-xpextreme-programming)
  - [TDD(Test Driven Development)](#tddtest-driven-development)
    - [개발주기](#개발주기)
  - [테스트 스타일 가이드](#테스트-스타일-가이드)




## 시작하기 전에
아래 링크를 기반으로 작성된 문서입니다.
### 소프트웨어 테스트가 처음이라면
- [프론트엔드 테스팅 기본](https://wiki.abacussw.co.kr/ko/technote/frontend/test)
### Playwright 가 처음이시라면 
- [Playwright 기본](https://wiki.abacussw.co.kr/ko/technote/frontend/vue/playwright)
## 기본 테스트 파일 구조
    - 각 폴더 및 파일명은 kebab-case로 작성되어야 합니다.
    - 테스트 프레임워크는 spec.ts 파일 확장자를 기준으로 구별합니다.  

**예시**
```bash
/playwright.config.ts # 테스트 최상위 레벨 옵션
/test/
  ├── tester.ts # 픽스처, 커스터마이징된 테스트 객체
  ├── testConfig.ts # 테스트 설정
  ├── e2e/ # E2E 테스트 폴더
  │  └── login.spec.ts # 로그인 페이지
  │  └── about.spec.ts # 소개 페이지
  │  └── {service}/ # 서브 페이지
  │     └── about.spec.ts # 소개 페이지
  │  └── user/ # 유저 서비스
  │     └── {id}.spec.ts # 유저 상세 페이지
  │     └── me.spec.ts # 마이 페이지
  ├── unit/ # 단위 테스트 폴더
  │   ├── {service}/ 
  │   ├── user # 유저 서비스 
  │     └── info.spec.ts # 유저 정보 생성, 수정 기능 테스트
  │   ├── authentication.spec.ts  # 유저 인증 기능 테스트
```

## 산출물(스크린샷) 제공 방법
1. 저장 관련 설정을 명시하십시오.
    ```ts
    // test/testConfig.ts

    export default {
      recordPath: 'records',
      saveRecord: true,
    }
    ```
2. 저장 위치를 반환하는 함수를 작성하십시오.
    ```ts
    // test/tester.ts
    import testConfig from './testConfig'

    const getRecordDir = (testInfo: TestInfo) => {
      const path = `${testConfig.recordPath}/${testInfo.titlePath.slice(1).join('/')}`
      return path
    ```
3. 전역 테스트에 사용될 hook과 fixture를 생성 하십시오.
    ```ts
    // test/tester.ts
    import { test as base } from '@playwright/test'

    base.afterEach(async ({ page }, testInfo) => {
      if (!testConfig.saveRecord)
        return
      const env = testInfo.project.name // webkit, firefox...
      // 테스트 after 스크린샷을 저장합니다.
      await page.screenshot({ path: `${getRecordDir(testInfo)}/after-${env}.jpeg`, type: 'jpeg', scale: 'css' })
    })

    interface IMyFixtures {
      screenshotBefore(): Promise<void>
    }

    export const test = base.extend<IMyFixtures>({
      screenshotBefore: async ({ page }, use, testInfo) => {
        await use(async () => {
          if (!testConfig.saveRecord)
            return
          await page.screenshot({ path: `${getRecordDir(testInfo)}/before-${testInfo.project.name}.jpeg`, type: 'jpeg', scale: 'css' })
        })
      },
      testConfig,
    })
    ```

4. 각 테스트 케이스의 before 기준을 선정하여 사용하십시오.
    ```ts
    // test/e2e/todo/example.spec.ts
    const MAIN_ROUTE = 'http://localhost:3333/guide/samp/el-todo'
    test.describe('할일 생성,읽기,수정,삭제 테스트', () => {
      test.beforeEach(async ({ page, pushAnnotation, screenshotBefore }) => {
        await page.goto(MAIN_ROUTE) // 매 테스트가 시작 되기 전 메인페이지로 이동합니다.
        await page.waitForSelector('[data-test-id="todo-table"]') // 할 일 테이블이 렌더링 될 때 까지 대기합니다.
        await screenshotBefore() // 테스트 before 스크린샷을 저장합니다.
      })

```
### 결과물
[**파일목록**] 
![screenshot-after-before.png](/성필/playwright/screenshot-after-before.png)

[**스크린샷 before**]
![screenshot-before.png](/성필/playwright/screenshot-before.png)

[**스크린샷 after**]
![screenshot-after.png](/성필/playwright/screenshot-after.png)


## 산출물(엑셀) 제공 방법
1. 테스트 결과를 엑셀로 표시 할 수 있는 사내제작, xlsx 패키지를 설치합니다.  
```bash
pnpm install -D playwright-excel-reporter xlsx@https://cdn.sheetjs.com/xlsx-0.19.3/xlsx-0.19.3.tgz
```
2. excel reporter를 playwright에 등록합니다.
```ts
// playwright.config.ts
export default defineConfig({
  ...,
  reporter: [
    ['html', {
      outputFolder: 'playwright-result-html',
      outputFile: 'result.html',
    }],
    ['playwright-excel-reporter', {
      // 결과가 기록될 엑셀 템플릿 파일, undefined 일 경우 새로운 파일을 생성합니다.
      excelInputPath: 'test/asset/unit-test-case.xlsx', 
      // 엑셀 파일의 시트이름
      caseSheetName: '블라인드',
      // 엑셀 파일의 시트에서 결과 기록이 시작될 행 번호
      excelStartRow: 5,
      // 테스트 결과가 저장될 경로, 파일명
      excelOutputDir: 'excel-reporter-result',
      excelOutputFileName: 'result.xlsx',
    } as Partial<IExcelConfig>],
  ],
})
```
3.1 (Optional) 추가 테스트 카테고리 분류
커스텀 test 객체에 Fixture로 Annotation을 등록하여 사용합니다.
```ts
// test/tester.ts
import { test as base } from '@playwright/test'

// 카테고리 타입 정의
export enum AnnotationType {
  MAIN_CATEGORY = 'MAIN_CATEGORY',
  SUB_CATEGORY1 = 'SUB_CATEGORY1',
  SUB_CATEGORY2 = 'SUB_CATEGORY2',
  SUB_CATEGORY3 = 'SUB_CATEGORY3',
}
// Fixture 등록
interface IMyFixtures {
  pushAnnotation(type: AnnotationType, description: string): void
}
export const test = base.extend<IMyFixtures>({
  pushAnnotation: async ({ page: _ }, use) => {
    await use((type, description) => {
      // https://playwright.dev/docs/test-annotations#custom-annotations
      base.info().annotations.push({ type, description })
    })
  }
})
```
3.2 분류된 테스트코드 작성
```ts
// test/e2e/todo/example.spec.ts

test.describe('할일 생성,읽기,수정,삭제 테스트', () => {
  // 테스트 그룹의 테스트가 시작되기전 훅 등록
  test.beforeEach(async ({ page, pushAnnotation, screenshotBefore }) => {
    // 테스트 카테고리 명시
    pushAnnotation(AnnotationType.MAIN_CATEGORY, 'UI 프레임워크')
    pushAnnotation(AnnotationType.SUB_CATEGORY1, 'TODO 관리')
    ...
  })
})
```
### 결과물
**[파일목록]**
![screenshot_2023-06-12_at_10.59.10_am.png](/screenshot_2023-06-12_at_10.59.10_am.png)
**[시트 데이터]**
![screenshot_2023-06-12_at_11.00.40_am.png](/screenshot_2023-06-12_at_11.00.40_am.png)

### 참고문서
- https://www.npmjs.com/package/playwright-excel-reporter
- https://playwright.dev/docs/test-reporters


## 테스트 자동화 우선순위

테스트의 종류는 무수히 많습니다.  
우리는 자동화 테스트 구축에 있어 **최소한**의 비용으로 효율적으로 구축 할 수 있어야 합니다.  
다음 항목들을 기준으로, 우선순위 작업들을 선정하십시오.  

### 1. 산출물을 우선하여 구현하십시오.
신뢰는 클라이언트로부터, 우리의 자신감 또한 클라이언트로부터 나옵니다.
클라이언트의 산출물 가장 우선하여 완성하고, 이 목록들만큼은 지켜내야 원만한 관계를 유지 할 수 있습니다.

#### 1.1 참조 산출물 목록
1. 통합 테스트 시나리오 문서
2. 단위 테스트 케이스 문서
3. 요구사항 정의서
4. 리스크 관리대장

### 2. 단순하지만 오래 걸리는 작업을 선정
만약 유저 권한변경시 1분이내 적용 여부를 테스트 해야 할 때
1. 윈도우1) 유저1 로그인 (접속중..)
2. 윈도우2) 관리자 권한 로그인 
3. 윈도우2) 유저1 권한 변경
4. 윈도우1) 유저1 1분이내 권한변경 확인

위 작업은 수동 테스트로 하기에 오래 걸리는 작업입니다.  
우리는 자동화 테스트로 작성하여 위 문제를 해결 할 수 있습니다.

### 3.  위험도/복잡도 기반 우선순위 결정

[관련 링크](https://uzooin.tistory.com/185)
- 발생 가능성: 복잡도/난이도/크기/개발자의 수준을 기준으로 판단하십시오.
- 발생시 심각도: 랜딩 페이지에서 문제가 발생할 경우 사용자 이탈률이 발생할 수 있습니다.   
  이와같이 발생시 가장 치명적인 기능을 우선순위로 작성하십시오.



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


## 테스트 스타일 가이드
- 테스트는 작고 증분적이어야 하며 자주 커밋하십시오.  
    새코드가 일부 테스트에 실패하면, 과도한 디버그 대신 간단히 실행 취소 또는 되돌릴 수 있습니다.
    작은 테스트는 모듈화가 가능하고, 읽고 이해하기 쉽습니다.

- 테스트의 속도를 고려하여 개별 Time out 을 적용하십시오.  
전체 타임아웃은 낮게 잡되 테스트 결과의 위음성(거짓음성)을 방지하기 위해 오래 걸리는 테스트는 개별 타임아웃을 적용 하십시오.
  ```ts
  // playwright.config.ts
  export default defineConfig({
    // 최상위 timeout을 3초로 정의
    timeout: 1000 * 3,
    ...
  ```
  ```ts
  // test/e2e/todo/example.spec.ts

  // 테스트 케이스 필터링을 위한 태그를 작성합니다.
  // https://playwright.dev/docs/test-annotations#tag-tests
  test('할 일 테이블 체크박스 수정 케이스 @slow', async ({ page }) => {
    // 기존 timeout의 3배를 허용하는 playwright API
    // https://playwright.dev/docs/api/class-testinfo#test-info-slow-1
    test.slow()
    ...
  ```
- 테스트간 종속성을 가지지 않아야합니다.  
테스트 목록의 실행 순서와 관계없이, 각 테스트는 고유의 상태를 가지고 있어야합니다.
상호의존적인 테스트는 계단식 위음성의 발생과 디버그, 관리의 어려움을 유발합니다.  

- 필요 이상의 동작을 테스트하는 코드를 작성하지 마십시오.    
일반적으로 오류는 복잡한 프로젝트 전체에서 미묘하게 발생합니다.  
정확한 에러 발생지점을 알기 위해 작은 테스트로 나누어 작성하십시오.
