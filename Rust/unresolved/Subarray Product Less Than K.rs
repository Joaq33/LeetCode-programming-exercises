///Done
struct Solution;

impl Solution {
    pub fn num_subarray_product_less_than_k(nums: Vec<i32>, k: i32) -> i32 {
        if k == 0 || k == 1 {
            return 0;
        }
        let mut ans: usize = 0;
        let mut start: usize = 0;
        let mut prod: i32 = 1;

        for index in 0..nums.len(){
            prod *= nums[index];
            while prod >= k {
                prod /= nums[start];
                start += 1;
            }
            ans += index - start + 1;
        }
        return ans as i32;
    }
}

fn main() {
    println!("{:?}", Solution::num_subarray_product_less_than_k([10, 5, 2, 6].to_vec(), 100));
}