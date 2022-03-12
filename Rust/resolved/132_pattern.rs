struct Solution;

impl Solution {
    pub fn find132pattern(nums: Vec<i32>) -> bool {
        let mut stack: Vec<i32> = Vec::new();
        let mut s3: i32 = -2147483647;
        for num in nums.iter().rev() {
            if num < &s3 {
                return true;
            }
            while !stack.is_empty() && stack.last().unwrap() < num {
                s3 = stack.drain(stack.len() - 1..).next().unwrap();
            }
            stack.push(*num)
        }
        false
    }
}


fn main() {
    println!("resultado: {:?}", Solution::find132pattern(vec![3, 1, 4, 2]));
}