use std::io;

fn ends_with_digit(str: &str) -> Option<u32> {
    let lst = str.chars().last().unwrap();
    if lst.is_ascii_digit() {
        return lst.to_digit(10);
    }

    let arr = vec![
        "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    ];

    for (idx, word) in arr.iter().enumerate() {
        if str.ends_with(word) {
            return Some(u32::try_from(idx).unwrap() + 1);
        }
    }

    None
}

fn solve(input: String) -> u32 {
    let mut first: Option<u32> = None;
    let mut last: Option<u32> = None;
    for l in 0..input.len() {
        let pref = &input[0..=l];
        if let Some(dig) = ends_with_digit(pref) {
            last = Some(dig);
            if let None = first {
                first = Some(dig)
            }
        }
    }
    (first.unwrap() * 10) + last.unwrap()
}

fn main() {
    let mut sum = 0;
    for line in io::stdin().lines() {
        if let Ok(input) = line {
            sum += solve(input);
        }
    }
    println!("{}", sum);
}

#[test]
fn test() {
    assert_eq!(solve(String::from("two1nine")), 29);
    assert_eq!(solve(String::from("eightwothree")), 83);
    assert_eq!(solve(String::from("abcone2threexyz")), 13);
    assert_eq!(solve(String::from("xtwone3four")), 24);
    assert_eq!(solve(String::from("4nineeightseven2")), 42);
    assert_eq!(solve(String::from("zoneight234")), 14);
    assert_eq!(solve(String::from("7pqrstsixteen")), 76);
}
