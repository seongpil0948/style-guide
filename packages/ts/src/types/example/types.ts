// >>> function >>>
type GreetFunction = (a: string) => void;
export function greeter(fn: GreetFunction) {
  return fn('hihi');
}

// Call Signatures
// 자바스크립트에서 function은 프로퍼티를 가질수 있고, callable하다

// <<< function <<<
// >>> conditional >>>
// T라는 제네릭 변수를 받는데, 만약 Array 타입일 경우 Array 의 제네릭 변수를 infer 하여
// Item 타입을 할당, 아니라면 제네릭 그대로 반환
// https://driip.me/b812974b-3974-46e3-829e-1476b9b30c94
export type Flatten<T> = T extends Array<infer Item> ? Item : T;
export type FlattenTwo<T> = T extends (infer Item)[] ? Item : T;

// Typically, distributivity is the desired behavior.
// To avoid that behavior, you can surround each side of the extends keyword with square brackets.
type ToArray<Type> = Type extends any ? Type[] : never;
type ToArrayNonDist<Type> = [Type] extends [any] ? Type[] : never;

export type StrArrOrNumArrWrong = ToArray<string | number>;
// 'StrArrOrNumArr' is no longer a union.
export type StrArrOrNumArrFine = ToArrayNonDist<string | number>;
// and maps over each member type of the union, to what is effectively:
// which leaves us with: string[] | number[];

// <<< conditional <<<
// >>> tuple >>>

export const bookNamePrice: [string, number] = ['카밍 시그널', 13320];
export type hmm = readonly [1, 'hello', false];
export const days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] as const;
type FirstEntry<T extends readonly unknown[]> = T[0];
type Length<T extends readonly unknown[]> = T['length'];
// 각 인덱스들의 가장 일반적인 형태(best common type)은 number 입니다.
// $ExpectType 'sun' | 'mon' | 'tue' | 'wed' | 'thu' | 'fri' | 'sat'
export type Day = (typeof days)[number];
export type FirstDay = FirstEntry<typeof days>;
// <<< tuple <<<
export type CountOfDays = Length<typeof days>;
