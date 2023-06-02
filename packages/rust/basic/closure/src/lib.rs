use std::thread;
use std::time::Duration;

fn expensive_calcultation = Cacher::new(|num| -> u32 {
    print("Very Expensive Caculating....")
    thread::sleep(Duration::from_secs(2));
    num
});

// use for memozation or lazy evaluation (캐싱)
struct Cacher<T>
    where T: Fn(u32) ->  u32
{
    calculation: T,
    value: Option<u32>
}

// 여러값에 대한 캐싱을 위해서는 HashMap에 저장하도록 해야한다/
// 타입이 한정 적이다.
impl<T> Cacher<T>
    where T: Fn(u32) ->  u32
{
    fn new(calculation: T) -> Cacher<T> {
        Cacher {
            calculation,
            value: None
        }
    }

    fn value(&mut self, arg: u32) -> u32 {
        match self.value {
            Some(v) => v,
            None => {
                let v = (self.calculation)(arg);
                self.value  = Some(v);
                v
            }
        }
    }
}