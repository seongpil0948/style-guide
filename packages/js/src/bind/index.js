let user = {
    firstName: "John",
    sayHi() {
      alert(`Hello, ${this.firstName}!`);
    }
  };
  
//   !!! !!!!!! NO! !!!!
  setTimeout(user.sayHi, 1000); // Hello, undefined!

  function Ok() { // 여기서 사용할 this.는 어디서 올까?
    alert(this.firstName);
  }
  let okUser = Ok.bind(user)
  okUser()


  function func(phrase) {
    alert(phrase + ', ' + this.firstName);
  }
  
  // this를 user로 바인딩합니다.
  let funcUser = func.bind(user);
  
  funcUser("Hello"); // Hello, John (인수 "Hello"가 넘겨지고 this는 user로 고정됩니다

  