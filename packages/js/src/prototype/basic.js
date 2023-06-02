import {Person} from "./person.js"

let person1 = new Person('Tammi', 'Smith', 32, 'neutral', ['music', 'skiing', 'kickboxing']);
/*
    inherit(proto chain order): 
        1) person1(instance)
        2) Person: person1.__proto__ = Object.getPrototypeOf(person1)
        3) Object = person1.__proto__.__proto__ =Object.getPrototypeOf(Object.getPrototypeOf(person1))
    브라우저는 우선 person1 객체가 valueOf() 메소드를 가지고 있는지 체크합니다.
    이후 proto chain order 역순으로 메소드 갖는지 여부를 체크
    프로토타입 체인에서 한 객체의 메소드와 속성들이 다른 객체로 복사(Cloning) 되는 것이 아님을 재차 언급합니다. 
    그저 역순으로 타고 올라가면서(주소값 접근) 체크 하는 것 일뿐.. 메모리 좀 아끼겠네
*/
person1.valueOf()

/*
    하지만 Person 은 Object 의 모든 메소드를 상속 받진 않았다.
    
    Object.is(), Object.keys()등 prototype 버킷에 정의되지 않은 멤버들은 상속되지 않습니다
    상속 받으려면 Object.prototype(sub name space) 에 정의 되어야 하기 때문.
        ex) Object.prototype.valueOf() -> Ok inherit obj
            Object.haha() -> only using Class construct method
            
    아래 예제는 주어진 객체를 프로토타입 체인 바로 상위 객체로 삼아 새로운 객체를 생성.
*/
// person2.__proto__ = person1
// person2 = {}
var person2 = Object.create(person1);
person1.__proto__.Access = () => console.log("ㅋㅋ")

Person.prototype.CONSTANT = "hihihihihiihihihihihih"
// // not working
// person1.__proto__.prototype.hi = function () { console.log("HI!") }
// person1 will auto update
Person.prototype.farewell = function() {
    alert(this.name.last + ' has left the building. Bye for now!');
};

person1.farewell()
person1.Access()
console.log(person1.CONSTANT)