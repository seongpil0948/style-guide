use std::thread;
use std::time::Duration;
// multi producer, single consumer
// Multiple threads can send values,
// but there should be only one place to receive and use
use std::sync::mpsc;


fn haha () {
    let v = vec![1, 2, 3];
    // spawn Return JoinHandle type
    // 자식스레드 생성
    // move closure 는 한 스레드의 데이터를 다른 스레드에서 사용 가능케 한다. 소유권 또한 가진다
    // 한마디로 소유권 Move
    // 주 스레드에서 갑자기 drop 해버리면 참조가 유효해지지 않기 때문.
    // 클로저가 캡쳐하고 들어가야 주스레드의 데이터를 사용가능하쥬
    let handle = std::thread::spawn(move || {
        for i in 1..10 {
            println!("New Thread: {} v: {:?}", i, &v);
            // stop curr thread for excute other thread
            thread::sleep(Duration::from_millis(1));
        }
    });
    // 자식스레드가 다 생성딜때까지 기다림
    handle.join().unwrap();

    for i in 1..5 {
        println!("Curr Thread: {}", i);
        thread::sleep(Duration::from_millis(1));
    }

    // 자식스레드가 종료 될때까지 주 스레드가 기다림.
    // handle.join().unwrap();

    // ---------
    // transmitter, recever
    let (tx, rx) = mpsc::channel();
    let tx2 = mpsc::Sender::clone(&tx);

    std::thread::spawn(move || {
        let vals = vec![
            String::from("Hi I'm Transmitter"),
            String::from("Nice meet you "),
            String::from("hahahah"),
        ];
        for val in vals {
            tx2.send(val).unwrap();
            thread::sleep(Duration::from_secs(1));
        }        
    });
    // OW is move to received
    // println!("{}", val);


    std::thread::spawn(move || {
        let vals = vec![
            String::from("Additional, "),
            String::from("Nice meet you "),
            String::from("hahahah"),
        ];
        for val in vals {
            tx.send(val).unwrap();
            thread::sleep(Duration::from_secs(1));
        }           
    });
    
    // let received = rx.recv().unwrap();
    for received in rx {
        println!("Received: {}", received);
    }    
}

/// * Mutax(mutual exclusion)
/// - You must acquire a lock before using the data.
///     - and after use, unlock 
// Arc(Artomic Rerference Count) = 성능손실이 조금 있기때문에 다중 스레드에서 Rc 사용시에만 사용
use std::sync::{Mutex, Arc};

fn main() {
    // for Multi(OW) 다중소유권
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Arc::clone(&counter);
        let handle = std::thread::spawn(move || {
            // acquire a lock
            // return LockResult as MutextGuard Type as Smart Pointer
            // and this pointer is implemented Deref trait
            let mut num = counter.lock().unwrap();
            
            // dereference(역참조) 여러 스레드가 공유가능한 데이터를 락을통해
            // 얻어왔다면 사용 가능하다.
            *num += 1;            

            // 범위를 벗어나면 unlock
        });
        handles.push(handle);
    }
    for handle in handles {
        // 모든 자식 스레드가 종료되기를 기다린다.
        handle.join().unwrap();
    }

    println!("Result : {}", *counter.lock().unwrap());
}
