# Playwright 시작하기
완벽한 어플리케이션을 제작하기 위한 개발자.  
우리 프론트엔드 개발자들을 위한 문서입니다.

## 시작하기전에
만약 당신이 [프론트엔드 테스팅 기본](/technote/frontend/test)를 읽지 않았다면 읽고 오시길 바랍니다.

- [Playwright 시작하기](#playwright-시작하기)
  - [시작하기전에](#시작하기전에)
- [왜 Playwright를 써야할까?](#왜-playwright를-써야할까)
  - [구체적으로 뭐가 좋을까?](#구체적으로-뭐가-좋을까)
      - [다양한 사용자 환경 지원](#다양한-사용자-환경-지원)
      - [확장성과 반복성](#확장성과-반복성)
      - [오류 감소와 일관성](#오류-감소와-일관성)
      - [빠른 피드백](#빠른-피드백)
- [Playwright란?](#playwright란)
  - [시작하기](#시작하기)
    - [결과 살펴보기](#결과-살펴보기)
      - [1. 행동(Action) 타임라인](#1-행동action-타임라인)
      - [2. 행동 목록](#2-행동-목록)
      - [3. 행동 뷰어](#3-행동-뷰어)
      - [4. 추적 정보 뷰어](#4-추적-정보-뷰어)
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
    - [14. 픽스처(Fixtures)](#14-픽스처fixtures)
      - [관련 링크](#관련-링크)
  - [그래서 왜 Playwright여야 할까?](#그래서-왜-playwright여야-할까)
- [Refer](#refer)


# 왜 Playwright를 써야할까?
    Playwright는 빠르고, 안정적인 테스트 자동화를 지원하는 Microsoft의 오픈소스 입니다.
대부분의 개발자들은 테스트 코드를 작성해야 하는 것을 너무나 잘 알고있습니다.   
그러나 빠듯한 일정에 대부분 도입을 주저합니다.  
이에 **Playwright**는 다양한 기능들을 통해 빠르고 안정적인 테스트 자동화가 이루어 질 수 있도록 지원합니다.  

## 구체적으로 뭐가 좋을까?
#### 다양한 사용자 환경 지원
여러 버전 또는 다양한 환경에서 소프트웨어를 테스트해야 하는 경우 자동화된 테스트는 수동 테스트보다 훨씬 효율적입니다.   
Playwright는 Chrome, Firefox, IPhone등 다양한 사용자 환경을 지원합니다.
#### 확장성과 반복성
자동화된 테스트는 큰 규모, 반복적인 작업 수행하는 데 탁월합니다.
URL을 입력하고 웹페이지와 인터랙션을 하면 Playwright는 그 행동에 대한 테스트코드를 작성 해줍니다.
#### 오류 감소와 일관성
수동 테스트는 사람의 **실수**라는 리스크가 있지만, 자동화된 테스트는 미리 정의된 작업을 정확히 수행하므로 일관성과 정확성이 향상됩니다.  
예상 결과와 실제 결과를 비교하여 오류를 식별하고 이에 대한 자세한 정보를 제공할 수 있습니다.  
#### 빠른 피드백
자동화된 테스트는 빠른 피드백 제공을 가능하게 합니다.  
테스트 결과와 오류 보고서가 즉시 생성되어 개발자나 테스터에게 전달되므로 문제를 신속하게 파악하고 수정할 수 있습니다.  
이는 개발 초기 단계에서 문제를 발견하고 해결하는 데 도움이 됩니다.

# Playwright란?
Playwright는 웹 애플리케이션 테스트 및 자동화를 위한 오픈 소스 도구입니다. 
브라우저(Chrome, Firefox, Safari 등)를 제어하고   
사용자의 행동(클릭, 키 입력, 네비게이션 등)에 대한 시뮬레이션, 테스트 기능을 제공합니다.

## 시작하기
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
    - 설치중 문제가 발생하였나요? 
      - 리눅스(Ubuntu) 환경이라면 패키지 의존성 관련 에러가 발생 할 수 있습니다
      - 아래 명령어를 사용하여 설치하세요. [관련링크](https://github.com/microsoft/playwright/issues/13738)
        ``` bash
          $ pnpm exec playwright install --with-deps
          or
          $ npx playwright install --with-deps
        ```
      - 그럼에도 문제가 발생 할 경우, [공식 설치페이지](https://playwright.dev/docs/intro#installing-playwright)를 참고 하십시오.


3. 설치 완료 확인을 위해 파일목록을 확인하세요.
   - 추가된 파일
      ```
      playwright.config.ts: playwright 설정파일
      test/e2e/: e2e 예시 파일
      tests-examples: 데모 TODO 앱 e2e 테스트 폴더
      ```
    - 수정된 파일
      ```
      .gitignore : playwright관련 출력 파일 목록 추가
      package.json : "@playwright/test" 패키지 추가
      pnpm-lock.yaml
      ```

4. vscode 에디터인경우 [익스텐션 설치](https://playwright.dev/docs/getting-started-vscode)을 설치해야 합니다.
	1. 익스텐션 아이콘을 눌러 목록으로 이동합니다.
![install_extension2.png](/성필/playwright/install_extension2.png)
	2. install 버튼을 클릭하여 설치합니다.
![playwright_extension.png](/성필/playwright/playwright_extension.png)


5. package.json 파일의 scripts 프로퍼티에 아래 명령어를 추가 하십시오.
    [관련문서](https://playwright.dev/docs/running-tests)
    ```json
        "test:e2e": "pnpm exec playwright test",
        "test:e2e:debug": "pnpm exec playwright test --debug",
        "test:e2e:report": "pnpm exec playwright show-report",
        "test:e2e:ui": "pnpm exec playwright test --ui",
        "test:e2e:gen": "pnpm exec playwright codegen",
    ```
6. `pnpm run test:e2e:ui` 를 실행하면 아래 사진과 같이 윈도우를 확인할 수 있습니다.
    ![ui_mode_blank.png](/성필/playwright/ui_mode_blank.png)
7. 위사진의 좌측 사이드바의 테스트 케이스 목록을 클릭하여 재생(Run) 버튼을 눌러주세요.
    아래와 같이 녹색 체크 표시가 보인다면, **축하합니다** 당신은 테스트에 성공했습니다!
    ![playwright-ui-allapssed.png](/성필/playwright-ui-allapssed.png)

### 결과 살펴보기
우리가 이전 단계에서 실행한 테스트한 정보를 확인 하겠습니다.  
모든 테스트 파일이 테스트 사이드바에 로드되어 각 파일을 확장하고  
블록을 설명하여 각 테스트를 개별적으로 실행, 보기, 보기 및 디버그할 수 있습니다.  

**텍스트** 또는 **@tag** 또는 통과, 실패 및 건너뛴 테스트뿐만 아니라.  
playwright.config 파일에 설정된 프로젝트별로 테스트를 필터링 할 수 있습니다. 
![filter_list.png](/성필/playwright/filter_list.png)

우리는 테스트의 전체 추적정보(trace)를 확인하고 각 작업 위에 앞뒤로 마우스를 올려(hover) 
각 단계에서 무슨 일이 발생했는지 확인하고 DOM 스냅샷을 별도의 창으로 팝업하여 디버깅 환경을 개선할 수 있습니다.
![test_ui.png](/test_ui.png)
#### 1. 행동(Action) 타임라인
테스트가 진행된 타임라인입니다. 클릭 후 마우스 이동으로 테스트가 어떻게 진행되었는지 UI로 확인 할 수 있습니다.

#### 2. 행동 목록
테스트간 진행된 행동 목록입니다 클릭시, 행동에 대한 추적(trace)정보 가 UI에 표시됩니다.

#### 3. 행동 뷰어
테스트 액션에 대한 추적 정보를 UI로 표시하는 인터랙티브 뷰어입니다.
뷰어의 특정 엘리먼트를 클릭하여 해당 셀렉터를 복사 할 수 있습니다.

#### 4. 추적 정보 뷰어
각 행동 또는 테스트전체에 대한 테스트코드, 콘솔로그, 테스트로그, 네트워크 로그를 확인 할 수 있습니다.
### 로컬환경에서 테스트 코드 작성하기
    playwright는 주어진 URL를 입력하면, 상호 작용 가능한 Window를 제공합니다.
    이것을 통해 우리는 앱을 테스트 하고, 상호작용 이력을 테스트코드로 자동 생성 할 수 있습니다.

1. 테스트 결과를 엑셀로 표시 할 수 있는 사내제작, xlsx 패키지를 설치합니다.  

    ```
    $ pnpm install -D playwright-excel-reporter xlsx@https://cdn.sheetjs.com/xlsx-0.19.3/xlsx-0.19.3.tgz
    ```

2. `playwright.config.ts` 파일을 열어 아래 코드들을 붙여넣습니다.
    ```typescript
    import { defineConfig, devices } from '@playwright/test'
    import type { IExcelConfig } from 'playwright-excel-reporter'

    export default defineConfig({
      testDir: './test/e2e',
      /* 테스트를 병렬로 실행합니다. */
      fullyParallel: true,
      /* CI 환경에서만 실패시 2회 재시도합니다. */
      retries: process.env.CI ? 2 : 0,
      /* 각 프로세스당 할당되는 스레드 수, 워커 단위로 테스트가 실행됩니다.  */
      workers: process.env.CI ? 1 : undefined,
      /* 테스트 산출물을 지정 할 수 있습니다. 더 많은 정보는 [관련링크](https://playwright.dev/docs/test-reporters)를 참고하세요 */
      reporter: [
        ['html', {
          outputFolder: 'playwright-result-html',
          outputFile: 'result.html',
        }],
        ['playwright-excel-reporter', {
          // excelInputPath: 'test/asset/unit-test-case.xlsx',
          // excelStartRow: 5,
          // caseSheetName: '블라인드',
          // excelOutputDir: 'excel-reporter-result',
          // excelOutputFileName: 'result.xlsx',
        } as Partial<IExcelConfig>],
      ],
      /* Shared settings for all the projects below. See https://playwright.dev/docs/api/class-testoptions. */
      use: {
        /* Base URL 은 도메인을 입력 하지않았을때 다음과 같이 사용합니다. `await page.goto('/')`. */
        baseURL: 'http://localhost:3333',

        /*  trace 테스트가 실패하면 에러관련 정보를 저장합니다. 관련문서:  https://playwright.dev/docs/trace-viewer */
        trace: 'on-first-retry',
      },

      /* 테스트 환경을 설정합니다. */
      projects: [
        {
          name: 'chromium',
          use: { ...devices['Desktop Chrome'] },
        },

        {
          name: 'firefox',
          use: { ...devices['Desktop Firefox'] },
        },
      ],
    })
    ```

2. 로컬 서버를 실행시킵니다.

    `$ pnpm run dev`

3. 새로운 테스트 파일을 생성합니다. 
	
  	`$ touch test/e2e/el-todo.spec.ts`
  
4. 다음 코드를 붙여넣습니다. 
```typescript
import { expect, test } from '@playwright/test'

// "Todo CRUD"라는 테스트 그룹과 하위 케이스 "create todo" 
const MAIN_ROUTE = 'http://localhost:3333/guide/samp/el-todo'
test.describe('Todo CRUD ', () => {
  test('create todo', async ({ page }) => {
    await page.goto(MAIN_ROUTE)
    await page.screenshot({ path: 'screenshots/todo/before-create.png', fullPage: true })

    await page.screenshot({ path: 'screenshots/todo/after-create.png', fullPage: true })    
  })
})
```
5. 커서를 `await page.goto(MAIN_ROUTE)` 하단 9번 라인에 위치 시킵니다.
    ![record_at_cursor.png](/성필/record_at_cursor.png)
6. 상단 사진의 1, 2번을 차례로 클릭하여 상호작용 가능한 Window를 실행시킵니다.

7. 테스트 브라우저의 주소창에 `http://localhost:3333/guide/samp/el-todo` 입력하여 이동합니다.

8. 페이지에서 todo 항목을 입력하고 추가 버튼을 눌러 **데이터 2건 생성**을 테스트 해보십시오.

9. playwright - code generate 기능을 통해 테스트 코드가 생성되었음을 확인하세요  
	 **만약 조금 이상하거나 다르다면 아래 코드를 붙여넣으세요.**
	
    ```javascript
    // test/e2e/
    //  --| el-todo.spec.ts
    import { expect, test } from '@playwright/test'

    test.describe('Todo CRUD ', () => {
      test('create todo', async ({ page }) => {
        await page.goto('http://localhost:3333/guide/samp/el-todo')

        await page.screenshot({ path: 'screenshots/todo/before-create.png', fullPage: true })
        
        await page.getByPlaceholder('TO-DO 항목을 입력해주세요.').click()
        await page.getByPlaceholder('TO-DO 항목을 입력해주세요.').fill('소금빵을 산다')
        await page.getByPlaceholder('TO-DO 항목을 입력해주세요.').press('Enter')
        await page.getByPlaceholder('TO-DO 항목을 입력해주세요.').click()
        await page.getByPlaceholder('TO-DO 항목을 입력해주세요.').fill('밥을 먹는다.')

        await page.screenshot({ path: 'screenshots/todo/after-create.png', fullPage: true })  
        
      })
    })
    ```

10.  좋습니다. 이제 생성된 2개의 todo목록에 대한 검증을 위한 코드를 16번 라인에 추가하겠습니다.  
```javascript
		// 할 일 목록 테이블에 2개의 행이 존재하는지 검증하는 코드
    expect((await page.$$('.data-test-row')).length).toEqual(2)
```

11. 테스트 UI를 통해 테스트를 실행합니다.   
		1. `pnpm run test:e2e:ui`  
		2. ![run_create_todo_test.png](/성필/run_create_todo_test.png)
12. 저런 테스트가 실패했습니다! 살펴봅시다.  **[사진 12]**  
![ui-test-fail.png](/성필/ui-test-fail.png)
    1. 실패한 테스트 목록을 확인 할 수 있습니다.
    2. 에러메세지를 확인 결과: 행이 2개가 아니라 0개로 잡힙니다.
    3. 테스트 진행 중 화면을 확인하니 행이 한개가 있습니다.


두 번째 행을 추가하는 테스트 코드 작성과  
`.data-test-row` class 를 가진 row 목록을 받아오는 코드의 수정이 필요합니다.

13. 두 번째 행을 추가하는 테스트 코드 작성
    1.  3번의 탭목록중 Pick locator를 클릭합니다.
    2.  그리고 화면의 추가 버튼을 클릭합니다.
    3.  ![add_todo.png](/성필/add_todo.png)
    4. **사진 12.4** 부분에서 복사, 파일열기 아이콘을 차례대로 누릅니다.
    5. 테스트코드에 `click` 기능과 함께 추가합니다.
    6. ```typescript
        await page.getByPlaceholder('TO-DO 항목을 입력해주세요.').fill('밥을 먹는다.')
        await page.getByRole('button', { name: '추가' }).click()
        expect((await page.$$('.data-test-row')).length).toEqual(2)
        ```
14. `.data-test-row` class 를 가진 row 목록을 받아오는 코드의 수정
> 테스트에 사용될 selector는 반드시 **data-test**를 prefix로 가져야 합니다.   
> 즉 변경되지 않으며 JS/Css 와 **격리**된, 테스트 용도의 속성이어야 합니다.  
 `src/guide/pages/samp/el-todo.vue` 파일 - `el-table` 엘리먼트의 속성을 추가합니다.          
  ```html
  <!-- row-class-name="data-test-row 속성 추가 -->
  <el-table data-test-id="todo-table" :data="todoList" style="width: 100%" row-class-name="data-test-row">
  ```

15.  다시 테스트를 진행, 성공을 확인합니다.
16.  screenshots 폴더에서 테스트 중 얻은 스크린샷을 확인합니다.

## 결론

지금까지 가이드를 통해, 우리는 다음과 같은 사실을 알 수 있습니다.
- 우리는 **배포/로컬 서버**를 통해 테스트 자동화 기능을 개발 할 수 있다.  

- 기본적인 테스트 코드들을 playwright 를 통해 **자동 생성**할 수 있다.  
- 테스트 결과, 에러정보를 **산출물**로 얻을 수 있다.
- **스크린샷 기능**을 통해, 테스트 케이스 전 후 비교된 산출물을 얻을 수 있다


## Playwright 특징 목록
    Playwright 는 아래 다양한 특징들을 기반으로, 완전 관리형 e2e 환경을 제공합니다.

### 1. Test generator
- 브라우저와 상호작용을 통해 원하는 테스트 코드를 자동생성 할 수 있습니다.  

- TDD 최대 난제 중 하나인 개발비용 단축에 대한 기능이자 핵심기능 중 하나입니다.

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
Playwright는 테스트 진행 로그들을 zip파일로 저장합니다. 
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

### 14. 픽스처(Fixtures)
    fixture(고정된 상태)은 각 테스트에 필요한 환경을 사전 구성하는 기능입니다.
픽스처는 각 테스트가 진행되기 전 DB를 세팅하는 작업이 될 수도, 공통적으로 사용되는 클래스의 초기화 작업이 될 수도 있습니다.  

픽스처는 크게 두가지의 종류로 사용됩니다.
1. 여러 테스트에 걸쳐 중복된 데이터 생성이 필요할 때
2. 여러 테스트에 사용되는 상태 혹은 helper 메소드를 정의 할 때

**Playwright** 는 기존 테스트에 사용되던 test 객체에 기능을 추가(extends)/오버라이딩 하는 방법으로 사용 할 수 있습니다.
#### 관련 링크
- https://playwright.dev/docs/test-fixtures
- https://en.wikipedia.org/wiki/Test_fixture



## 그래서 왜 Playwright여야 할까?
먼저 vitest, vue3는 unit, component 공식 unit/component 테스트 라이브러리로 vitest를 사용하고 있습니다.  
하지만 vite, vue 모두 SPC 를 위한 툴이며, vitest는 SPC, Client-Side Rendering 가 아닌 환경에서는 component 테스팅조차 의도대로 동작하지 않습니다.  

이에 nuxt는 nuxt/test-utils 특히 vue는 playwright 전 cypress에 대한 복잡한 세팅과정을 CLI 사전 세팅을 통해 해결하려 했지만 라이브러리 자체의 문제인 진입장벽, 개발비용, 복잡한 셋업 과정을 커버 할 순 없었습니다. 

그동안 e2e 테스트는 unit test 보다 앱에대한 자신감을 가질 수 있지만, 
훨씬 더 요구되는 개발비용으로 인해 도입이 어려웠었던 것이 현실입니다.
이에 마이크로소프트의  __Playwright__ 는 위 문제들에 대한 대안을 제시합니다.
# Refer
- https://docs.cypress.io/guides/core-concepts/testing-types
- https://playwright.dev/docs/intro
 - https://github.com/microsoft/playwright/issues/10855
 - https://playwright.dev/docs/videos
