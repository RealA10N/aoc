use std::io;

#[derive(Debug, Clone, Copy)]
struct RoundInfo {
    red: u32,
    green: u32,
    blue: u32,
}

impl RoundInfo {
    fn is_possible(self: Self) -> bool {
        self.red <= 12 && self.green <= 13 && self.blue <= 14
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
        let cnt: u32 = pair.nth(0)?.parse().ok()?;

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
    let mut sum = 0;
    for (idx, game) in input.lines().map(|str| parse_game(str)).enumerate() {
        if !game.iter().any(|r| !r.is_possible()) {
            sum += idx + 1;
        }
    }
    println!("{}", sum);
}
