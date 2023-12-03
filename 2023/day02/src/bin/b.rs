use std::io;

#[derive(Debug, Clone, Copy)]
struct RoundInfo {
    red: i32,
    green: i32,
    blue: i32,
}

impl RoundInfo {
    fn combine(self: &Self, other: &RoundInfo) -> RoundInfo {
        RoundInfo {
            red: self.red.max(other.red),
            green: self.green.max(other.green),
            blue: self.blue.max(other.blue),
        }
    }

    fn power(self: &Self) -> i32 {
        self.red * self.green * self.blue
    }
}

fn parse_round(str: &str) -> Option<RoundInfo> {
    let mut round = RoundInfo {
        red: 0,
        green: 0,
        blue: 0,
    };

    for pair_str in str.split(", ") {
        let mut pair = pair_str.splitn(2, ' ');
        let cnt: i32 = pair.nth(0)?.parse().ok()?;

        match pair.nth(0)? {
            "red" => round.red = cnt,
            "green" => round.green = cnt,
            "blue" => round.blue = cnt,
            _ => (),
        }
    }

    Some(round)
}

fn parse_game(str: &str) -> Vec<RoundInfo> {
    str.splitn(2, ": ")
        .nth(1)
        .unwrap()
        .split("; ")
        .filter_map(|s| parse_round(s))
        .collect()
}

fn main() {
    let input = io::read_to_string(io::stdin()).unwrap();
    let sum: i32 = input
        .lines()
        .map(|str| {
            parse_game(str)
                .into_iter()
                .reduce(|a, b| a.combine(&b))
                .unwrap()
                .power()
        })
        .sum();
    println!("{}", sum);
}
