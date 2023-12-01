use std::io;

fn main() {
    let input = io::read_to_string(io::stdin()).unwrap();
    let mut s = 0;
    for line in input.lines() {
        let digits: Vec<char> = line.chars().filter(|c| c.is_ascii_digit()).collect();
        let a = digits[0].to_digit(10).unwrap();
        let b = digits[digits.len() - 1].to_digit(10).unwrap();
        s += (a * 10) + b;
    }
    println!("{}", s);
}
