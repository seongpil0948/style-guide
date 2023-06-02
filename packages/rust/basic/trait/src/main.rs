
mod lib;

/// # Trait
/// ## define shareable behavior

/// * there are some difference, but similar to Interface in other Language
/// * Abstractism
/// * python 의 Stub?

// 1
pub trait Summary {
    // Must implement
    fn summarize(&self) -> String {
        println!("Default Sumarry Trait Method")
    }
}
trait Summary2 {}
trait Summary3 {}

// 2
pub struct NewArticle {
    pub headline: String,
    pub location: String,
    pub author: String,
    pub content: String,
}
// Tweet 에 의한 NewArticle
impl Summary for NewArticle {
    fn summarize(&self) -> String {
        // go to  println's  {}
        format!("{}, by {}, ({})", self.headline, self.author, self.location)
    }
}

pub struct Tweet {
    pub username: String,
    pub content: String,
    pub reply: bool,
    pub retweet: bool,
}

// Tweet 에 의한 Summary
impl Summary for Tweet {
    fn summarize(&self) -> String {
        format!("{}: {}", self.username, self.content)
    }
}


// both implement Summary and  Tweet
//  pub fn notify<T: Summary + Tweet>(item: T, item2: T) 

//  pub fn notify<T: Summary>(item: T, item2: T) 
//  arg is implement trait Summary
//  Garantee items has summary method
pub fn notify(item: impl Summary) -> String {
    println!("속보!: {}", item.summarize());
}

// diff type and same func
pub fn notify(item1: impl Summary, item2: impl Tweet) -> String {
    println!("속보!: {}, {}", item1.summarize(), item2.summarize());
}

/// 아이템은 3 개의 트레이트에들을 모두 구현 해야한다
pub fn notify(item: impl Summary + Summary2 + Display) -> String;
pub fn notify<T:Summary + Summary2 + Display> (item: T ) -> String;


/// 제네릭을 이용해 들어온 인자의 트레이트 구현 상태에 따른 다른 시그니처 적용
fn some_func<T, U>(t: T, u: U) -> Tweet {
    // fn some_func<T: Display + Clone, U: Clone + Debug>(t: T, u: U) -> i32 
    where 
        T: Display + Clone,
        U: Clone + Debug
    {
        Tweet {
            username: String::from("RUST_EBOOK"),
            content: String::from("Start to Read"),
            reply: false,
            retweet: false,
        }
    }
}


fn main() {
    println!("Hi Main");
    let tweet = Tweet {
        username: String::from("RUST_EBOOK"),
        content: String::from("Start to Read"),
        reply: false,
        retweet: false,
    };
    // return format!
    println!("New a Tweet: {} ", tweet.summarize());    
}
