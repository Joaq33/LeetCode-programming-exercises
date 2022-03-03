///copied
struct Solution;

impl Solution {
    /// not optimal, just copied
    pub fn fizz_buzz(n: i32) -> Vec<String> {
        let mut res = vec![];
        for i in 1..=n {
            let fizz = i % 3 == 0;
            let buzz = i % 5 == 0;
            let s = match (fizz, buzz) {
                (true, true) => "FizzBuzz".to_string(),
                (true, false) => "Fizz".to_string(),
                (false, true) => "Buzz".to_string(),
                (false, false) => format!("{}", i),
            };
            res.push(s);
        }
        res
    }
}

fn main() {
    println!("{:?}", Solution::fizz_buzz(20));
}