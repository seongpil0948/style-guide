export enum TODO_STATUS {
  PREPARE = "prepare",
  IN_PROGRESS = "in-progress",
  DONE = "done",
  EXCEPTED = "excepted",
}

export interface ITodo {
  id: string;
  status: TODO_STATUS;
  text: string;
  done: boolean;
}
interface IPageOption {
  limit: number;
  page: 1;
}

let todoList = <ITodo[]>[];
const opt: IPageOption = {
  limit: 1,
  page: 1,
};

function onMounted(cb: (todo: ITodo) => void) {
  if (todoList) cb(todoList[0]);
}
onMounted(getTodo);

// 순수함수
// 인자와 리턴값이 명확합니다.
// API 주소가 바뀌었을때, 주소만 바꾸면 당신의 서비스는 문제가 없을 것입니다.
export const getTodoList2 = async (page?: string) => {
  const res = await fetch(`api/v1/todo?page=${page ?? 1}`);
  return await res.json();
};

// 이것은 순수함수가 아닙니다.
// 인자가 명확하지않고, 리턴값도 없습니다.
// 옵션에 종속성이 있어서 외부에서 opt이 바뀔경우 이함수에 영향을 미칩니다.
// 우리는 이것을 실행함수라고 부르기로 했습니다.
export const getTodoList1 = async () => {
  const res = await fetch(`api/v1/todo?page=${opt.page}`);
  todoList = await res.json();
};

const selectedTodo: ITodo | undefined = todoList[0];
export function getTodo(selectedTodo: ITodo) {
  return new Promise((resolve, reject) => {
    fetch(`api/v1/todo/${selectedTodo?.id}`)
      .then((resp) => resp.json().then((j) => resolve(j)))
      .catch((err) => reject(err));
  });
}
