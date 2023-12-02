use std::fs::read_to_string;

fn main() {
    let input = read_lines("src/inputs/01.txt");
    println!("Solution part 1: {}", solve_1(input.clone()));
    println!("Solution part 2: {}", solve_2(input));
}

fn solve_1(input: Vec<String>) -> u32 {
    input.iter()
        .map(|line| get_num_for_line(line))
        .sum()
}

fn solve_2(input: Vec<String>) -> u32 {
    let replaced_str: Vec<String> = input.iter()
        .map(|line| replace_chars_with_digits(line.to_string()))
        .collect();

    solve_1(replaced_str)
}

fn replace_chars_with_digits(v: String) -> String {
    v
        .replace("one", "one1one")
        .replace("two", "two2two")
        .replace("three", "three3three")
        .replace("four", "four4four")
        .replace("five", "five5five")
        .replace("six", "six6six")
        .replace("seven", "seven7seven")
        .replace("eight", "eight8eight")
        .replace("nine", "nine9nine")
}

fn get_num_for_line(line: &str) -> u32 {
    let digits: Vec<char> = line.chars()
        .filter(|c| c.is_digit(10))
        .collect();

    format!("{}{}", digits.first().unwrap().to_string(), digits.last().unwrap().to_string()).parse::<u32>().unwrap()
}

fn read_lines(filename: &str) -> Vec<String> {
    let mut result = Vec::new();

    for line in read_to_string(filename).unwrap().lines() {
        result.push(line.to_string())
    }

    result
}
