use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}
const MAX_W: i32 = 6999;
const MAX_H: i32 = 3000;
const GRAVITY: f32 = 3.711;
// V speed For a landing to be successful,
const MAX_DY: i32 = 40;
const MAX_DX: i32 = 20;
const MARGIN_SPEED: i32 = 5;

//

#[derive(Debug, Clone, Copy)]
struct Coord (i32, i32); // x, y

#[derive(Debug)]
struct SurFace { coord: Coord}
#[derive(Debug)]
struct Speed<T> { // vertical, horizantal
    v: T, h: T
}
#[derive(Debug)]
struct Ship<'a> {
    target_points: Option<( &'a SurFace, &'a SurFace)>,
    coord: Coord,
    speed: Speed<i32>,
    fuel: i32,
    rotate: i32, // the rotation angle in degrees (-90 to 90).
    power: i32 // 0 ~ 4
}
impl<'a> Ship<'a> {
    fn new () -> Self {
        Self {
            coord: Coord (MAX_W, MAX_H),
            speed: Speed {v: 0, h: 0},
            fuel: 0,
            rotate: 0,
            power: 0,
            target_points: None,
        }
    }
    /// get current speed
    /// return (Horizantal Speed, Vertical Speed)
    fn curr_speed (&self) -> Speed<f32> {
        let r = self.rotate as f32;
        let degree = r * (3.14 / 180.0);
        Speed { 
            h: degree.cos(),
            v: degree.sin()
        }
    }
    fn is_wrong_direction (&self) -> bool {
        let ps = self.target_points.as_ref().expect("Target Points is None1");
        let x = self.coord.0;
        let target_left_x = ps.0.coord.0;
        let target_right_x = ps.1.coord.0;
        (x < target_left_x && self.speed.h < 0) || // x 가 목표지점 왼쪽에 있지만 속도가 왼쪽으로 향할때
        (x > target_right_x && self.speed.h > 0 ) // x가 목표지점 오른쪽에 있지만 속도가 오른쪽을 향할때
    }
    /// returns the best angle to slow down marse lander
    /// the angle directing thrust in the opposition direction to the mvmt)
    fn angle_to_slow (&self) -> i32 {
        let s = &self.speed;
        let hypoten = (s.h * s.h) + (s.v * s.v);
        let ratio_sin: f32 = (s.h / hypoten) as f32;
        // asin: y축에 대한 각도 
        let radian: f32 = ratio_sin.asin() * ( 3.14 / 180.0);
        radian.floor() as i32

    }
    fn angle_to_aim (&self) -> i32 {
        let angle = ((GRAVITY / 4.0).acos() * (3.14 / 180.0)).floor() as i32;
        let (x, y) = (self.coord.0,  self.coord.1);
        let ps = self.target_points.as_ref().expect("Target Points is None1");
        let (x1, y1) = (ps.0.coord.0,  ps.0.coord.1);
        let (x2, y2) = (ps.1.coord.0,  ps.1.coord.1);        
        if x < x1  { 
            -angle
        } else if x2 < x { 
            angle
        } else {
            0
        }   
    }

    fn update (&mut self) {
        let mut input_line = String::new(); io::stdin().read_line(&mut input_line).unwrap();
        let inputs = input_line.split(" ").collect::<Vec<_>>();
        self.coord = Coord (
            parse_input!(inputs[0], i32),
            parse_input!(inputs[1], i32)
        );
        self.speed = Speed { // can be negative
            h: parse_input!(inputs[2], i32),
            v: parse_input!(inputs[3], i32),
        };
        self.fuel = parse_input!(inputs[4], i32); // the quantity of remaining fuel in liters.
        self.rotate = parse_input!(inputs[5], i32);
        self.power = parse_input!(inputs[4], i32);
    }
    fn moving (&self) {
        let (mut rotate, mut power) = (self.angle_to_aim(), 4);  // rotate power
        if self.is_wrong_direction() {
            rotate = self.angle_to_slow();
        } else if rotate == 0 {
            power = 3
        }
        
        
        println!("{} {}", rotate, power)
    }   
}
fn new_surfaces () -> Vec<SurFace> {
    let mut input_line = String::new(); io::stdin().read_line(&mut input_line).unwrap();
    let n = parse_input!(input_line, i32);
    let mut v: Vec<SurFace> = Vec::new();
    for i in 0..n as usize {
        let mut input_line = String::new(); io::stdin().read_line(&mut input_line).unwrap();
        let inputs = input_line.split(" ").collect::<Vec<_>>();
        v.push(SurFace{
            coord: Coord( // By linking all the points together in a sequential fashion, you form the surface of Mars.
                parse_input!(inputs[0], i32),
                parse_input!(inputs[1], i32)
            )
        })    
    }
    v 
}

fn main() {
    let sfs = new_surfaces(); // 그냥 점들의 집합으로 연결하여 표면 완성
    let mut ship = Ship::new();
    let mut prev = &sfs[0];
    for s in sfs[1..].iter() {
        if s.coord.1 == prev.coord.1 {
            ship.target_points = Some((prev, s));
            break;
        } else {
            prev = s
        }
    }



    // game loop
    loop {
        ship.update();
        ship.moving();
    }
}
