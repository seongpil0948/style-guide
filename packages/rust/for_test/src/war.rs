use std::io;
use std::collections::{ VecDeque };

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

struct Player {
    deck: VecDeque<String>
}
impl Player {
    fn new (n: i32) -> Self {
        Self {
            deck: VecDeque::with_capacity(n as usize)
        }
    }
    fn deck_len (&self) -> usize {
        self.deck.len()
    }
    fn update_deck (&mut self, cardp: String) {
        self.deck.push_back(cardp);
    }
}

fn main() {
    let mut input_line = String::new(); io::stdin().read_line(&mut input_line).unwrap();
    let n = parse_input!(input_line, i32); // the number of cards for player 1
    let mut p1 = Player::new(n);
    for i in 0..p1.deck_len() as usize {
        let mut input_line = String::new(); io::stdin().read_line(&mut input_line).unwrap();
        let cardp_1 = input_line.trim().to_string(); // the n cards of player 1
        p1.update_deck(cardp_1);
    }
    
    let mut input_line = String::new(); io::stdin().read_line(&mut input_line).unwrap();
    let m = parse_input!(input_line, i32); // the number of cards for player 2
    let mut p2 = Player::new(m);
    for i in 0..m as usize {
        let mut input_line = String::new(); io::stdin().read_line(&mut input_line).unwrap();
        let cardp_2 = input_line.trim().to_string(); // the m cards of player 2
        p2.update_deck(cardp_2);
    }


    println!("PAT");
}
