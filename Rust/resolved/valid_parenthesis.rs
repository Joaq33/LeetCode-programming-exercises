use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack = Vec::new();
        let mut closing_equivalent: HashMap<char, char> = HashMap::new();
        closing_equivalent.insert('(', ')');
        closing_equivalent.insert('[', ']');
        closing_equivalent.insert('{', '}');

        for letter in s.chars() {
            if "([{".contains(letter) {
                stack.push(letter)
            } else {
                if stack.is_empty() {
                    return false;
                }
                let ultima = stack.pop();
                if closing_equivalent[&ultima.unwrap()] != letter {
                    return false;
                }
            }
        }
        return stack.is_empty();
    }
}

fn main() {
    println!("{:?}", Solution::is_valid("()()[]".to_string()));
}