use std::{io};
use std::collections::HashMap;
use rand::{thread_rng, Rng};

macro_rules! parse_input {
    ($x:expr, $t:ident) => {
        match $x.trim_matches('\n').trim_end().trim().parse::<$t>() {
            Ok(result) => result,
            Err(e) => panic!("ERROR IN MACRO {} \n {}", $x, e)
        }
    }
}

type C = i32; // common type
type GradientIdx = usize;
type NumOfGradient = C;
type DeltaNumOfGradient = C;
const NUM_OF_GRADIENT_TYPES: GradientIdx = 4;

#[derive(Clone, Debug)]
struct Witch {
    score: C,
    grads: HashMap<GradientIdx, NumOfGradient>,
}
impl Witch {
    fn new() -> Self{
        let g = HashMap::with_capacity(NUM_OF_GRADIENT_TYPES);
        Self {
            score: 0,
            grads: g // k: num of tier-0 ingredients in inventory
        }
    }
    fn update (&mut self, inputs: Vec<&str>) {
        self.score = parse_input!(inputs[4], C);
        for tier in 1..=NUM_OF_GRADIENT_TYPES as GradientIdx {
            self.grads.insert(tier -1 , parse_input!(inputs[tier - 1], C));
        }   
    }
}
#[derive(Debug, Clone, PartialEq)]
enum ActionType {
    Brew,
    Cast,
    OpponentCast,
    Rest,
    Wait,
}
impl ActionType {
    fn matching(a_type: String) -> Self {
        match a_type.as_str() {
            "BREW" => Self::Brew,
            "CAST" => Self::Cast,
            "OPPONENT_CAST" => Self::OpponentCast,
            _ => panic!("Not Matched Any Type : {} \n among ('BREW', 'CAST', 'OPPONENT_CAST", a_type)
        }
    }    
}

#[derive(Clone, Debug)]
struct Action {
    a_id: C,
    //  only (delta <= 0) not positive if action type BREW
    //  available both posit or negative if action type Other
    // in the first league: BREW; later: CAST, OPPONENT_CAST, LEARN, BREW
    a_type: ActionType,
    // detas idx = GradientIdx
    deltas: Vec<DeltaNumOfGradient>,
    // revenue earned ruppes
    earn: C,
    castable: bool
}
impl Action {
    fn new_rest () -> Self {
        Self {
            a_id: -1,
            a_type: ActionType::Rest,
            deltas: vec![-1],
            earn: -1,
            castable: false
        }
    }
    fn new (inputs: Vec<&str>, num_types: GradientIdx) -> Self {
        let mut d = Vec::with_capacity(num_types);
        for tier in 2..=(1 + NUM_OF_GRADIENT_TYPES) as GradientIdx { // 2, 3, 4 ,5
            d.push(parse_input!(inputs[tier], C));
        }
        let id = parse_input!(inputs[0], C); 
        Self {
            a_id: id,
            a_type: ActionType::matching(inputs[1].trim().to_string()) ,
            deltas: d,
            earn: parse_input!(inputs[6], C),
            castable: match parse_input!(inputs[9], C) {
                1 => true,
                0 => false,
                _ => panic!("{} is not accepted as boolean", parse_input!(inputs[9], C))
            }
        }
    }

    fn print_act (&self) {
        match self.a_type {
            ActionType::Brew => println!("BREW {}", self.a_id),
            ActionType::Cast => println!("CAST {}", self.a_id),
            ActionType::Rest => println!("REST"),
            _ => println!(" Not Implement")
        }
    }
}
/**
    TODO: 소유권 관리 차원 및 탐색 줄임을 위해 액션 타입별로 그래프를 생성.
    TODO: 우선순위 (위상 정렬)
        1. 캐스트 그래프 로부터 개수에 상관없이 MAX_EARN 이 완성 가능한 경우
        2. BREW 그래프 로부터 일단 물약 제조가 가능한경우
        3. 물약이 2개 이상 사용가능해지는 중점일 경우 
        4. Tier 가 높은게 생성되는 CAST 인 경우

    TODO: Cast 에 의해 사용될 스펠 초기화 할지 말지 결정 로직
    TODO: 티어 1이상 재료 (idx >= 1) 는 매턴 1루피를 준다.
    TODO: Index 별 Naming 안되나.. ㅎㅎ
    
 **/
