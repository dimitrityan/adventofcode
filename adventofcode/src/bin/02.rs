use std::fs::read_to_string;

fn main() {
    let input = read_lines("src/inputs/02.txt");
    println!("Solution part 1: {}", solve_1(input.clone()));
    println!("Solution part 2: {}", solve_2(input));
}

fn solve_1(input: Vec<String>) -> u32 {
    input.iter()
        .map(|l| map_to_num_color(l))
        .enumerate()
        .map(|(i, t)| map_possible_game_id((i.try_into().unwrap(), t)))
        .sum()
}

fn solve_2(input: Vec<String>) -> u32 {
    input.iter()
        .map(|l| map_to_num_color(l))
        .map(|l| map_min_num(l))
        .sum()
}

fn map_min_num(draws: Vec<Vec<(u32, &str)>>) -> u32 {
    let mut red: u32 = 0;
    let mut green = 0;
    let mut blue = 0;

    for subset in draws {
        for (count, color) in subset {
            match color {
                "red" => if count > red { red = count }
                "green" => if count > green { green = count }
                "blue" => if count > blue { blue = count }
                _ => ()
            }
        }
    }

    red * green * blue
}

fn map_possible_game_id((i, draws): (u32, Vec<Vec<(u32, &str)>>)) -> u32 {
    for subset in draws {
        for (count, color) in subset {
            match color {
                "red" => if count > 12 { return 0 }
                "green" => if count > 13 { return 0 }
                "blue" => if count > 14 { return 0 }
                _ => ()
            }
        }
    }

    i + 1
}

fn map_to_num_color(line: &str) -> Vec<Vec<(u32, &str)>> {
    line
        .split(":").collect::<Vec<&str>>()[1]
        .trim()
        .split(";")
        .map(|subset| split_subset(subset))
        .collect::<Vec<Vec<(u32, &str)>>>()
}

fn split_subset(subset: &str) -> Vec<(u32, &str)> {
    subset
        .trim()
        .split(",")
        .map(|draw| get_count_color_tup(draw))
        .collect::<Vec<(u32, &str)>>()
}

fn get_count_color_tup(draw: &str) -> (u32, &str) {
    let d = draw
        .trim()
        .split(" ")
        .collect::<Vec<&str>>();
    (d[0].parse::<u32>().unwrap(), d[1])
}

fn read_lines(filename: &str) -> Vec<String> {
    let mut result = Vec::new();

    for line in read_to_string(filename).unwrap().lines() {
        result.push(line.to_string())
    }

    result
}