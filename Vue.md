# 1. Dev Guide for Vue

이 문서는 사내 Vue 프레임워크 프로젝트 레이아웃을 다루며,
개발자가 소스 코드 작성 시에 따라야 할 규칙과 그에대한 가이드를 기술합니다.

Vue의 패키지 버전은 2가 아닌 3이상을 사용 하십시오.(작성일 기준 3.3.2)

Typescript를 사용 하십시오.

이 프로젝트는 사내 인원들의 노력으로 품질을 향상 시킬 수 있습니다.
새로운 혹은 업데이트가 필요한 패턴이 있다면 이슈를 열어주세요.

## TODO
- [ ] fetch & mockup -> axios 로 변경 및 세팅 PR
- [ ] https://github.com/socketbear/vue-dev-guide

## Table of Contents

- [1. Dev Guide for Vue](#1-dev-guide-for-vue)
  - [TODO](#todo)
  - [Table of Contents](#table-of-contents)
- [2. 세팅(Setup)](#2-세팅setup)
    - [2.1 신규 프로젝트 생성시](#21-신규-프로젝트-생성시)
- [3. 파일/폴더 구성 방법](#3-파일폴더-구성-방법)
  - [3.1 파일 작성 방법](#31-파일-작성-방법)
    - [3.1.1 `style tag` 작성법](#311-style-tag-작성법)
      - [3.1.2 deep 사용법](#312-deep-사용법)
  - [3.2 `/locales/`](#32-locales)
    - [상수는 i18n으로 다국적언어들을 모두 사용 할 수 있게하십시오](#상수는-i18n으로-다국적언어들을-모두-사용-할-수-있게하십시오)
    - [3.2.1 로케일 파일 설정](#321-로케일-파일-설정)
    - [3.2.2  `useI18n()` 에서 `t` 함수를 추출하여, 사용](#322--usei18n-에서-t-함수를-추출하여-사용)
    - [3.2.3 로케일 설정](#323-로케일-설정)
  - [3.3 `/public/`](#33-public)
  - [3.4 `/src`](#34-src)
    - [3.4.1 `/src/components`](#341-srccomponents)
      - [3.4.1.1 Component-scoped styling](#3411-component-scoped-styling)
    - [3.4.2 `/src/composables`](#342-srccomposables)
    - [3.4.3 `/src/{service}`](#343-srcservice)
      - [3.4.3.1 `/src/{service}/components`](#3431-srcservicecomponents)
      - [3.4.3.2 `/src/{service}/components/{page}/{component}.vue`](#3432-srcservicecomponentspagecomponentvue)
      - [3.4.3.3 `/src/{service}/types/}`](#3433-srcservicetypes)
      - [3.4.3.4 `/src/{service}/store/}`](#3434-srcservicestore)
      - [3.4.3.5 `/src/{service}/composables/}`](#3435-srcservicecomposables)
    - [3.4.4 `/src/layouts`](#344-srclayouts)
    - [3.4.5 `/src/modules`](#345-srcmodules)
    - [3.4.6 `/src/pages`](#346-srcpages)
    - [3.4.8 `/src/store`](#348-srcstore)
    - [3.4.9 `/src/styles`](#349-srcstyles)
    - [3.4.10 `/src/types`](#3410-srctypes)
    - [3.4.11 `/test/`](#3411-test)
- [4. Vue API/Pkg 이용](#4-vue-apipkg-이용)
  - [4.1 약어 사용(Directive shorthands)](#41-약어-사용directive-shorthands)
      - [4.1.1 BAD](#411-bad)
      - [4.1.2 GOOD](#412-good)
  - [4.2 V-for](#42-v-for)
      - [4.2.1 BAD](#421-bad)
      - [4.2.2 GOOD](#422-good)
  - [4.3 props, defineProps](#43-props-defineprops)
      - [4.3.1 BAD](#431-bad)
      - [4.3.2 GOOD](#432-good)
  - [4.4 emits, defineEmits](#44-emits-defineemits)
      - [4.4.1 BAD](#441-bad)
      - [4.4.2 GOOD](#442-good)
  - [4.5 V-slot](#45-v-slot)
      - [4.5.1 BAD](#451-bad)
      - [4.5.2 GOOD](#452-good)
  - [4.6 Pinia(Store)](#46-piniastore)
      - [4.6.1 BAD](#461-bad)
      - [4.6.2 GOOD](#462-good)
  - [4.7 Composition API와 함께하는 Script Setup 사용](#47-composition-api와-함께하는-script-setup-사용)
  - [4.8 반응형(Reactivity)](#48-반응형reactivity)
    - [4.8.1 reactive](#481-reactive)
      - [limitation](#limitation)
    - [4.8.2 ref](#482-ref)
    - [4.8.3 typing](#483-typing)
- [5. UI framework](#5-ui-framework)
    - [5.1  `element plus` 사용하기](#51--element-plus-사용하기)
    - [5.1 예제 문서 준수](#51-예제-문서-준수)
- [6. INWORK Http 통신을 위해 Axios 사용하기](#6-inwork-http-통신을-위해-axios-사용하기)
  - [특징](#특징)
- [7. Css Style 작업을 위한 `.scss` 사용하기](#7-css-style-작업을-위한-scss-사용하기)
  - [`7.1 .scss` 파일 만들기](#71-scss-파일-만들기)
  - [7.2 변수 사용하기](#72-변수-사용하기)
  - [7.3 스타일 적용 가이드](#73-스타일-적용-가이드)
- [`8. Vue Use` 사용하기](#8-vue-use-사용하기)
- [`Uno CSS`와 shortcuts 구성하기](#uno-css와-shortcuts-구성하기)
  - [`shortcuts` 기능 사용하기](#shortcuts-기능-사용하기)
- [상황별 가이드](#상황별-가이드)
    - [대용량 데이터 처리](#대용량-데이터-처리)
    - [컴포넌트 내에서 최초 한 번 실행되어야 할 함수](#컴포넌트-내에서-최초-한-번-실행되어야-할-함수)
  - [Reference](#reference)

---

# 2. 세팅(Setup)

1. vscode(IDE)가 설치 되었는지 확인 하십시오.
2. 다음 vscode Extensions 목록을 설치 하십시오.
   1. [Vue Language Features (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.volar)
   2. [Typescript Vue Plugin](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin)

### 2.1 신규 프로젝트 생성시

1. 회사 공식 setup baseline 프로젝트를 Clone 하십시오.

```bash
$ git clone https://github.com/socketbear/vue-dev-guide.git
```

2. [Typescript takeover to Volar 활성화](https://vuejs.org/guide/typescript/overview.html#volar-takeover-mode)
   기본적으로 vscode는 builtin 익스텐션으로 TS(Typescript)를 지원하지만,
   Volar는 Vue 와 TS 둘 다 지원 합니다
   이는 1프로젝트 당 2개의 Ts지원 익스텐션이 활성화 됨을 의미하며,
   큰 프로젝트에서 성능저하를 야기하십시오.
   하단 이미지와 같이 Bottom 윈도우에서 takeover을 확인하십시오
   `<img src="./asset/ts-take-over.png">`
   **[⬆ back to top](#table-of-contents)**
3. 알맞은 폴더를 선정하여 파일을 생성하고 [vue example file](./example/vue.vue) 을 참고하여
   코드를 작성 하십시오.
4. 아래와 같이 포맷터가 설정 되었는지 확인 하십시오.
   1. cmd/ctr + shift + p
   2. open settings(JSON)
```json
  "[vue]": {
    "editor.defaultFormatter": "Vue.volar"
  },
```

# 3. 파일/폴더 구성 방법

## 3.1 파일 작성 방법

자신이 작성한 파일이지만, 타인원에 의해 유지보수 될 회사의 코드 입니다.
일관성, 가독성을 위해 [example](./example/vue.vue) 에 따라  일정 형식과 순서에 준수하십시오.
모든 vue 파일은 composition-api(options가 아님에 유의)을 이용하여 작성하십시오

### 3.1.1 `style tag` 작성법

https://vuejs.org/api/sfc-css-features.html#scoped-css
컴포넌트 중심의 코드 작성을 유도하는 Vue 프레임워크로 작성된 코드는
여러 컴포넌트들이 중첩된 트리 구조를 띄고 있습니다.
각 컴포넌트의 스타일 정의를 HTML 반영하게 될 경우를 상상해보세요
여러 선택자들의 override로 예상치 못한 스타일이 원치않는 컴포넌트에 적용 될 수 있습니다.
상상도 하고싶지 않겠죠.
이런 사이드 이펙트를 방지하기 위해 우리는 scoped 속성을 style 태그에 삽입합니다.
사용 방법은 다음과 같습니다.

```css
<style scoped>
  .example {
    color: red;
  }
</style>

<template>
  <div class="example">hi</div>
</template>
```

위 코드는 vite 혹은 webpack 같은 번들링 도구 별 제공하는 vue 파일 loader(vue-loader) 에 의해
다음과 같이 변환(transform) 됩니다.

```css
<style>
  .example[data-v-f3f3fdk] {
    color: red;
  }
</style>

<div class="example" data-v-f3f3fdk>hi</div>
```

위코드는 각 컴포넌트별 고유한 해쉬값에 대한 선택자(selector)로서
스타일을 적용하기 때문에, 컴포넌트 고유의 스타일을 정의 할 수 있습니다.

#### 3.1.2 deep 사용법

"하지만 만약" 당신은 UI 프레임 워크를 사용하고 있거나, 특정 컴포넌트/엘리먼트 하위 모든 컴포넌트(프레임워크 컴포넌트 포함)에 스타일을 적용하고 싶은 경우
"Deep Selectors" 를 사용할 수 있습니다 마치 다음과 같이 말이죠

```css
<style scoped>
.example :deep(.target-component) {
  /* ... */
}
</style>
```

그리고 이코드는 다음과 같이 컴파일 됩니다.

```css
<style>
.example[data-v-f3f3eg9] .target-component {
  /* ... */
}
</style>
```

위 코드를 통해 우리는 부모 컴포넌트와 자식컴포넌트중 `.target-component` 클래스를 가진
엘리먼트들에 대한 스타일 적용을 할 수 있습니다.

## 3.2 `/locales/`

__i18n 데이터를 관리하는 폴더__
i18n은 다국어 지원을 의미하며, Framework에서 해당 기능을 간단하게 지원할 수 있도록 구성되어 있습니다.
i18n을 사용하기 위해서는 다음과 같은 작업이 필요합니다.

1. `/locales` 폴더 내 로케일 파일 설정
2. `useI18n()` 에서 `t` 함수를 추출하여, 사용

### 상수는 i18n으로 다국적언어들을 모두 사용 할 수 있게하십시오
```typescript
// bad
const title = '에버커스 제목'
// good
const title = t('title.abacus')
```
### 3.2.1 로케일 파일 설정

`/locales` 폴더 내에 로케일 파일을 생성합니다. 로케일 파일은 `.yml` 형식으로 작성되며, `key`와 `value`로 구성됩니다. `key`는 `t` 함수의 인자로 사용되며, `value`는 실제로 출력될 문자열입니다. 예를 들어, `ko.yml` 파일을 다음과 같이 작성하면, `t('hello')` 함수를 호출하면 `안녕하세요`가 출력됩니다.

```yaml
hello:안녕하세요
button:
  guide:개발가이드
  about:소개
```

`.yml`으로 작성 시, 간단하게 계층 구조를 만들 수 있습니다. 예를 들어, `ko.yml` 파일을 위와 같이 작성하면, `t('button.guide')` 함수를 호출하면 `개발가이드`가 출력됩니다.

### 3.2.2  `useI18n()` 에서 `t` 함수를 추출하여, 사용

`.vue` 파일 내에서 `t` 함수를 사용하기 위해서는, `useI18n()` 함수를 사용하여 `t` 함수를 추출합니다. `useI18n()` 함수는 `t` 함수를 반환합니다.

```html
<script setup lang="ts">
const { t } = useI18n()
</script>

<template>
  <RouterLink class="icon-btn mx-2" to="/guide" :title="t('button.guide')">
    <div i-carbon-dicom-overlay />
  </RouterLink>
</template>
```

### 3.2.3 로케일 설정

`useI18n()`는 비단 `t` 함수만 추출 할 수 있는게 아닙니다. `locale`, `availableLocales`를 추출 할 수 있습니다. locale은 현재 적용된 언어이며, availableLocales는 사용 가능한 언어 목록입니다. 해당 설정 및 사용 방법은 `src/components/Footer.vue`에 정의된 내용을 확인하십시오.

## 3.3 `/public/`

해당 폴더에 저장된 파일들은 서버의 {루트 경로}/{filename} 으로 클라이언트에게 bundling, transform 등의 작업 없이 direct 로 제공될 리소스 폴더입니다.

`/public/robots.txt` will be available at `http://localhost:3000/robots.txt`

`/public/favicon.ico` will be available at  `http://localhost:3000/favicon.ico`

```html
<img :style="` width: 150%; height: 150%`" src="/logo.png" />
```

## 3.4 `/src`

source 의 약어로 프로젝트를 구성하는 소스코드가 저장될 폴더입니다.

Component, page의 명칭은 **고유**해야 합니다. 자동으로 `import` 기능을 사용함에 따라 동일한 명칭을 가진 파일들이 존재하면 무한 루프가 발생할 수 있습니다. `directoryAsNamespace: true` 로 사용하는 경우 디렉토리 path를 넣어야 사용이 가능합니다. (현재 반영된 상태)

### 3.4.1 `/src/components`

프로젝트 전체 서비스에서 사용되는 최소 단위 컴포넌트를 저장하십시오
좋은 컴포넌트는 재사용성이 높고 타 컴포넌트에 종속되지 않습니다.
- 각 파일명은 PascalCase를 준수 하십시오.
- The prefix
  - The를 prefix로 하는 이름을 가진 컴포넌트는 전역적인 최상위 컴포넌트로서
    한 단어로 정의되도록 작성하십시오.
  - 레이아웃을 포함한 페이지당 한 개만 존재 해야만합니다.
  - 재사용성이 없도록 props 를 받지 않아야 합니다.

#### 3.4.1.1 Component-scoped styling

컴포넌트 파일 내에서 `<style>` 태그를 사용 할 경우, 타 컴포넌트에도 스타일이 적용됩니다.
반드시 scoped 속성을 추가하십시오.
[관련링크](https://vue-loader.vuejs.org/guide/scoped-css.html#mixing-local-and-global-styles)

### 3.4.2 `/src/composables`

개발 간 편리성을 향상 시키기 위해서 많은 기능들이 있습니다.

Framework 내 상기 디렉토리 아래에 구성된 `export` 항목들은 자동으로 **Global**하게 사용할 수 있습니다.

디렉토리 하단의 파일들에 정의된 항목들은 `export` 여부에 따라 자동 등록됩니다.

`composable`은 **typescript**로 구성한 라이브러리 들이 존재해야 하며, 공통으로 사용되지 않을 경우 여기에 정의하지 마십시오. 그리고, 최대한 **순수 함수** 형태로 구성하십시오.

### 3.4.3 `/src/{service}`

프로젝트 하위 서비스 단위 폴더로 서비스 전역적으로 사용 되지 않으며,
해당 서비스 한정 사용되는 비즈니스 로직을 분리하기 위해 사용하십시오.

- 각 파일명은 kebab-case를 준수하여 작성하십시오.

#### 3.4.3.1 `/src/{service}/components`

서비스 내부 사용되는 최소 단위 컴포넌트를 저장하십시오.

#### 3.4.3.2 `/src/{service}/components/{page}/{component}.vue`
서비스내 특정 페이지 한정 사용되는 컴포넌트를 저장하십시오.
#### 3.4.3.3 `/src/{service}/types/}`
서비스내 한정 사용되는 타입들을 저장하십시오.
#### 3.4.3.4 `/src/{service}/store/}`
서비스내 한정 사용되는 pinia 모듈을 저장하십시오.

#### 3.4.3.5 `/src/{service}/composables/}`
서비스내 한정 사용되는 composition-api 모듈을 저장하십시오. 

### 3.4.4 `/src/layouts`

**Framework**에서는 layout으로 사용되는 파일들은 `src/layouts`에 정의합니다.
기본은 `default.vue`로 정의되어 있습니다. 그리고 각 **페이지**에서 아래와 같이 내역을 추가하면
특정 layout 파일을 사용할 수 있습니다

```html
<route lang="yaml">
meta:
  layout: guide
  // if drawer or header is not required, such as Login page
  // layout: empty
</route>
```

layout을 사용한 페이지는 layout 내 `<RouterView />`에 해당 페이지가 렌더링 됩니다. 다시 정리하자면, 각 **페이지**에서 사용하는 layout을 **선택**하는 구조 입니다.

### 3.4.5 `/src/modules`
[Modules](https://github.com/antfu/vitesse/tree/main/src/modules) 위 경로에 저장된 *.ts은 아래와 같은 템플릿을 따르며,
Vue plugin으로서 자동설치 됩니다. (src/main.ts) 
```typescript
// https://github.com/antfu/vite-ssg
export const createApp = ViteSSG(
  App,
  { routes, base: import.meta.env.BASE_URL },
  (ctx) => {
    // install all modules under `modules/`
    Object.values(import.meta.glob<{ install: UserModule }>('./modules/*.ts', { eager: true }))
      .forEach(i => i.install?.(ctx))
  },
)
```
[Vue Plugin](https://vuejs.org/guide/reusability/plugins.html#plugins) 플러그인은 APP 수준에서 기능들을 추가/확장 하기 위한 자체 코드입니다.  
각 파일명은 camelCase를 준수 해야합니다.  
*각 플러그인은 다음 항목중 하나를 준수 해야합니다.*
- Vue App에 대하여 Global directive/component 로서 등록 되어야 합니다.
- [provide/inject](https://vuejs.org/guide/components/provide-inject.html)  방법으로 하위 컴포넌트에서 사용 가능해야합니다.
- 앱 전역 프로퍼티로서 하위 컴포넌트에서 `app.config.globalProperties` 를 통해 접근 가능해야 합니다.
- 외부 라이브러리를 확장하여 `app.use(router)` 형태로 사용 가능해야합니다.

```typescript
const router = VueRouter.createRouter({
  // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
  history: VueRouter.createWebHashHistory(),
  routes, // short for `routes: routes`
})
app.use(router)
```

### 3.4.6 `/src/pages`

`Vite`에는 Webpack과 같이 많은 **플러그인**들이 존재합니다.
그중 `Pages` 플러그인([vite-plugin-pages](https://github.com/hannoeru/vite-plugin-pages))을 통해 `pages` 디렉토리에 기정의한 규칙으로 배치된 파일(*.vue/js)들을 기준으로 자동 path를 생성해 주고 있습니다. 편리한 기능이지만, 복잡한 서비스들을 가진 웹 서비스일 경우, 적절히 사용하는 구조에 따라 나눠야 하는 경우가 있습니다.

```
# path에 따른 구조 예시
src/
  ├── features/
  │  └── dashboard/
  │     ├── code/
  │     ├── components/
  │     ├── types/
  │     └── pages/
  ├── admin/
  │   ├── code/
  │   ├── components/
  │   ├── types/
  │   └── pages/
  └── pages/
```

위 내용을 보면,  **features** , **admin** 서비스를 따로 디렉토리 구성하여, 그 안에 각각의 개별 주요 디렉토리(components, types, pages …)를 통해 분리 한것을 확인할 수 있습니다. 이렇게 되면 `src` 디렉토리 바로 아래에 있는 건 전체 서비스에서 사용하는 공통을 의미하고, 각 서비스 디렉토리 안에 내역들은 각 서비스에서만 사용하는 것들로 정의가 가능합니다. 이게 필요한 이유는, `src` 바로 아래에 정의한 것들은 자동 import 됨에 따라 전역에서 사용할 수 있기 때문에, 각 사용성에 따라 분리가 필요합니다. (너무 많으면 로딩 및 개발의 불편함을 초래합니다.)

```javascript
// vite.config.js
export default {
  plugins: [
    Pages({
      dirs: [
        { dir: 'src/pages', baseRoute: '' },
        { dir: 'src/features/**/pages', baseRoute: 'features' },
        { dir: 'src/admin/pages', baseRoute: 'admin' },
      ],
    }),
  ],
}
```

- 각 서비스를 나눠진다 해도, `Vite`의 `Pages` 플러그인을 사용할 수 있습니다. 위와 같이 등록하게 되면, **sub-path**로 각 서비스들을 접근하여 사용할 수 있습니다.
- 각 파일명은 kebab-case를 준수하여 작성하십시오.
- 각 파일명은 URL 과 1대1 매칭이 되도록하십시오.



### 3.4.8 `/src/store`

특정 {service}가 아닌 전역적으로 사용되는 [Pinia](#piniastore)모듈로 구성된 폴더입니다.

- 각 파일명은 camelCase를 준수 하십시오.

### 3.4.9 `/src/styles`

css, scss 파일로 구성된 폴더 입니다. `<br>`
variables 폴더는 scss 전역 변수, 함수등을 적용 하므로 주의하세요.

### 3.4.10 `/src/types`
- 각 파일명은 PascalCase를 준수 하십시오.
- if.. `a: string | undefined`보다는 `a = computed<string>` 형태로 사용하세요

### 3.4.11 `/test/`

**[⬆ back to top](#table-of-contents)**

# 4. Vue API/Pkg 이용

[vue api 목록](https://vuejs.org/api/)을 프로젝트에 적용 하였을때의 가이드, 주의사항으로 구성 되어있습니다.

## 4.1 약어 사용(Directive shorthands)

vue는 템플릿 작성시 디렉티브의 약어 기능을 제공합니다.
반드시 약어로 사용하십시오.

#### 4.1.1 BAD

```html
  <input v-bind:value="newTodoText">
  <input v-on:input="onInput">
  <template v-slot:header>
    <h1>Here might be a page title</h1>
  </template>


```

#### 4.1.2 GOOD

```html
<input @input="onInput" @focus="onFocus" />
<input :value="newTodoText" :placeholder="newTodoInstructions" />
<template #footer>
  <p>Here's some contact info</p>
</template>

```

## 4.2 V-for
- (:key)를 각 요소 별 고유한 ID값으로 반드시 넣으십시오.
- 인덱스 값을 할당하지 않습니다
- v-if 와 같은 element에 사용하지 않습니다.

#### 4.2.1 BAD

```html
<ul>
  <li v-for="(todo, index) in todos" :key="index" >
    {{ todo.text }}
  </li>
</ul>
```

#### 4.2.2 GOOD

```html
<ul>
  <li v-for="(todo, index) in todos" :key="todo.uniqueId" >
    {{ todo.text }}
  </li>
</ul>
```

## 4.3 props, defineProps

자식 컴포넌트 코드를 작성 할 때,부모 컴포넌트로 부터 상태를 공유 받아야 하는 경우 사용 하는 API 입니다.

- 선언/정의시 camelCase, DOM Template 태그 내에서 사용할 때에는 kebab-case를 준수 하십시오.
- attribute 로서 넣는게아닌 v-bind(약어)를 사용하여 전달 하십시오.
- 가급적 Object 타입보다 String 또는 Primitive 으로 세분화 하여 전달 하십시오.

#### 4.3.1 BAD

```html
<template>
  <FloatActionButton statusLoading="progress" ></FloatActionButton>
</template>
```

```javascript
// This is only OK when prototyping
const props = defineProps(['status'])
defineProps<{ title: string | undefined }>()
```

#### 4.3.2 GOOD

```html
<template>
  <float-action-button :status-loading="'progress'" />
</template>
```

```javascript
const props = defineProps<{
  status: string
}>()

const props = defineProps({
  statusLoading: {
    type: String,
    required: true,

    validator: (value) => {
      return ['syncing', 'synced', 'version-conflict', 'error'].includes(
        value
      )
    }
  }
})
withDefaults(defineProps<{ title: string | undefined }>(), {
  title: "",
});
```

**[⬆ back to top](#table-of-contents)**

## 4.4 emits, defineEmits

자식 컴포넌트의 특정 이벤트를 부모가 수신 받아야 할 때 사용하는 API 입니다.

- 전달할 인자가 있을 경우 반드시 타입을 명시 해주세요.
- 가급적 Object 타입보다 String 또는 Primitive 으로 세분화 하여 전달 하십시오.
- defineEmits 선언시 타입은 [call signatural](https://www.typescriptlang.org/docs/handbook/2/functions.html#call-signatures) 문법을 준수 하십시오.

#### 4.4.1 BAD

```html
<template>
  <FloatActionButton v-on:update:user="onUpdateUser" ></FloatActionButton>
</template>
```

```javascript
// This is only OK when prototyping
const emits = defineEmits(["update:user"]);
```

#### 4.4.2 GOOD

```html
<template>
  <float-action-button @update:user="onUpdateUser" />
</template>
```

```javascript
const emits = defineEmits<{
  // call signature
  (e: "update:user", value: UserInfo): void;
  // named tuple property
  update: [value: string];
}>();
```

## 4.5 V-slot

**PrimaryCard** 라는 전역 컴포넌트를 사용한다 가정해봅시다.
우리는 유저프로필, 상품진열, 이벤트 배너등 다양한 곳에 한 컴포넌트를 사용 함으로써 재사용성과 유지보수성 모두 잡고 싶습니다.
부모 컴포넌트가 **PrimaryCard**의 제목, 콘텐츠 단락을 자유롭게 변경 할 수 없다면, 혹은 props api를 이용하여 텍스트 정도만 변경 할 수 있다면

```javascript
defineProps<{title: string}>()
```

필시 우리는 UserCard, ProductCurationCard, EventBannerCard 를 만들 수 밖에 없고.. 제한요소는 너무나 많습니다. 템플릿 형태로 자식 컴포넌트에 전달 하고 싶을때 "우리는 v-slot을 사용합니다."
"v-slot"은 컨텐츠 배포 통로 라는 [Slot Proposal](https://github.com/WICG/webcomponents/blob/gh-pages/proposals/Slots-Proposal.md) 에서 영향을 받았습니다.

[slot example](#good-4)을 보면,
공통된 단일 컴포넌트를 사용하며, 동일한 공간에 각기 다른 스타일과 기능의 Element들을 배치 할 수 있습니다.

위 내용을 통해 우리는 공통 컴포넌트에 v-slot을 최대한 활용하여 개발을 해야함을 알 수 있습니다.

- 중첩된 slot 사용은 유지 보수성에 좋지 않습니다.
  header-extra 를 사용하는 컴포넌트를 찾아가려면 3개의 파일을 확인 해야합니다.

#### 4.5.1 BAD

```html
<template #header="headerProps">
  <template #action="actionProps">
    <template #header-extra="extraProps">
      {{headerProps}} {{actionProps}} {{extraProps}}
      <router-link to="/cs/home" #="{ navigate, href }" custom>
        <n-a :href="href" @click="navigate"> CS 페이지</n-a>
      </router-link>
    </template>
  </template>  
</template>
```

#### 4.5.2 GOOD

```html
<template #header>
</template>
<template #header-extra>
  <router-link to="/cs/home" #="{ navigate, href }" custom>
    <n-a :href="href" @click="navigate"> CS 페이지</n-a>
  </router-link>
</template>
<template #action>
  <n-button @click="processAll"> 생성 및 매핑 </n-button>
</template>
```

## 4.6 Pinia(Store)

Vue(공식) 어플리케이션의 상태관리(State Management) 라이브러리로서, `<br>`
App 내 모든 컴포넌트에 대한 중앙 집중식 저장소(store) 역할을 담당하십시오.
"자사"는 "Options API" 패턴을 사용 하지 않으며 반드시 "Composition-API" 패턴을 사용 해주시기 바랍니다.

#### 4.6.1 BAD

```javascript
export const useCounterStore = defineStore('counter', {
  state: () => ({
    count: 0,
  }),
  getters: {
    doubleCount(state) {
      return state.count * 2
    },
  },
})|
```

#### 4.6.2 GOOD

```javascript
export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  const name = ref('Eduardo')
  const doubleCount = computed(() => count.value * 2)
  function increment() {
    count.value++
  }

  return { count, name, doubleCount, increment }
})
```

## 4.7 Composition API와 함께하는 Script Setup 사용
Vue2에서도 지원되는 Composition API 사용 시, setup() 함수에서 기존 기능과 혼용해서 사용 했었습니다. 이때 가장 귀찮은 것 중 하나가 DOM에서 사용하기 위해서 return을 통해 대상 오브젝트들을 밖으로 사용할 수 있게 선언했다면, 이제는 그렇지 않아도 됩니다. const 등 상수든 변수든 선언되면 return 과 상관없이 바로 사용할 수 있습니다.
``` typescript
<script setup>
// 상수를 선언하고,
const msg = 'Hello!'

// 함수를 선언하고,
function log() {
  console.log(msg)
}
</script>

<template>
  <!-- 그대로 사용 -->
  <button @click="log">
    {{ msg }}
  </button>
</template>
```
하지만, props와 emit은 사용하기 위해서 정의를 먼저 해야 합니다. 나머지는 Vue2의 Composition API와 같습니다.
``` typescript
// props를 정의하는 방법
const { title, typeList, financialId } = defineProps<IFinancialStatementProps>()
```
- props 정의는 defineProps를 사용합니다.
- Typescript에서 지원하는 Interface를 통해 해당 Component에서 사용하는 props를 타입 정의합니다.
- 독립된 컴포넌트는 자신이 받을 props의 타입 정의 해야 완전한 독립성을 유지할 수 있습니다. (코딩의 실수가 줄어듭니다!)
- 타입을 정의하고 사용하는 건 [Interface](https://vue-dev-guide.netlify.app/guide/interface) 문서를 확인하십시오.
- 참고: defineProps에서 바로 타입을 정의할 수 없지만, vite-plugin-vue-type-imports 플러그인을 통해 가능하게 되었습니다.
- emit 정의는 defineEmits를 사용합니다. 이후, 기존 사용하는 방식 그대로 활용하십시오
``` typescript
const emit = defineEmits(['change', 'delete'])
// ...
const updateData = () => {
  emit('change', financial)
}
```

## 4.8 반응형(Reactivity)
우리는 웹앱을 운영하고 있고, `C` 라는 변수는 `A` 변수와 `B` 변수의 합으로 
특정 인터랙션을 통해 A 와 B의 값이 변경 되었을때 `C`변수를 갱신하고 싶습니다.
그리고, A라는 변수의 영향을 받는 Element만 DOM 내에서 끊임없이 갱신(rerender)하고 싶습니다.
이때 우리는 vue의 핵심 기능중 하나인, reactivity 기능을 이용 할 수 있습니다.
- https://vuejs.org/api/reactivity-core.html
- https://vuejs.org/guide/essentials/reactivity-fundamentals.html

### 4.8.1 reactive
`function reactive<T extends object>(target: T): UnwrapNestedRefs<T>`
Reactive 오브젝트는 [JavaScript Proxies](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy) 를 사용하여 객체를 생성합니다.
반드시 인터페이스를 사용하십시오.
#### limitation
- 오직 다음과 같은 타입에 대해서만 사용 가능합니다. `objects, arrays, and collection types such as Map and Set`
- destructure, export as module(such as composable) 에 대해서 반응형이 누실됩니다.
```typescript
interface UserCounter { count: number }
const state = reactive<UserCounter>({ count: 0 })

// n is a local variable that is disconnected
// from state.count.
let n = state.count
// does not affect original state
n++

// count is also disconnected from state.count.
let { count } = state
// does not affect original state
count++

// the function receives a plain number and
// won't be able to track changes to state.count
callSomeFunction(state.count)
```
### 4.8.2 ref
`function ref<T>(value: T): Ref<UnwrapRef<T>>`
위 reactive의 한계를 보완하기 위하여, Vue는 ref 기능을 제공하며 특징은 다음과 같습니다.    
- `const count = ref(0); console.log(count.value) // 1 `
- `.value`로 읽기/쓰기 작업에 대한 reactive 기능을 제공합니다. 
- 위 reactive의 한계의 상황에서도 반응성을 잃지 않습니다.
- 이기능은 [composable](https://vuejs.org/guide/reusability/composables.html)에 거의 필수적으로 사용됩니다.
```typescript 
const obj = {
  foo: ref(1),
  bar: ref(2)
}
const obj2 = ref({
  a: 1, b: 2
})
// the function receives a ref
// it needs to access the value via .value but it
// will retain the reactivity connection
callSomeFunction(obj.foo)

// still reactive
const { foo, bar } = obj
```
### 4.8.3 typing

에러와 추가 핸들링 작업을 줄이기 위하여, string 혹은 primitive  `ref<string | undefined>(undefined)` 보다
`ref<string>("")` 과 같이 기본값을 할당 하십시오.
그 외 주소값을 가지는 모든 객체에 대하여 `ref<(string | number)[]>([])` 과 같이반드시 타입을 지정 해 주십시오.

**[⬆ back to top](#table-of-contents)**

# 5. UI framework

`vuejs`를 사용하면서, 가장 많이 사용한 경험이 있는 component set은 [element-plus](https://element-plus.org/en-US/) 입니다. vue3로 올라오면서 element ui도 [`element plus`](https://element-plus.org/en-US/)라는 이름으로 변경되고, 많음 부분이 업데이트 되었습니다. element plus는 많은 부분에 대해 좋은 컴포넌트를 제공하고, vue3를 잘 사용할 수 있도록 규칙적으로 작성되어 있습니다. 문제는 element plus를 그대로 사용하기에는 거대하고 큰 몸체를 가지고 있기 때문입니다. 다행히도, Framework에서는 사용하는 부분만 가져와 사용하고 빌드할 수 있게 `resolver`가 구성되어 있습니다. 이를 통해, 필요한 부분만 `import` 도 없이 사용이 가능합니다.

> **tip** : 간혹, 사용한 component에서 사용 에러가 나올 경우, 오탈자인 경우가 대부분입니다. 다시 찾아보세요.

### 5.1  `element plus` 사용하기

[`element plus`](https://element-plus.org/en-US/)의 사이트로 들어가 우측 상단의 **Component**를 클릭해서 들어가면, 제공되는 컴포넌트들을 볼 수 있습니다. 여기서 사용할 때, 코드 그대로 가져와 `<template />` 영역에 넣어 사용하면 됩니다. `import` 없이 resovler가 알아서 가져와 사용합니다. 예를 들어, `button`을 사용하고 싶다면, 아래와 같이 사용하면 됩니다.

```html
<el-button type="primary"disabled>Primary</el-button>
<el-button type="success"disabled>Success</el-button>
```

`src/guide/pages/samp/el-todo.vue` 파일을 보면 좀 더 자세한 사용법을 볼 수 있습니다.

### 5.1 예제 문서 준수

프레임 워크에 기여한 사람들은 대부분 숙련된 프론트엔드 개발자 입니다.
예제 문법을 준수하여 사용해야 하십시오.
가독성 또는 축약을 위해 함부로 수정 하지 마십시오.

# 6. INWORK Http 통신을 위해 Axios 사용하기

Axios는 node.js와 브라우저를 위한 *[Promise 기반](https://javascript.info/promise-basics)* HTTP 클라이언트 라이브러리입니다.

서버 사이드에서는 네이티브 node.js의 `http` 모듈을 사용하고, 클라이언트(브라우저)에서는 XMLHttpRequests를 사용합니다.

## 특징

* 브라우저를 위해 [XMLHttpRequests](https://developer.mozilla.org/ko/docs/Web/API/XMLHttpRequest) 생성
* node.js를 위해 [http](http://nodejs.org/api/http.html) 요청 생성
* [Promise](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise) API를 지원
* 요청 및 응답 인터셉트
* 요청 및 응답 데이터 변환
* 요청 취소
* JSON 데이터 자동 변환
* [XSRF](https://ko.wikipedia.org/wiki/%EC%82%AC%EC%9D%B4%ED%8A%B8_%EA%B0%84_%EC%9A%94%EC%B2%AD_%EC%9C%84%EC%A1%B0)를 막기위한 클라이언트 사이드 지원

# 7. Css Style 작업을 위한 `.scss` 사용하기

CSS를 그대로 사용하는 것은 험난한 일입니다. 옛것을 그대로 사용하는 것은 낭만이 있는 방법이지만, 생산성과 편의성을 위해서 CSS는 전처리기가 포함된 좋은 라이브러리들이 생겨났습니다. stylus, less, sass, scss, postcss 등이 그것입니다. 이 문서에서는 guide 문서를 기반으로 만들어진 framework 기반에서 `scss`를 사용하는 방법을 다룹니다. **Framework**는 `scss`를 사용하기 위해 `sass` 라이브러리가 개발환경에서 설치되어 사용합니다. Vitejs에서는 별다른 설정 없이, `sass` 라이브러리만 설치해도 사용할 수 있게 구성해 줍니다.

## `7.1 .scss` 파일 만들기

`.css` 든 `.scss` 든, 이러한 스타일 파일들은 퍼블리셔가 작성합니다. 작성 경우 크게 두 가지 타입으로 나눠 집니다. 서비스 전체에 걸쳐 반영되는 main 혹은 global 급의 스타일과, 각 subpath 내 서비스 별 급의 스타일로 나눠집니다. **main** 급 스타일 파일들은 `src/styles`에서 작성됩니다. **subpath** 급 스타일 파일들은 각 서비스의 폴더 내 `styles` 폴더에서 작성됩니다. 이렇게 작성된 스타일 파일들은 main 급은 `App.vue`에서 import 되고, subpath 급은 각 서비스의 `index.vue`에서 import 됩니다. 물론, 각 서비스의 `index.vue`에서 import 되는 스타일 파일들은 `App.vue`에서 import 되는 스타일 파일들을 포함합니다.

해당 예시는 `src/styles/test.scss`와 `src/guide/pages/samp/scss-test.vue`를 확인 하면 됩니다. 참고로, 해당 `scss` 파일은 `App.vue`에서 import 되고 있습니다.

## 7.2 변수 사용하기

`.scss`는 위와 같이 간단하게 사용할 수 있습니다. 문제는 변수를 선언해서 사용하는 경우입니다. `Vitejs` 환경에서는 **on-demand** 형식으로 필요에 의해서 불러와 사용하는 방식이기 때문에 전반적으로 영향을 미치는 변수의 경우 이러한 `scss` 들이 사용하기 전에 선언되어야 합니다. 이러한 경우 vitejs에서는 `vite.config.js`에서 `css.preprocessorOptions`를 통해 전역 변수를 선언할 수 있습니다. 해당 예시는 `vite.config.js`에서 `css.preprocessorOptions`를 통해 전역 변수를 선언하는 방법을 보여줍니다. 해당 예제의 변수를 선언한 파일은 `src/styles/_variables.scss`입니다.

```js
// vite.config.js
// SCSS 전역 사용
css:{
    preprocessorOptions:{
	scss:{
	    additionalData:'@import "./src/styles/_variables";',
	},
    },
},
```

## 7.3 스타일 적용 가이드

* `src/styles` 폴더에 `scss` 파일을 생성합니다.
* 서비스 전체에서 사용하는 스타일은 `main.scss` 혹은 `global.scss`에서 정의하고, `App.vue`에서 import 합니다.
* 서비스 상위(로그인, 레이아웃 등)에서 사용하는 page 나 component 경우, `src/styles/pages` 혹은 `src/styles/components`에 `scss` 파일을 생성하고, 해당 `scss` 파일을 import 합니다. 파일명은 사용되는 `.vue` 맞추는 것을 권장합니다.
* 각 서비스 내에서 사용되는 스타일들은 각 서비스 내 `styles` 폴더에 `scss` 파일을 생성합니다.
* `scss` 파일을 생성할 때, `scss` 파일명은 `kebab-case`를 사용합니다.
* 변수와 같이 전역적으로 사전에 시작되는 파일들은 `_`를 붙여서 생성합니다.
* 사전에 정의된 css 셋은 [UnoCSS](https://github.com/unocss/unocss)를 우선으로 사용합니다. tailwind나 windiCSS와 같은 형식으로 사용 가능합니다.

# `8. Vue Use` 사용하기

[`Vue Use`](https://vueuse.org/)는 javascript의 `lodash`와 같이 vue3로 개발 할 때, 레고의 블럭과 같이 많이 사용할 만한 컴포넌트나 기능들을 모아둔 라이브러리 셋입니다. 대부분 기능들은 컴포넌트로도 사용가능하며, `composition API`를 사용하여 개발할 수 있습니다. Vue Use의 대부분 기능들은 `import`를 하지 않아도 바로 사용 가능합니다. [`Vue Use`](https://vueuse.org/) 사이트에서 여러 기능과 컴포넌트들을 확인하십시오. 개발 간 편리성을 위해 `Vue Use`를 사용하면 좋습니다.

# `Uno CSS`와 shortcuts 구성하기

Tailwindcss가 나오면서 css를 작성하는 방법이 많이 바뀌었습니다. Class를 utility 형태로 사용하면서, css를 `.css` 가 아닌, html 내에서 작성하고, 이를 통해 궁극적으로 추가/수정의 편리성, Copy & Paste의 용의성을 가지고 왔습니다. 이후, windicss 등이 나왔고, 주요한 골자인 class를 utility 형태로 사용한다는 것은 편하지 않았습니다. `Uno CSS`도 마찬가지 입니다. tailwindcss를 기존에 사용하고 있어도 문제 없이 사용 가능하게 **tailwind** 전용 **사전 정의 셋**을 제공하고 있습니다.

## `shortcuts` 기능 사용하기

이미 지정된 사전 정의 셋을 사용만 하기에는 부족할 수 있습니다. Bootstrap과 같이 기본적인 class를 사용하고 싶을 수도 있고, 특정 class를 사용하고 싶을 수도 있습니다. 이럴 때, `shortcuts` 기능을 사용하면 됩니다. `shortcuts` 기능은 `unocss.config.ts` 내 `shortcuts` 항목에 추가 하면됩니다.

```js
export default defineConfig({
  shortcuts: [
    ['btn', 'px-4 py-1 rounded inline-block bg-teal-700 text-white cursor-pointer hover:bg-teal-800 disabled:cursor-default disabled:bg-gray-600 disabled:opacity-50'],
    ['icon-btn', 'inline-block cursor-pointer select-none opacity-75 transition duration-200 ease-in-out hover:opacity-100 hover:text-teal-600'],
    ['tiny-btn', 'border px-1 hover:bg-green-600 hover:text-white hover:border-green-600 active:bg-green-300'],
    ['tiny-del-btn', 'border px-1 hover:enabled:bg-red-600 hover:enabled:text-white hover:enabled:border-red-600 active:enabled:bg-red-300 disabled:cursor-not-allowed disabled:text-gray-300'],
  ],
})
```

이차원 배열로 구성되며, shortcut 구성을 하는 방법은 다음과 같습니다.

```js
['shortcut-name','class1 class2 class3 ...']
```

이 외 많은 기능들이 있습니다. [`Uno CSS` 사이트](https://github.com/unocss/unocss)를 참고하십시오.

# 상황별 가이드

### 대용량 데이터 처리
Vue 는 상태관리에 대한 직관성을 위해, 반응형 변수에 대해 deep observe 가 default 하도록 되어있습니다.
또한, 그에대한 event effect를 WeakMap전역변수로 관리하기 때문에, 데이터(This typically becomes noticeable when dealing with large arrays of deeply nested objects) 크기가 커지게 되면 오버헤드로 RAM 2G 사양의 클라이언트 노트북에서 확인이 불가능 할 것이 눈에 선합니다.
최적화 방법에는 여러가지가 있지만, 이에 vue-api는 [shallow](https://vuejs.org/api/reactivity-advanced.html) 를 제공합니다. 이 기능은 반응형 변수에 대한 root level 에 대해서만 observe 기능을 제공하고 있습니다.

```typescript
const shallowArray = shallowRef([...Array(100000).keys()].map(num => ({ num })))

watch(
  () => shallowArray.value,
  val => console.log('shallowArray to ', val),
  { deep: true },
)

function triggerForce() {
  const newObject = { num: 5000 }
  shallowArray.value.push(newObject)
  triggerRef(shallowArray)
}
function triggerSuccess() {
  const newObject = { num: 5000 }
  shallowArray.value = [...shallowArray.value, newObject]
}
function triggerFail() {
  const newObject = { num: 5000 }
  shallowArray.value.push(newObject)
}
```
https://vuejs.org/guide/best-practices/performance.html#reduce-reactivity-overhead-for-large-immutable-structures


### 컴포넌트 내에서 최초 한 번 실행되어야 할 함수

composition api를 사용하는 경우에는 `<b>`setup hook에서 beforeCreate, created에 해당하는 과정이 한꺼번에 처리 됩니다.
최초 데이터를 받아오는 함수는 사이클이 아닌 `setup` 과정에서 받아 올 수 있도록 합니다.

## Reference

- https://vuejs.org/style-guide/
- https://vue-dev-guide.netlify.app/guide
- https://vuejs.org/guide/extras/reactivity-in-depth.html