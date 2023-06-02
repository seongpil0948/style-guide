use std::sync::{mpsc, Arc, Mutex};
use std::thread;

trait FnBox {
    // 매개변수에 대한 소유권을 갖고 Box<T>를 외부로 옮길 수 있도록
    fn call_box(self: Box<&self>);
}

/// FnOnce 트레이트를 구현하는 모든 F 타입 매개변수에 대해 FnBox 트레이트를 구현
/// call_box 는 클로저를 Box(T)에서 옮겨와 호출한다.
impl<F: FnOnce()> FnBox for F {
    fn call_box(self: Box<F>) {
        (*self)() // DeReferencing Function
    }
}

// execute 메소드가 전달받을 클로저 타입을 저장할 트레이트 객체에 대한 별칭
// 런타임에 동적으로 FnBox 트레이트를 구현 하는 타입
type Job = Box<dyn FnBox + Send + 'static>;

struct Worker {
    id: usize,
    // () for Return None
    thread: thread::JoinHandle<()>,
}

impl Worker {
    // MutexGuard 의 수명주기에 대하여 잘 알아 둘 필요가 있다.

    fn new(id: usize, receiver: Arc<Mutex<mpsc::Receiver<Job>>>) -> Worker {
        // create new thread
        let thread = thread::spawn(move || {
            // 채널의 수신샂로부터 새로운 작업이 있는지 확인
            // 리소스 점령후(락 희득)
            // 에러방지 Mutex 상태에 문제가 있다면 에러 발생 가능
            // 채널에 속한 Sender로 부터 recv 메소드를 호출, Job Instance 수신
            while let Ok(job) = job = receiver.lock().unwrap().recv() {
                print!("Start: Worker {}", id);
                job.call_box();
            }
        });
        Worker { id, thread }
    }
}

pub struct ThreadPool {
    workers: Vec<Worker>,
    sender: mpsc::Sender<Job>,
}

impl ThreadPool {
    /// New Thread Pool Instance
    /// size arg: num of threads in pool
    /// # Panics
    ///     * size <= 0
    ///     * usize for using not negative
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let (sender, receiver) = mpsc::channel();
        // Arc: 여러 작업자가 하나의 수신자를 공유한다,
        //    - Reference Count is added
        // Mutex: 한번에 하나의 작업자가 수신자로 부터 작업을 가져 올 수 있다.
        let receiver = Arc::new(Mutex::new(receiver));
        // with_capacity: Set vector size in advance
        let mut workers = Vec::with_capacity(size);

        for _ in 0..size {
            // 스레드들을 생성하고 벡터 내에 보관합니다
            workers.push(Worker::new(id, Arc::clone(&receiver)));
        }
        ThreadPool { workers, sender }
    }
    /// * closure arguments [Fn, FnMut, FnOnce(단한번만 실행 가능한 함수)]
    ///     - f: thread use func after created
    pub fn execute<F>(&self, f: F)
    where
        // FnOnce는 리턴과 매개변수가 없기 때문에 괄호가 필요
        F: FnOnce() -> ThreadPool,
        F: Send + 'static,
    {
        // 클로저를 이용해 Job 생성
        let job = Box::new(f);
        // prevent Error
        self.sender.send(job).unwrap();
    }
}
