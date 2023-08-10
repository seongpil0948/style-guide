- [VeeValidate 가이드.](#veevalidate-가이드)
  - [왜 VeeValidate를 사용해야 할까.](#왜-veevalidate를-사용해야-할까)
    - [코드양 단축](#코드양-단축)
      - [기준 템플릿](#기준-템플릿)
      - [라이브러리 미사용시](#라이브러리-미사용시)
      - [라이브러리 사용시](#라이브러리-사용시)
    - [정확한 **타입 추론**을 지원](#정확한-타입-추론을-지원)
    - [마무리 하며](#마무리-하며)

# VeeValidate 가이드.
본 문서는 Vue3의 유효성 검사 라이브러리인 VeeValidate를 사용해야 하는 이유에 대하여 설명합니다.  
다양한 개발 환경과 프로젝트에 적용 할 수 있는 방안을 제시합니다.

## 왜 VeeValidate를 사용해야 할까.
- vue3 composition-api를 지원합니다.

- vue-devtools를 지원합니다.

- 시간, 비용이 절약됩니다..
  - 폼 유효성 검사 로직을 직접 작성하려면 많은 시간과 노력이 필요합니다. 반면에 이미 **검증된 라이브러리**를 사용하면 개발 시간을 단축하고 개발 비용을 절감할 수 있습니다.

- 코드 품질과 유지보수성
  - 외부 라이브러리는 **높은 수준의 개발자**들이 **품질**을 유지하고 **버그**를 수정하며 업데이트하는 과정을 거쳐왔기 때문에 안정성과 신뢰성이 높습니다. 

- 간편한 통합 및 사용성 
  - Vue.js와 완벽하게 통합되어 있으므로 프로젝트에서 쉽게 사용할 수 있습니다.  
  라이브러리를 설치하고 설정하는 과정이 간단하며, Vue 컴포넌트와 함께 자연스럽게 작동합니다.

- 다양한 빌트인 규칙
  - 다양한 미리 정의된 유효성 검사 규칙을 제공합니다. 필수 필드, 이메일 형식, 숫자 범위 등 다양한 규칙을 쉽게 적용할 수 있습니다. 이로 인해 개발자는 **일일이 각각의 검사 규칙을 구현하지 않아도 됩니다.**

- 보안과 안정성 
  - 검증된 라이브러리는 일반적으로 **보안과 안정성**에 대한 염려 사항을 고려하여 설계되고 유지보수됩니다. 이를 통해 애플리케이션의 보안과 안정성을 높일 수 있습니다

- 다국어 지원
  - 다국어 메시지 지원을 포함하여 다양한 언어로 에러 메시지를 정의하고 사용할 수 있습니다. 이는 **국제화된 애플리케이션**을 개발할 때 유용합니다.

### 코드양 단축
VeeValidate를 사용하면 코드양을 단축할 수 있습니다. 
예를 들어, 유효성 검사를 직접 구현하려면 많은 코드를 작성해야 합니다.
아래 예제에서는 간단한 로그인 폼을 대상으로 유효성 검사를 수행합니다.

#### 기준 템플릿
```html
<template>
  <div class="login">
    <h1 class="logo">
      <Icon name="logo__idp--536" width="198" height="29" alt="U+ 산업데이터플랫폼" />
    </h1>

    <form class="login__form" novalidate @submit="handleClickLoginBtn">
      <custom-input field-name="userId" :label="t('login.userId')" :placeholder="t('login.pls_enter_id')" size="xl"
        direction="col" required class="id" @keyup.enter="handleClickLoginBtn" />
      <custom-input field-name="password" input-type="password" :label="t('login.password')"
        :placeholder="t('login.pls_enter_pw')" size="xl" direction="col" required class="pw"
        @keyup.enter="handleClickLoginBtn" />

      <div class="login__util">
        <div class="checkbox">
          <input id="login-save-id" v-model="isSaveId" type="checkbox">
          <label for="login-save-id">{{ t('login.saveId') }}</label>
        </div>
        <button type="button" class="login__btn--text">
          {{ t('login.reset-pw') }}
        </button>
      </div>
    </form>

    <button data-test-id="login-btn" type="submit" class="btn__full--primary btn--xl" @click="handleClickLoginBtn">
      {{ t('login.login_btn') }}
    </button>
  </div>
</template>
```
#### 라이브러리 미사용시
이렇게 직접 유효성 검사 로직을 작성하는 경우, 
vee-validate가 제공하는 다양한 기능과 편의성(실시간 유효성 검사, 커스텀 규칙 등)을 
직접 구현해야 합니다.는 점을 염두에 두시기 바랍니다.
```ts
const userId: ref('')
const password =  ref('')
const validateForm = () {
    const errors = [];

    if (!userId.value) {
    errors.push('아이디를 입력해주세요.');
    }

    if (!password.value) {
    errors.push('비밀번호를 입력해주세요.');
    }
    if (!checkNonEnterableSpecialCharcter(password.value)) {
    errors.push('영문+숫자+특수문자 포함 8자리 이상 입력해주세요.');
    }
    if (!checkPasswordFrame(password.value)) {
    errors.push('입력 불가능한 특수문자를 확인 해주세요.');
    }

    if (errors.length > 0) {
    // 유효성 검사 에러 처리
    console.log('유효성 검사 에러:', errors);
    return false;
    }

    return true;
}

const handleClickLoginBtn = () => {
    if (this.validateForm()) {
        const param = {
            userId: this.userId,
            password: this.password
        }
        const res = await request.post<ILoginResponseWrap<ILoginApiBody>>(param)
    }
}

// 영문+숫자+특수문자 포함 8자리 이상
function checkPasswordFrame (value: any) {
  const regx = /^(?=.*[A-Za-z])(?=.*\d) (?=.*[-~! @$^&*=_+, •;":"\[\]{}\\])(?! .*\s). {8,20}$/;
  if (value.match(regx) === null) {
    return false;
  }
  return true;
}
// 입력 불가능한 특수문자 확인
function checkNonEnterableSpecialCharcter (value: any) {
const regx = /[< >()#&*"/]?\s\\]+/;
  if (value.match(regx) !== null) {
    return false;
  }
  return true;
} 
```

#### 라이브러리 사용시
```ts
# 1
const schema = toTypedSchema(object({
  userId: string().min(5).required(),
  password: string()
    // 영문+숫자+특수문자 포함 8자리 이상
    .matches(/^(?=.*[A-Za-z])(?=.*\d) (?=.*[-~! @$^&*=_+, •;":"\[\]{}\\])(?! .*\s). {8,20}$/)
    // 입력 불가능한 특수문자 확인
    .matches(/[< >()#&*"/]?\s\\]+/)
    .required(),
}))
# 2
const { handleSubmit, values } = useForm({ validationSchema: schema })
# 3
const handleClickLoginBtn = handleSubmit(async (values) => {
    const res = await request.post<ILoginResponseWrap<ILoginApiBody>>(..values)
})
```
1. `toTypedSchema` 함수를 사용하여, 상태값에 따라 타입 추론이 가능한, 유효성 검사 스키마로 변환합니다.
2. `useForm`은 `useField`에 의해 생성된 필드를 그룹화하고 해당 상태를 집계할 수 있는 API입니다.
useField는 `vee-validate`가 제공하는 커스텀 훅으로, 필드의 상태를 추적하고 유효성 검사를 수행합니다.
공용 컴포넌트로 분리하여 사용할 수 있습니다.
1. `handleSubmit`은 `useForm`이 제공하는 API로, `submit` 이벤트를 생성, 유효성 검사를 수행하고, 성공하면 콜백 함수를 실행합니다.


### 정확한 **타입 추론**을 지원
사용해본 결과, vee-validate는 상태값에 따라 타입 추론을 **정확하게** 지원합니다.
위의 예제에서 `values`는 `userId`와 `password`를 가지고 있습니다.
아래 코드는 유효성 검사 전 `values`의 타입으로, 모든 필드가 `undefined` 일 수 있습니다.
**유저 인터페이스**를 고려하면, 합리적인 타입 추론입니다.
```ts
{
  userId?: string,
  password?: string
}
```

그러나 유효성 검사(`handleClickLoginBtn` 함수 실행) 후 `values`의 타입은 다음과 같습니다.
```ts
{
  userId: string,
  password: string
}
```
이는 `userId`와 `password`가 필수값(`required`)이기 때문입니다.
이처럼 vee-validate는 상태값에 따라 정확한 타입 추론을 지원합니다.



### 마무리 하며
조금 낯설수있지만 우리가 사용하는 composition api를 사용하는 것은 동일합니다.
유틸 함수를 조금 익힌다면 위와 같이 간편하고, 타입에 안전하게 유효성 검사를 수행할 수 있습니다.
또한 `resetForm, setValues` 등 수많은 유틸함수와 `values` 객체는 reactive로 관리되어 추가로 선언 할 필요가 없습니다.  

더 많은 정보는 [공식문서](https://vee-validate.logaretm.com/v4/guide/overview)를 확인하세요.
감사합니다.


