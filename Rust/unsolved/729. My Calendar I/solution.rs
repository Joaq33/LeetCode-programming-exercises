struct MyCalendar {
    bookings: Vec<(i32, i32)>,
}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyCalendar {

    fn new() -> Self {
        let bookings = vec![(-1,-1), (i32::MAX,i32::MAX)];
        // let bookings = [(-1,-1), (f32::Infinity,f32::Infinity)];
        Self { bookings }
    }

    fn book(&self, start: i32, end: i32) -> bool {
        println!("{:?}", self.bookings);
        true
    }
}


fn main() {
    // let asd:i32 = i32::MAX;
    // println!("{:?}", asd);
    let obj = MyCalendar::new();
    let start = 5;
    let end = 10;
    let ret_1: bool = obj.book(start, end);
}