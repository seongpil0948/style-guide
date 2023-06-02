function Person(first, last, age, gender, interests) {
    this.name = {
      first,
      last
    };
    this.age = age;
    this.gender = gender;
    this.interests = interests;
};

Person.prototype.greeting = function() {
    alert('Hi! I\'m ' + this.name.first + '.');
};

function Teacher(first, last, age, gender, interests, subject) {
    // Teacher()의 생성자는 Person()을 상속
    // 실행하고자 하는 함수의 첫 번째 매개변수로 this를 전달하고 나머지는 실제 함수 실행에 필요한 인자들을 전달하면 됩니다.
    Person.call(this, first, last, age, gender, interests);
    // 추가 속성 정의
    this.subject = subject;
}

var teacher1 = new Teacher('Dave', 'Griffiths', 31, 'male', ['football', 'cookery'], 'mathematics');
// teacher1.__proto = Teacher constructor
// teacher1.greeting() is not a function

Teacher.prototype = Object.create(Person.prototype);
Teacher.prototype.constructor = Teacher; // person consturctor nono~~
teacher1.greeting()

// overriding
Teacher.prototype.greeting = function() {
    var prefix;
  
    if (this.gender === 'male' || this.gender === 'Male' || this.gender === 'm' || this.gender === 'M') {
      prefix = 'Mr.';
    } else if (this.gender === 'female' || this.gender === 'Female' || this.gender === 'f' || this.gender === 'F') {
      prefix = 'Mrs.';
    } else {
      prefix = 'Mx.';
    }
  
    alert('Hello. My name is ' + prefix + ' ' + this.name.last + ', and I teach ' + this.subject + '.!@#!@#@$!$!@$!@@$');
  };

  teacher1.greeting()