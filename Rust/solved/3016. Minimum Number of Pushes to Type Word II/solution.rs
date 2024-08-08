struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn minimum_pushes(word: String) -> i32 {
        let mut count_map: HashMap<char, usize> = HashMap::new();
        for item in word.chars() {
            // println!("{:?}",item);
            let cur_item = count_map.entry(item).or_insert(0);
            *cur_item += 1;
        }

        let mut count_vec: Vec<(&char, &usize)> = count_map.iter().collect();
        println!("{:?}", count_vec);
        count_vec.sort_by(|a, b| b.1.cmp(a.1));
        println!("Sorted: {:?}", count_vec);

        let mut ans = 0usize;
        for (i, (k, v)) in count_vec.iter().enumerate() {
            println!("Sorted: {:?},{:?} = {:?}", i / 8, k, v);
            ans += (i / 8 + 1) * *v
        }
        ans as i32
    }
}

//         let char_counts = word.chars().collect::<Counter<_>>();
//         println!("char_counts {:?}", char_counts);
//         let most = char_counts.most_common_ordered();
//
//         println!("{:?}", most);
//         let mut ans = 0;
//
//         for (i, item) in most.iter().enumerate(){
//             println!("The {}th item is {:?}, {:?}", i, item, (i/8+1)*item.1);
//             ans+=(i/8+1)*item.1
//         }
//
//         ans as i32
// }#!/usr/bin/env cargo eval --
// //! ```cargo
// //! [dependencies]
// //! counter = "0.6.0"
// //! ```
//
// struct Solution;
//
// extern crate counter;
// use counter::Counter;
//
// impl Solution {
//     pub fn minimum_pushes(word: String) -> i32 {
//
//         let char_counts = word.chars().collect::<Counter<_>>();
//         println!("char_counts {:?}", char_counts);
//         let most = char_counts.most_common_ordered();
//
//         println!("{:?}", most);
//         let mut ans = 0;
//
//         for (i, item) in most.iter().enumerate(){
//             println!("The {}th item is {:?}, {:?}", i, item, (i/8+1)*item.1);
//             ans+=(i/8+1)*item.1
//         }
//
//         ans as i32
//     }
// }

fn main() {
    println!("{:?}", Solution::minimum_pushes(String::from("aabbccddeeffgghhiiiiii")));
}