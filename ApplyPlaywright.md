

# 시작전 정할사항

## 언제부터자동화 테스트를 할까?

# 사내 프로젝트 적용 방법
우리는 앞서 테스트의 필요성, Playwright 사용방법 및 특징에 대하여 알아보았습니다.  

어떤 방법으로 테스트를 우리 프로젝트에 효율적으로 적용 시킬수 있을지
우리는 Playwright의 어떤 기능들을 더 이용 할 수 있을지 알아보겠습니다.

## 프로젝트 시작 전

- 이용중인 [프레임 워크](https://github.com/socketbear/vue-dev-guide)에 설정 및 예시파일을 적용 합니다.
  - playwright.config.ts 
  - tests/unit/example.spec.ts
  - tests/e2e/example.spec.ts


## 프로젝트 진행

1. 각자 프로젝트의 **클라이언트가** 요구하는 산출물 양식에 따라, [Custom Reporter](https://playwright.dev/docs/test-reporters#custom-reporters)를 제작합니다.
	- 다음은 [builtin](#reporter) 외 제작이 예상되는 리포터 입니다.  
		- xlsx 라이브러리를 이용한 엑셀 리포터
		- 테스트 실패시 이메일, 푸시, 슬랙 알림등을 전송하는 리포터


2. 자동화 테스트로 대체할 테스트 단계와 수동 테스트 QA까지 진행 할 단계를 구분하여 기획합니다.
   - ex ) develop 단계에서는 **신규 기능에 대한 QA** 및 **자동화 테스트**로 진행
   - ex ) staging 이상부터 모든 서비스에 대한 QA 까지 진행
   - patch(1.1.x) 버전, dev 환경 수정: 자동화 테스트
   - minor 버전 이상, staging 환경 이상: 자동화 + 수동 테스트



3. 테스트 시나리오 및 코드를 작성합니다.
	- 전체 시나리오에 대한 테스트코드를 자동생성 기능을 이용하여 작성
	- [우선순위](#todo-어떻게-효율적으로-테스트코드를-작성할-수-있을까)에 따라 테스트 코드 완성
  