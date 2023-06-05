# Playwright 시작하기
완벽한 어플리케이션을 제작하기 위한 개발자.  
우리 프론트엔드 개발자들을 위한 문서입니다.
- [Playwright 시작하기](#playwright-시작하기)
- [왜 Test, Playwright를 써야할까?](#왜-test-playwright를-써야할까)
  - [수동으로 모든 테스트를 충족 시킬 수 없다.](#수동으로-모든-테스트를-충족-시킬-수-없다)
  - [그렇다면 도입시 어떤 가치를 얻을 수 있을까?](#그렇다면-도입시-어떤-가치를-얻을-수-있을까)
    - [도입시 예상되는 업무의 변화](#도입시-예상되는-업무의-변화)
- [Playwright란?](#playwright란)
  - [시작하기](#시작하기)
    - [로컬환경에서 테스트 코드 작성하기](#로컬환경에서-테스트-코드-작성하기)
  - [결론](#결론)
  - [Playwright 특징 목록](#playwright-특징-목록)
    - [1. Test generator](#1-test-generator)
    - [2. Reporter](#2-reporter)
    - [3. Debugging](#3-debugging)
    - [4. API 테스트](#4-api-테스트)
      - [위 내용은 API 목업/프록시 테스트 또한 가능하다는 말과 같습니다.](#위-내용은-api-목업프록시-테스트-또한-가능하다는-말과-같습니다)
    - [5. Authenticate](#5-authenticate)
    - [6. Http Auth를 위한 예제](#6-http-auth를-위한-예제)
    - [7. Trace viewer](#7-trace-viewer)
    - [8. Inspector](#8-inspector)
    - [9. 경량성](#9-경량성)
    - [10. 폭넓은 렌더링 엔진을 지원](#10-폭넓은-렌더링-엔진을-지원)
    - [11. 실험적 기능인 컴포넌트 테스팅](#11-실험적-기능인-컴포넌트-테스팅)
    - [12. Annotations](#12-annotations)
      - [예시 1) 파이어 폭스 브라우저 환경에서 테스트 skip을 목적으로 하는 테스트.](#예시-1-파이어-폭스-브라우저-환경에서-테스트-skip을-목적으로-하는-테스트)
      - [예시 2) 테스트에 태그를 추가하여 필터링된 테스트 케이스를 실행.](#예시-2-테스트에-태그를-추가하여-필터링된-테스트-케이스를-실행)
      - [예시 3) 사용자 설정된 주석으로 테스트 메타 데이터 관리](#예시-3-사용자-설정된-주석으로-테스트-메타-데이터-관리)
    - [13. Videos](#13-videos)
      - [Refer](#refer)
- [사내 프로젝트 적용 방법](#사내-프로젝트-적용-방법)
  - [프로젝트 시작 전](#프로젝트-시작-전)
  - [프로젝트 진행](#프로젝트-진행)
  - [어떻게 효율적으로 테스트코드를 작성할 수 있을까](#어떻게-효율적으로-테스트코드를-작성할-수-있을까)
    - [1. 산출물을 우선하여 구현하십시오.](#1-산출물을-우선하여-구현하십시오)
    - [2. 앱의 메인 기능에 집중하라!](#2-앱의-메인-기능에-집중하라)
    - [3. 단순하지만 오래 걸리는 작업을 선정하라!](#3-단순하지만-오래-걸리는-작업을-선정하라)
    - [4.  위험도/복잡도 기반 우선순위 결정](#4--위험도복잡도-기반-우선순위-결정)
- [Advanced](#advanced)
  - [테스트 도입에 대한 개발자 관점](#테스트-도입에-대한-개발자-관점)
    - [1. 결국 QA팀, 개발팀의 검수가 필요하지 않을까?](#1-결국-qa팀-개발팀의-검수가-필요하지-않을까)
    - [2.  변수 시나리오 Chaining에 대한 제한](#2--변수-시나리오-chaining에-대한-제한)
    - [리소스에 대한 보장의 어려움](#리소스에-대한-보장의-어려움)
  - [클라이언트 관점](#클라이언트-관점)
    - [클라이언트는 기술을 가진 회사를 신뢰합니다.](#클라이언트는-기술을-가진-회사를-신뢰합니다)
    - [클라이언트는 산출물이 필요합니다.](#클라이언트는-산출물이-필요합니다)
    - [결국 신뢰를 얻습니다.](#결국-신뢰를-얻습니다)
  - [그래서 왜 Playwright?](#그래서-왜-playwright)
- [5. Refer](#5-refer)


# 왜 Test, Playwright를 써야할까?
> 벽에 페인트를 던져 많은 부분의 벽을 칠할 수 있겠지만 브러시를 들고 벽에 오르지 않으면 모서리는 절대 칠하지 못할 것입니다.  

**수동테스트**로 많은 테스트를 어느 정도의 확신과 진행 할 수 있겠지만 **자동화 테스트** 없이는 절대 서비스 전체를 감출 순 없을 것입니다.

<br />

모든 개발자는 프로젝트가 커지면 커질수록 수정된 적은 양의 코드가 전체 프로젝트에 미칠 영향을 걱정합니다. 이에 **Playwright**는 우리에게 확신을 줍니다. 
>"너의 코드는 문제없어, 내가 보장할게."

<br />

대부분의 개발자들은 테스트 코드를 작성해야 하는 것을 너무나 잘 알고있습니다.  
그리고 빠듯한 일정에 대부분 도입을 주저합니다. 
**Playwright**는 코드 작성 자동화를 통해 편리함을 제공합니다.

<br />

> "페이지 좀 보자, 코드는 내가 만들게"

<br />


## 수동으로 모든 테스트를 충족 시킬 수 없다.
<br />

테스트 자동화가 필요한 이유는 매 배포마다 수백 줄에 달하는 **단위테스트케이스목록** 을 수동으로 테스트하기에 한계가 있기 때문입니다.  

-  테스트: **난 완벽주의 개발자!**  자부심을 갖고 꼼꼼하게 테스트합니다.
- 두 번째 테스트: **종일 테스트할 수 있지** 지치지 않습니다. 테스트합니다. 

  ......

-  19 번째 테스트: ~~"input element 하나 추가한 건데 해야 해?.."~~ 테스트를 하긴 합니다.

<br />

## 그렇다면 도입시 어떤 가치를 얻을 수 있을까?
<br /> 

1. 아예 수동 테스트를 진행하지 않을 수 있다.  
프로젝트시 우리는 개발환경을 분리합니다. (개발, 베타, 출시)버전  
다음과 같이 선택 할 수 있습니다.
   - "수동, 자동화 테스트는 **베타** 이상" 
  
   - **이전버전**은 자동화 테스트만을 이용해 검증."

2. 다양한 사용자 환경에서 테스트를 할 수 있다.  
매 배포, 모든 시나리오에 대해 Chrome, Firefox, IPhone등 
다양한 사용자 환경에서 테스트 할 수 있습니다.

### 도입시 예상되는 업무의 변화
<br /> 

만약 클라이언트로 부터 카드 element 주위에 공백을 추가 해달라는 요구사항을 받았다면  
다음과 같이 코드를 수정 할 수 있습니다.  

```html
<div class="card" />
<div class="card" />
<style>
  .card {
    margin: 0.5rem
  }
</style>
```

테스트 코드가 작성되어 있다면, 우리는 단 두 단계로 이슈를 해결 할 수 있습니다.
1. 전체 어플리케이션 테스트 실행  
  `$ pnpm run test `
1. 개발계 브랜치 병합 이슈 해결  

그렇다면 어떻게 자동화 테스트를 도입 할 수 있을까요?  
**Playwright란** 무엇인지, 위 내용들을 **충족** 하는지 직접 확인해보겠습니다.

<br />  

# Playwright란?
Playwright는 웹 애플리케이션 테스트 및 자동화를 위한 오픈 소스 도구입니다.  
브라우저(Chrome, Firefox, Safari 등)를 제어하고   
사용자의 행동(클릭, 키 입력, 네비게이션 등)을 시뮬레이션, 테스트하는 기능을 제공합니다.

<br />

## 시작하기
<br />

1. 다음 명령어를 사용하여 vue 프로젝트를 생성합니다. 
    ```bash
    $ git clone git@github.com:socketbear/vue-dev-guide.git
    ```
2. `$ pnpm dlx create-playwright` 를 입력하여 설치합니다.
    ```
    ✔ Where to put your end-to-end tests? · test/e2e
    ✔ Add a GitHub Actions workflow? (y/N) · false
    ✔ Install Playwright browsers (can be done manually via 'pnpm exec playwright install')? (Y/n) · true
    ```
    - e2e 테스트 경로는 `test/e2e`로 설정합니다
    - Github Action 워크플로우는 설정하지 않습니다.
    - 처음 설치한 경우 테스트 브라우저 엔진은 설치하지 않습니다.


    ### 설치중 문제가 발생하였나요? 
    리눅스(Ubuntu) 환경이라면 패키지 의존성 관련 에러가 발생 할 수 있습니다
    > https://github.com/microsoft/playwright/issues/13738
    ``` bash
    $ pnpm exec playwright install --with-deps
    or
    $ npx playwright install --with-deps
    ```
    그럼에도 문제가 발생 할 경우, [공식 설치페이지](https://playwright.dev/docs/intro#installing-playwright)를 참고 하십시오.


3. 설치 완료 확인을 위해 파일목록을 확인하세요.
   - 추가된 파일
      ```
      playwright.config.ts
      test/e2e/
      tests-examples/
      ```
    - 수정된 파일
      ```
      .gitignore
      package.json
      pnpm-lock.yaml
      ```

4. vscode 에디터인경우 [익스텐션 설치](https://playwright.dev/docs/getting-started-vscode)를 참고해주세요. (하단 익스텐션 설치 완료시 화면)
<br />
![screenshot_2023-06-01_at_1.15.40_pm.png](/성필/screenshot_2023-06-01_at_1.15.40_pm.png)

5. package.json 파일의 scripts 프로퍼티에 아래 명령어를 추가 하십시오.
    [관련문서](https://playwright.dev/docs/running-tests)
    ```json
        "test:e2e": "pnpm exec playwright test",
        "test:e2e:debug": "pnpm exec playwright test --debug",
        "test:e2e:report": "pnpm exec playwright show-report",
        "test:e2e:ui": "pnpm exec playwright test --ui",
        "test:e2e:gen": "pnpm exec playwright codegen",
    ```
    1. `pnpm run test:e2e:ui` 를 실행하면 아래 사진과 같이 윈도우를 확인할 수 있습니다.
    ![playwright-ui-home.png](/성필/playwright-ui-home.png)
    2. 위사진의 Run 버튼을 눌러주세요.
    아래와 같이 뜬다면, **축하합니다!** 당신은 테스트 코드의 실행을 완료한 것입니다!
    ![playwright-ui-allapssed.png](/성필/playwright-ui-allapssed.png)

### 로컬환경에서 테스트 코드 작성하기
<br />

1. `playwright.config.ts` 파일을 열어 아래 옵션들을 추가합니다.
    ```typescript
    {
      use: {
        /* Maximum time each action such as `click()` can take. Defaults to 0 (no limit). */
        // actionTimeout: 0,
        /* Base URL to use in actions like `await page.goto('/')`. */
        baseURL: 'http://localhost:3333',
        /* Only on CI systems run the tests headless */
        headless: !!process.env.CI,
        /* Collect trace when retrying the failed test. See https://playwright.dev/docs/trace-viewer */
        trace: 'on-first-retry',
      },  
      webServer: {
        /**
         * Use the dev server by default for faster feedback loop.
        * Use the preview server on CI for more realistic testing.
        Playwright will re-use the local server if there is already a dev-server running.
        */
        // command: process.env.CI ? 'vite preview --port 3333' : 'vite dev',
        command: process.env.CI ? ' pnpm run preview --port 3333' : 'vite dev',
        port: 3333,
        reuseExistingServer: !process.env.CI,
      },
    }
    ```
<br />

2. `$ pnpm run dev` 명령어로 로컬 서버를 실행시킵니다.

<br />
3. 사진과 같이 vscode 익스텐션에서 경로를 포커싱하여 파일 위치를 지정합니다.


![playwright-extnsion-main.png](/성필/playwright-extnsion-main.png)

4. 하단의 `Record new` 버튼을 클릭합니다.
 
<br />
 
5. 테스트 브라우저의 주소창에 `http://localhost:3333/guide/samp/el-todo` 를 입력합니다.

<br />


6. todo 항목을 입력하고 추가 테스트해 봅니다.

<br />


7. playwright - code generate 기능을 통해 테스트 코드가 생성되었음을 확인하세요
		
    ```javascript
    import { expect, test } from '@playwright/test'

    test('test', async ({ page }) => {
      await page.goto('http://localhost:3333/guide/samp/el-todo')
      await page.getByPlaceholder('TO-DO 항목을 입력해주세요.').click()
      await page.getByPlaceholder('TO-DO 항목을 입력해주세요.').fill('소금빵을 산다')
      await page.getByPlaceholder('TO-DO 항목을 입력해주세요.').press('Enter')
      await page.getByPlaceholder('TO-DO 항목을 입력해주세요.').click()
      await page.getByPlaceholder('TO-DO 항목을 입력해주세요.').fill('밥을 먹는다.')
    })
    ```
8. 좋습니다. 이제 생성된 2개의 todo목록에 대한 검증을 위한 코드를 한 줄 추가하겠습니다.  
    ```javascript
    expect((await page.$$('.data-test-row')).length).toEqual(2)
    ```

<br />

9. 다시 마우스 커서를 test 함수 내부로 위치시킵니다. 

<br />

10. `Record new`하단의 `Record at cursor`를 클릭합니다.

<br />

11.  그리고 todo 데이터를 생성하고, 미완료/완료로 상태변경하는 테스트를 작성 하십시오.


<br />

12.  같은 과정을 반복하여 다음과 같은 코드를 완성 할 수 있습니다.
- 체크박스 상태변경
- todo 데이터 삭제 테스트를 진행 검증코드 추가
- 어려울 경우 아래 코드를 복사하여 붙여 넣으세요


```javascript
import { type Page, expect, test } from '@playwright/test'
// API: https://playwright.dev/docs/writing-tests#navigation

const MAIN_ROUTE = 'http://localhost:3333/guide/samp/el-todo'
test.describe('Todo CRUD ', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(MAIN_ROUTE) // Go to the starting url before each test.
  })
  test('create todo', async ({ page }) => {
    await page.waitForSelector('[data-test-id="todo-table"]')
    await page.screenshot({ path: 'screenshots/todo/before-create.png', fullPage: true })
    await createTwoTodo(page)
    expect((await page.$$('.data-test-row')).length).toEqual(2)
    await page.screenshot({ path: 'screenshots/todo/after-create.png', fullPage: true })
  })
  test('update todo checkbox', async ({ page }) => {
    await createTwoTodo(page)
    await page.getByRole('row', { name: '소금빵을 산다 미완료' }).locator('span').nth(1).click()
    await expect(page.getByRole('row', { name: '소금빵을 산다 미완료' }).locator('label.el-checkbox')).toHaveClass(/is-checked/)
    await page.getByRole('row', { name: '밥을 먹는다. 미완료', exact: true }).locator('span').nth(1).click()
    await expect(page.getByRole('row', { name: '밥을 먹는다. 미완료' }).locator('label.el-checkbox')).toHaveClass(/is-checked/)

    await page.getByRole('row', { name: '소금빵을 산다 미완료' }).locator('span').nth(1).click()
    await expect(page.getByRole('row', { name: '소금빵을 산다 미완료' }).locator('label.el-checkbox')).not.toHaveClass(/is-checked/)
    await page.getByRole('row', { name: '밥을 먹는다. 미완료', exact: true }).locator('span').nth(1).click()
    await expect(page.getByRole('row', { name: '밥을 먹는다. 미완료' }).locator('label.el-checkbox')).not.toHaveClass(/is-checked/)
  })

  test('delete all todo', async ({ page }) => {
    await createTwoTodo(page)
    await page.getByRole('row', { name: '소금빵을 산다 미완료' }).locator('span').nth(1).click()
    await page.getByRole('row', { name: '밥을 먹는다. 미완료' }).locator('span').nth(1).click()
    await page.getByRole('button', { name: '삭제' }).click()
  })
})

async function createTwoTodo(page: Page) {
  await page.getByPlaceholder('TO-DO 항목을 입력해주세요.').click()
  await page.getByPlaceholder('TO-DO 항목을 입력해주세요.').fill('소금빵을 산다')
  await page.getByPlaceholder('TO-DO 항목을 입력해주세요.').press('Enter')
  await page.getByPlaceholder('TO-DO 항목을 입력해주세요.').click()
  await page.getByPlaceholder('TO-DO 항목을 입력해주세요.').fill('밥을 먹는다.')
  await page.getByRole('button', { name: '추가' }).click()
}
```

<br />

13. 명령어를 통해 방금 만들 코드를 실행해 봅시다.
`pnpm run test:e2e test/e2e/test-1.spec.ts`
저런 테스트가 실패하며 Playwright Test Report 타이틀을 가진 사이트가 열립니다.
![screenshot_2023-06-01_at_2.40.35_pm.png](/성필/screenshot_2023-06-01_at_2.40.35_pm.png)

<br />

14. `.data-test-row` class 를 가진 row 목록을 받아오려 했지만 실패했습니다.
**important**: 테스트에 사용될 selector는 반드시 **data-test**를 prefix로 가져야 합니다.

<br />

15. src/guide/pages/samp/el-todo.vue 파일의 el-table 엘리먼트의 속성()을 추가합니다.
_row-class-name="data-test-row 속성 추가_
```
<el-table data-test-id="todo-table" :data="todoList" style="width: 100%" row-class-name="data-test-row">
```

<br />

16. 다시 11번 과정을 테스트 합니다.

<br />

17.  테스트 성공 결과 확인

<br />

18.  screenshots 폴더에서 테스트 중 얻은 스크린샷을 확인합니다.

<br />

## 결론
<br />

지금까지 가이드를 통해, 우리는 다음과 같은 사실을 알 수 있습니다.
- 우리는 **배포/로컬 서버**를 통해 테스트 자동화 기능을 개발 할 수 있다.  

- 기본적인 테스트 코드들을 playwright 를 통해 **자동 생성**할 수 있다.  
- 테스트 결과, 에러정보를 **산출물**로 얻을 수 있다.
- **스크린샷 기능**을 통해, 테스트 케이스 전 후 비교된 산출물을 얻을 수 있다

다음은 Playwright의 기능들에 대해 살펴 보겠습니다.  

---
## Playwright 특징 목록

<br />

### 1. Test generator
    브라우저와 상호작용을 통해 원하는 테스트 코드를 자동생성 할 수 있습니다.  
    TDD 최대 난제 중 하나인 개발비용 단축에 대한 기능이자 핵심기능 중 하나입니다.

아래 명령어를 실행하여, URL 주소에 대한 테스트 생성 기능을 테스트 해보세요.
[관련문서](https://playwright.dev/docs/codegen)
```bash
$ npx playwright codegen {URL}
$ npx playwright codegen --viewport-size=800,600  demo.playwright.dev/todomvc
$ npx playwright codegen --device="iPhone 13" demo.playwright.dev/todomvc
```

~~테스트 커버리지를 계산, 모든 파일에 대한 테스트 파일 생성을 기대했으나... 실패~~


### 2. Reporter
    playwright는 진행된 테스트에 대한 레포트를 다양한 양식으로 지원합니다.  
주요 양식은 다음과 같습니다.
[관련문서](https://playwright.dev/docs/test-reporters)
- HTML
  - 파일(페이지) - 테스트 그룹 - 테스트 케이스로 분류된 목록
  - pass/fail/skip 필터링
  - 검색
- Screenshot
  - 테스트 코드중 설정에 따라 programmatic 또는 자동 으로 테스트 장면을 저장 가능
- JSON/Custom Reporter
  - 엑셀 라이브러리를 이용하여, 커스텀한 엑셀을 생성 및 제공 할 수 있습니다.
  - 그 외 고객의 요구사항에 맞게 커스터마이징한 Reporter 를 제공 할 수 있습니다.
  
### 3. Debugging
    vscode 익스텐션이 설치되어 있다면, 테스트 중 아래 기능들을 사용 할 수 있습니다.
- breakpoint등 (builtin)디버깅 기능들을 사용 할 수 있습니다.
- 실시간 브라우저 윈도우 와 IDE 를 비교하며 에러를 수정 할 수 있습니다.  

### 4. API 테스트
    REST API 통신과 관련된 테스트를 제공합니다.
- E2E 와 별도로 API 테스트를 위해서 HTTP 통신을 통해 서버 테스트가 가능합니다.
- E2E 테스트 도중, 혹은 setup/teardown 훅에서 자유롭게 HTTP 통신을 할 수 있습니다.
- playwright는 모든 네트워크 트래픽에 대한 모니터링, 수정이 가능합니다.  

#### 위 내용은 API 목업/프록시 테스트 또한 가능하다는 말과 같습니다.
```javascript
const browser = await chromium.launch({
  proxy: {
    server: 'http://myproxy.com:3128',
    username: 'usr',
    password: 'pwd'
  }
});
```

[관련문서](https://playwright.dev/docs/api-testing)
### 5. Authenticate
어떤 유저인증 전략이든, 유저 인증 정보를 브라우저 혹은 파일로 저장하게 됩니다.  
`await page.context().storageState({ path: authFile });`

우리는 계정정보를 파일로서 관리하고, 로그인 과정에 사용 할 수 있습니다.
```javascript
    await page.goto('https://github.com/login');
    await page.getByLabel('Username or email address').fill(account.username);
    await page.getByLabel('Password').fill(account.password);
    await page.getByRole('button', { name: 'Sign in' }).click();
    await page.waitForURL('https://github.com/');
    await expect(page.getByRole('button', { name: 'View profile and more' })).toBeVisible();
```
위 코드는 저장된 계정을 통해 로그인하고, 쿠키가 저장된 상태로 홈페이지로의 리다이렉션을 대기하는 테스트 케이스를 작성 할 수 있습니다.
### 6. Http Auth를 위한 예제
```javascript
const context = await browser.newContext({
  httpCredentials: {
    username: 'bill',
    password: 'pa55w0rd',
  },
});
const page = await context.newPage();
await page.goto('https://example.com');
```


### 7. Trace viewer
    Playwright는 테스트 항목들의 로그들을 zip파일로 저장합니다. 
- 인터렉션 로그, 스냅샷(스크린샷), 
- 테스트 소스 코드 ,  
- 네트워크 로그
- 테스트 사양, 환경
- [관련문서](https://playwright.dev/docs/trace-viewer)  
[trace.playwright.dev](https://trace.playwright.dev/) 링크 혹은
아래 명령어를 사용하여, 정보를 확인 할 수 있습니다.  
`$ npx playwright show-trace trace.zip`


### 8. Inspector
    익숙한 Vue Inspector처럼 Playwright 또한 GUI 툴을 제공합니다.

- 클릭등의 인터랙션을 통하여 테스트의 생성, 정지,수정 녹화, 복사, 삭제. 언어변경이가능합니다.
- 브라우저 엘리먼트의 selector를 실시간으로 추출 할 수 있습니다.
- 브라우저 액션에 대한 로그를 확인 할 수 있습니다.

### 9. 경량성
E2E 테스트 라이브러리는 대체로 **무겁고, 느립니다.**  
테스트 브라우저를 설치하고, 매 테스트마다 브라우저 엔진을 재가동, 재 렌더링해야 하기 때문입니다.  
경험상 Cypress를 사용 했었을때 직관적이고 많은 기능을 가지고 있었지만 많은 기능을 가진 프레임워크 특징인  
확장성문제, 커스터마이징 시간소요, 느린 속도로 인해 반드시 구현해야 했던 병렬처리등으로 진행중 삭제한 경험이 있습니다.  
이에 **Playwright**는 cypress 패키지 사이즈 기준 **200배** 경량화된 용량, 훨씬 **빠른 체감속도**로, **최적화**에 많은 노력을 기울이고 있습니다.
`Cypress(4.99 MB) > Nightwatch(webdriver required) > Playwright(24.2 kB)`

### 10. 폭넓은 렌더링 엔진을 지원
1. 크로미움, 웹킷, 파이어폭스, 
2. 윈도우, 리눅스, MacOS
3. headless, headed, 모바일 emulator(chrome for android, safari for ios)
4. [관련 문서](https://playwright.dev/docs/browsers)

### 11. 실험적 기능인 컴포넌트 테스팅
문서 작성일 기준, vite, vue, pinia 에 대한 플러그인, 호환을 지원하지만  
아직 실험적 기능이며, 컴포넌트 테스팅을 도입하기 위해서 추가 테스트가 필요합니다.
[관련문서](https://playwright.dev/docs/test-components)

### 12. Annotations
Playwright는 `skip`, `failures`, `fixme`등 관리 가능한 **주석** 기능을 제공합니다.  
**관리**는 조건 또는 필터를 통한 테스트 실행, 메타 데이터의 관리 가능을 의미합니다.  
- [관련문서](https://playwright.dev/docs/test-annotations)
- 주석은 테스트 혹은 테스트 그룹 일 수 있습니다.
- 사전설정/조건에 따라 동적으로 적용 가능합니다.
<br />

아래 분류 별 예시를 확인하고 상세 내용은 [관련문서](https://playwright.dev/docs/test-annotations)를 참조 하십시오.  
#### 예시 1) 파이어 폭스 브라우저 환경에서 테스트 skip을 목적으로 하는 테스트.
```javascript
test('skip this test', async ({ page, browserName }) => {
  test.skip(browserName === 'firefox', 'Still working on it');
});
```
#### 예시 2) 테스트에 태그를 추가하여 필터링된 테스트 케이스를 실행.
1. `slow` 태그가 추가된 테스트 케이스를 작성합니다.
```javascript
  test('update todo status @slow', async ({ page }) => {
    await createTwoTodo(page)
    await page.getByRole('row', { name: '소금빵을 산다' }).getByRole('button', { name: '미완료' }).click()
    await expect(page.getByRole('row', { name: '소금빵을 산다' })).not.toContainText(/미완료/)
    await expect(page.getByRole('row', { name: '소금빵을 산다' })).toContainText(/완료/)
    await page.getByRole('row', { name: '소금빵을 산다 완료' }).getByRole('button', { name: '완료' }).click()
    await expect(page.getByRole('row', { name: '소금빵을 산다 미완료' })).toContainText(/미완료/)
  })
```
2. 이후 위 태그에 해당하는 테스트만 실행할 수 있습니다.
`npx playwright test --grep @slow`
#### 예시 3) 사용자 설정된 주석으로 테스트 메타 데이터 관리
메타데이터는 key(type)/value(description) 쌍으로 관리되며  
[Reporter](#2-reporter)에서 보여질 수 있습니다.  

### 13. Videos
우린 테스트 항목들에 대한 녹화 기능을 이용할 수 있습니다.
적용 방법은 아래와 같습니다.
용량이 너무 크지 않도록 사이즈를 조절하세요
```javascript
import { defineConfig } from '@playwright/test';
export default defineConfig({
  use: {
    video: {
      mode: 'on-first-retry', 
      size: { width: 640, height: 480 }
    }
  },
});
```
#### Refer
 - https://github.com/microsoft/playwright/issues/10855
 - https://playwright.dev/docs/videos

# 사내 프로젝트 적용 방법
우리는 앞서 테스트의 필요성, Playwright 사용방법 및 특징에 대하여 알아보았습니다.  

어떤 방법으로 테스트를 우리 프로젝트에 효율적으로 적용 시킬수 있을지
우리는 Playwright의 어떤 기능들을 더 이용 할 수 있을지 알아보겠습니다.

## 프로젝트 시작 전
<br />

- 이용중인 [프레임 워크](https://github.com/socketbear/vue-dev-guide)에 설정 및 예시파일을 적용 합니다.
	- playwright.config.ts 
  - tests/unit/example.spec.ts
  - tests/e2e/example.spec.ts


## 프로젝트 진행
<br />

1. 각자 프로젝트의 **클라이언트가** 요구하는 산출물 양식에 따라, [Custom Reporter](https://playwright.dev/docs/test-reporters#custom-reporters)를 제작합니다.
	- 다음은 [builtin](#reporter) 외 제작이 예상되는 리포터 입니다.  
		- xlsx 라이브러리를 이용한 엑셀 리포터
		- 테스트 실패시 이메일, 푸시, 슬랙 알림등을 전송하는 리포터


2. 자동화 테스트로 대체할 테스트 단계와 수동 테스트 QA까지 진행 할 단계를 구분하여 기획합니다.
	- ex ) develop 단계에서는 **신규 기능에 대한 QA** 및 **자동화 테스트**로 진행
  - ex ) staging 이상부터 모든 서비스에 대한 QA 까지 진행



3. 테스트 시나리오 및 코드를 작성합니다.
	- 전체 시나리오에 대한 테스트코드를 자동생성 기능을 이용하여 작성
	- [우선순위](#todo-어떻게-효율적으로-테스트코드를-작성할-수-있을까)에 따라 테스트 코드 완성
  


## 어떻게 효율적으로 테스트코드를 작성할 수 있을까
    테스트의 종류들은 정적 테스트(eslint, typescript), 단위, 통합, e2e, 컴포넌트, smocking, api...  
    너무 많습니다...   

배보다 배꼽이 더 큰 상황, 우리는 자동화 테스트 구축에 있어 **최소한**의 비용으로

테스트 코드를 효율적으로 작성 할 수 있어야 합니다.  

다음 항목들을 기준으로, 우선순위 작업들을 선정하십시오.

### 1. 산출물을 우선하여 구현하십시오.

신뢰는 클라이언트로부터, 우리의 자신감 또한 클라이언트로부터 나옵니다..
클라이언트 관점에서 사용자 요구정의서, 화면 정의서를 가장 우선하여 완성하고
이 목록들만큼은 지켜내야 원만한 관계를 유지 할 수 있습니다.

### 2. 앱의 메인 기능에 집중하라!

모든 서비스는 메인 서비스가 있고, 타겟층이 있습니다.
예로 클라우드 사진 저장소 서비스(구글포토)를 제작한다면
- 메인 서비스: 사진 관리(CRUD)
- 타겟층: 10 ~ 40대 여성
10 ~ 40대 여성이 많이 사용하는 환경(아이폰 최신형, 14인치 노트북, RAM: 2~4GB)  
에서 사진관리에 대한 테스트를 우선 개발해야 합니다.


### 3. 단순하지만 오래 걸리는 작업을 선정하라!

만약 유저 권한변경시 1분이내 적용 여부를 테스트 해야 할 때
1. 윈도우1) 유저1 로그인 (접속중..)
2. 윈도우2) 관리자 권한 로그인 
3. 윈도우2) 유저1 권한 변경
4. 윈도우1) 유저1 1분이내 권한변경 확인

위 작업은 수동 테스트로 하기에 오래 걸리는 작업입니다.  
우리는 자동화 테스트로 작성하여 위 문제를 해결 할 수 있습니다.

### 4.  위험도/복잡도 기반 우선순위 결정

[관련 링크](https://uzooin.tistory.com/185)
- 발생 가능성: 복잡도/난이도/크기/개발자의 수준을 기준으로 판단하십시오.
- 발생시 심각도: [앱의 메인 기능](#앱의-메인-기능에-집중하라)이나 랜딩 페이지에서 문제가 발생할 경우  
  기하급수적인 사용자 이탈률이 발생할 수 있습니다.

<br />

# Advanced

<br />

## 테스트 도입에 대한 개발자 관점

<br />

### 1. 결국 QA팀, 개발팀의 검수가 필요하지 않을까?

당연히 인간의 QA는 필수입니다. 하지만 수동/자동화 테스트코드는 완전한 교집합이 아닙니다.    
클라이언트 요구사항에 적합한지등 다양한 면에서,  
QA 테스트가 월등하지만 다음과 같은 한계가 있습니다.

<br />

### 2.  변수 시나리오 Chaining에 대한 제한

예로 Cloud 사진관리에 대한 구현을 가정 하였을때  
1.  사진첩동기화  설정을 해둔 기기에서 사진을 기기에 저장 하였을때 원격 저장소 반영여부 확인
2. 곧 바로 네트워크 연결을 종료하고 해당 사진 삭제 
3. 다시 네트워크 연결 후 1분(또는 threshold)이내 원격저장소 동기화 여부확인
위 목록을 엑셀로 관리하고 매번 다른 인원의 테스트 하였을때 누락 될 가능성이 있습니다.

또한 위 2번 이후, 3번 항목이 변경되는 변수(ex 네트워크상태를 나타내는 텍스트 확인 테스트)를 10개로 가정하였을때,  
매 배포마다 진행해야 할 테스트 케이스는 10의 배수로 증가합니다.  
이처럼 유저 시나리오 관점의 테스트는 왠만한 QA테스트 만으로는 제한이 있습니다.
![screenshot_2023-06-01_at_10.28.49_am.png](/screenshot_2023-06-01_at_10.28.49_am.png)

<br />

###  리소스에 대한 보장의 어려움

QA 테스트시 개발자 도구를 통해 ram 메모리 환경등 컴퓨팅 리소스를 낮추는 등의 설정이 가능하지만,  
코드 자체에 대한 검증은 어렵습니다.
아래 예제를 버전 1.0.2의 사진을 저장하는 코드로 가정하겠습니다.
```typescript
// src/store/user.ts
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
위 코드는 회원이 새로운 사진을 저장 하였을때 반응하는 이벤트로  

isValidPicture은 살인, 자살, 욕설등의 유해성 콘텐츠를 감지하는 API로 이용료는 장당 1원입니다.  

savePicture은 이미지 편집 API를 이용 기기 사이즈에 맞게(400, 800, 1200, 2400)px 총 4장으로 편집하는 API로 장당 1원  

그밖에 클라우드 함수일 경우 호출당, NoSQL DB일 경우 문서 저장 당, 추가로 저장시 구동되는 워크플로우가 있을 수 있습니다.  

아래는 버전 1.0.3의 다른 팀원의 머지되어버린 PR 입니다.
```typescript
...
// src/user/store/preference.ts
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

<br />

### 클라이언트는 기술을 가진 회사를 신뢰합니다.
- 규모가 큰 회사 일수록 더욱 중요시 생각하는 __소프트웨어 테스트 자동화__ 기술은 소유한 업체에 대하여 각종 포트폴리오, 디자인등 문서에 더하여 큰 선정 고려요소이자, 신뢰를 제공 할 수 있는 대표적인 방법 중 하나입니다.

<br />

### 클라이언트는 산출물이 필요합니다.
- 개발업체를 선정하는 부분에 있어, 업체 별 산출물의 정리과정중 __소프트웨어 테스트__ 관련 문서는 고려대상이 아닐 수 없습니다.
클라이언트 입장에서, 테스트를 전적으로 우리회사에게 맡기는 경우는 거의 존재하지 않습니다.
각 회사는 개발팀부터 QA팀, PM, PL까지 많은 인력 소모를 감수하여, 매 배포시 테스트를 진행합니다.
우리는 __playwright__ 의 [reporter](#reporter) 기능을 통해,
고객에 맞는 산출물을 제공 할 수 있습니다.

<br />

### 결국 신뢰를 얻습니다.
**처음** 파트너쉽을 맺은 경우, 신중한 클라이언트들은 테스트의 결과를 믿지 못할 수 있습니다.
지속적인 검증을 통해 점차 테스트 결과서를 **신뢰하고**, 신뢰된 산출물을 바탕으로 소통 할 수 있다는 것은
- 커뮤니케이션 입장에서 매우 **효율적이고 안정적인 업무**가 가능합니다.
- 장기적인 파트너쉽 유지에 도움이 됩니다.

<br />

## 그래서 왜 Playwright?
먼저 vitest, vue3는 unit, component 공식 unit/component 테스트 라이브러리로 vitest를 사용하고 있습니다.  
하지만 vite, vue 모두 SPC 를 위한 툴이며, vitest는 SPC, Client-Side Rendering 가 아닌 환경에서는 component 테스팅조차 의도대로 동작하지 않습니다.  

이에 nuxt는 nuxt/test-utils 특히 vue는 playwright 전 cypress에 대한 복잡한 세팅과정을 CLI 사전 세팅을 통해 해결하려 했지만 라이브러리 자체의 문제인 진입장벽, 개발비용, 복잡한 셋업 과정을 커버 할 순 없었습니다. 

그동안 e2e 테스트는 unit test 보다 앱에대한 자신감을 가질 수 있지만, 
훨씬 더 요구되는 개발비용으로 인해 도입이 어려웠었던 것이 현실입니다.
이에 마이크로소프트의  __Playwright__ 는 위 문제들에 대한 대안을 제시합니다.
# 5. Refer
- https://docs.cypress.io/guides/core-concepts/testing-types
- https://playwright.dev/docs/intro
- https://doong-jo.github.io/posts/front-end_testing_strategy/
<!-- - https://wiki.abacussw.co.kr/ko/technote/frontend/javascript/vue-library/full-calendar -->