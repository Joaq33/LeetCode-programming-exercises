///Done
struct Solution;

impl Solution {
    pub fn fizz_buzz(n: i32) -> Vec<String> {
        let mut ans = Vec::new();
        for number in 1..=n {
            let mut phrase: String = "".to_owned();
            if number % 3 == 0 {
                phrase += "Fizz"
            }
            if number % 5 == 0 {
                phrase += "Buzz"
            }
            if phrase == "" {
                ans.push(number.to_string())
            } else {
                ans.push(phrase)
            }
        }
        ans
    }

    // not optimal, just copied
    // pub fn fizz_buzz(n: i32) -> Vec<String> {
    //     let mut res = vec![];
    //     for i in 1..=n {
    //         let fizz = i % 3 == 0;
    //         let buzz = i % 5 == 0;
    //         let s = match (fizz, buzz) {
    //             (true, true) => "FizzBuzz".to_string(),
    //             (true, false) => "Fizz".to_string(),
    //             (false, true) => "Buzz".to_string(),
    //             (false, false) => format!("{}", i),
    //         };
    //         res.push(s);
    //     }
    //     res
    // }
}

fn main() {
    println!("{:?}", Solution::fizz_buzz(20));
}