function mul(a, b) {
    return a * b;
}

// func.bind(context, [arg1], [arg2], ...);
let a = mul.bind(null, 1000)
a(5)

// ============================

let user = {
    firstName: "John",
    say(time, phrase) {
      alert(`[${time}] ${this.firstName}: ${phrase}!`);
    }
  };

  function partial(func, ...bound) {
    return function(...args) { // (*)
      return func.call(this, ...bound, ...args);
    }
  }

  // 시간을 고정한 부분 메서드를 추가함
const fixedTime = new Date().getHours() + ':' + new Date().getMinutes()
  user.sayNow = partial(user.say, fixedTime);

  user.sayNow("Hello");
// 출력값 예시:
// [10:00] John: Hello!