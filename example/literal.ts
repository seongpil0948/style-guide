// 타입이 추가 될 때마다 핸들러를 추가해야 하는 문제를 해결.
type EventNames = "click" | "doubleClick" | "mouseDown" | "mouseUp";
// type HandlerNames = 'onClick' | 'onDoubleClick' | 'onMouseDown' | 'onMouseUp';
type HandlerNames = `on${Capitalize<EventNames>}`;
type Handlers = {
  [H in HandlerNames]: (event: Event) => void;
};
// 원래 MyElement 그대로 작동!
type MyElement = Handlers & {
  addEventListener: (
    eventName: EventNames,
    handler: (event: Event) => void
  ) => void;
};

// get generic type from promise
type PromiseType<T> = T extends Promise<infer U> ? U : never;
// type A = number
type A = PromiseType<Promise<number>>;
// type B = string | boolean
type B = PromiseType<Promise<string | boolean>>;

// get generic types from array except first one
type TailOf<T> = T extends [unknown, ...infer U] ? U : [];
type HeadOf<T> = T extends any[] ? T[0] : [];

// type A = [boolean, number];
type C = TailOf<[string, boolean, number]>;
// check empty array
type IsEmpty<T extends any[]> = T extends [] ? true : false;
// type B = true
type D = IsEmpty<[]>;
// type C = false
type E = IsEmpty<[number, string]>;

// trim right through recursive
type TrimSide<T extends string> = T extends `${infer R} `
  ? TrimSide<R>
  : T extends ` ${infer L}`
  ? TrimSide<L>
  : T;
type TossTrim = TrimSide<"   Toss      ">;

type Split<S extends string> = S extends `${infer T}.${infer U}`
  ? [T, ...Split<U>]
  : [S];

// type S = ["foo", "bar", "baz"];
type S = Split<"foo.bar.baz">;

type ValueOf<Type, Paths extends any[]> =
  /*
   * IsEmpty<TailOf<Paths>>가 참이면
   * == TailOf<Paths>가 빈 Tuple이면
   */
  IsEmpty<TailOf<Paths>> extends true
    ? Type[HeadOf<Paths>]
    : ValueOf<Type[HeadOf<Paths>], TailOf<Paths>>;

// function getDeepByDots(obj: { [key: string]: any }, path: string) {
//   return path.split(".").reduce((o, k) => (o || {})[k], obj);
// }
// const result = getDeepByDots({ a: { b: { c: 1 } } }, "a.b.c");

function lodashSet<Type, Path extends string>(
  obj: Type,
  path: Path,
  value: ValueOf<Type, Split<Path>>
): void {
  // set by dots
  let current = obj;
  path.split(".").forEach((key) => {
    if (current === undefined) throw new Error("invalid path");
    current = current[key];
  });
  current = value;
}
// describe('test literal', function() {
//   it('test literal.lodashSet', function(done) {
//       let obj = { a: { b: { c: 1 } } };
//       literal.lodashSet(obj, 'a.b.c', 2);
//       assert.equal(obj.a.b.c, 2);
//       done();
//   })
// })
const someObject = {
  abacus: {
    core: {
      client: {
        platform: "foo",
      },
    },
  },
};

// OK!
lodashSet(someObject, "toss.core.client", { platform: "bar" });

// Error: 'bar' is not assignable to type '{ platform: string }';
lodashSet(someObject, "toss.core.client", "bar");
let obj: MyObj = JSON.parse('{ "myString": "string", "myNumber": 4 }');
console.log(obj.myString);
console.log(obj.myNumber);
