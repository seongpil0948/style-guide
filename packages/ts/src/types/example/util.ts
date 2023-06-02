type Record<K extends string | number, T> = {
  [P in K]: T;
};

type IFieldValue = {
  name: string;
  value: number;
};

type IFormName = 'event' | 'point';

export const x: Record<IFormName, IFieldValue> = {
  event: {
    name: 'foo',
    value: 0,
  },
  point: {
    name: 'foo',
    value: 30,
  },
};

// Exclude 타입은 2개의 제네릭 타입을 받을 수 있으며,
// 첫번째 제네릭 타입 T 중 두번째 제네릭 타입 U와 겹치는 타입을 제외한 타입을 반환한다.
// 즉, T 타입중 U 타입을 제외하겠다라는 뜻.
export type OnlyNumber = Exclude<string | number, string>;
export type T0 = Exclude<string | number | (() => void), Function>;

// T 타입 중 U에 해당하는/할당 할 수 있는 타입을 뽑는다
export type T1 = Extract<'a' | 'b' | 'c', 'a' | 'f'>;
export type T2 = Extract<string | number | (() => void), Function>;

export type T3 = NonNullable<string[] | null | undefined>;

declare function f1(arg: {a: number; b: string}): void;
export type T4 = Parameters<typeof f1>;
export const a: T4 = (a: 1);