struct Actions {
    actions: Vec<Action>,
}
impl Actions {
    fn new<'a> (action_count: usize) -> Self {
        Self {
            actions: Vec::with_capacity(action_count),
        }
    }
    fn select_act(&self, witch: &Witch) -> Vec<&Action> {
        let brewable_acts = self.get_brewable_acts(&witch);
        if brewable_acts.len() > 0 {
            brewable_acts
        } else {
            let casts = self.get_brewable_casts(&witch);
            casts
        }
    }

    fn get_acts(&self, a_type: ActionType) -> Vec<&Action> {
        self.actions.iter().filter(|act| act.a_type == a_type).collect()
    }

    fn get_brewable_acts(&self, witch: &Witch) -> Vec<&Action> {
        let brews = self.get_acts(ActionType::Brew);
        
        let mut results: Vec<&Action> = Vec::new();
        brews.iter().for_each(|act| {
            let mut valid = true;
            for tier in 0..NUM_OF_GRADIENT_TYPES {
                let d = witch.grads.get(&tier).expect("Not Found I") + act.deltas[tier];
                valid = valid && d > 0; // 모든 delta 가 0 이 넘어야 한다. 
            };
        
            if valid {
                results.push(act.clone())
            }
        });
        results
    }

    fn get_close_to_brewable(&self, witch: Witch) -> Action {
        let cast_acts = self.get_acts(ActionType::Cast);
        let brew_acts = self.get_acts(ActionType::Brew);
        let mut result: Option<Action> = None;

        for i in 0..cast_acts.len() {
            let cast_act = cast_acts[i];
            let mut max_score = 0;
            let mut score = 0;
            for j in 0..brew_acts.len() {
                let brew_act = brew_acts[j];
                for (idx, delta) in brew_act.deltas.iter().enumerate() {
                    let d = *delta - cast_act.deltas[idx];
                    if d > *delta { // 각 재료가에 필요한 값이 줄어들면
                        score += d.abs();
                    }
                }
            }
            if score > max_score {
                max_score = score;
                result = Some(cast_act.clone());
            }            
                

        }
        result.expect("=get_close_to_brewable= 함수의 단 한개의 결과 값도 존재 하지 않습니다 ")
    }

    fn get_brewable_casts (&self, witch: &Witch) -> Vec<&Action> {
        let cast_acts = self.get_acts(ActionType::Cast);
        let castable_acts = cast_acts.iter().filter(|act| act.castable == true);

        let temp: Vec<&&Action> = castable_acts.clone().collect();
        let mut rest_act = Vec::with_capacity(1);
        if temp.len() == 0 {
            rest_act.push(&Action::new_rest());
            return rest_act
        }

        let mut results: Vec<&Action> = Vec::new();
        castable_acts.clone().for_each(|action| {
            let mut witch = witch.clone();
            for tier in 0..NUM_OF_GRADIENT_TYPES {
                let own = witch.grads.get(&tier).expect("HASH MAP Not Found I in temp witch");
                witch.grads.insert(tier, own + action.deltas[tier]);
            };
            if self.get_brewable_acts(&witch).len() > 1 {
                results.push(action.clone());
            }
        });   
        if results.len() == 0 { // Cast를 하더라도 생산이 불가능 할때
            let mut rng = thread_rng();
            let cast_vec:Vec<&&Action> = castable_acts.collect();
            let a = *cast_vec[rng.gen_range(0..=cast_vec.len())].clone();
            results.push(&a)
        }
        results     
    }
}


fn main() {
    let mut witch = Witch::new();
    // each index indicate tier, ex) [0, 2, 10, 0] -> tier2 = 10 개, ''1 = 2개
    loop {
        let mut input_line = String::new(); io::stdin().read_line(&mut input_line).unwrap(); let action_count = parse_input!(input_line, C);
        let mut actions = Actions::new(action_count as usize); 
        for i in 0..action_count as usize{
            let mut input_line = String::new(); io::stdin().read_line(&mut input_line).unwrap(); let inputs = input_line.split(" ").collect::<Vec<_>>();
            let action = Action::new(inputs, NUM_OF_GRADIENT_TYPES);
            actions.actions.push(action)
        };
        actions.actions.sort_by(|a, b| b.earn.cmp(&a.earn));            
        for i in 0..2 as usize {
            let mut input_line = String::new(); io::stdin().read_line(&mut input_line).unwrap(); let inputs = input_line.split(" ").collect::<Vec<_>>();
            if i == 0 { // i == 1 -> opponent
                witch.update(inputs);
            }
        }
        let selected_acts: Vec<&Action> = actions.select_act(&witch);
        selected_acts[0].print_act();
        // in the first league: BREW <id> | WAIT; later: BREW <id> | CAST <id> [<times>] | LEARN <id> | REST | WAIT
    }
}
