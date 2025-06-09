use std::{
    fmt::Write,
    io::{self, Read},
    ops::RangeInclusive,
};

struct SegmentTree {
    tree: Vec<i32>,
    n: usize,
}

impl SegmentTree {
    pub fn new(x: &Vec<i32>) -> Self {
        let tree_size = x.len().next_power_of_two() << 1;
        let mut tree = Self {
            tree: vec![1; tree_size],
            n: x.len(),
        };

        tree.build(x);

        tree
    }

    pub fn build(&mut self, x: &Vec<i32>) {
        self._build(x, 0, self.n - 1, 1);
    }

    pub fn update(&mut self, idx: usize, value: i32) {
        self._update(0, self.n - 1, idx, value, 1);
    }

    pub fn query(&self, range: &RangeInclusive<usize>) -> i32 {
        return self._query(0, self.n - 1, range, 1);
    }

    fn _build(&mut self, x: &Vec<i32>, start_idx: usize, end_idx: usize, tree_idx: usize) {
        if tree_idx >= self.tree.len() {
            return;
        }

        if start_idx == end_idx {
            self.tree[tree_idx] = x[start_idx];
            return;
        }

        let mid_idx = (start_idx + end_idx) / 2;
        let left_child_idx = tree_idx * 2;
        let right_child_idx = tree_idx * 2 + 1;

        self._build(x, start_idx, mid_idx, left_child_idx);
        self._build(x, mid_idx + 1, end_idx, right_child_idx);

        self.tree[tree_idx] = self.tree.get(left_child_idx).unwrap_or(&1)
            * self.tree.get(right_child_idx).unwrap_or(&1);
    }

    fn _update(
        &mut self,
        start_idx: usize,
        end_idx: usize,
        idx: usize,
        value: i32,
        tree_idx: usize,
    ) {
        if start_idx == end_idx {
            self.tree[tree_idx] = value;
            return;
        }

        let mid_idx = (start_idx + end_idx) / 2;

        if idx <= mid_idx {
            self._update(start_idx, mid_idx, idx, value, tree_idx * 2);
        } else {
            self._update(mid_idx + 1, end_idx, idx, value, tree_idx * 2 + 1);
        }

        self.tree[tree_idx] = self.tree.get(tree_idx * 2).unwrap_or(&1)
            * self.tree.get(tree_idx * 2 + 1).unwrap_or(&1);
    }

    fn _query(
        &self,
        start_idx: usize,
        end_idx: usize,
        query_range: &RangeInclusive<usize>,
        tree_idx: usize,
    ) -> i32 {
        let mid_idx = (start_idx + end_idx) / 2;

        if tree_idx >= self.tree.len() {
            return 1;
        }

        if *query_range.start() > end_idx || *query_range.end() < start_idx {
            return 1;
        }

        if *query_range.start() <= start_idx && end_idx <= *query_range.end() {
            return self.tree[tree_idx];
        }

        let left_child_idx = tree_idx * 2;
        let right_child_idx = tree_idx * 2 + 1;
        let left = self._query(start_idx, mid_idx, query_range, left_child_idx);
        let right = self._query(mid_idx + 1, end_idx, query_range, right_child_idx);

        left * right
    }
}

enum Command {
    Change { idx: usize, value: i32 },
    Product { i: usize, j: usize },
}
fn main() {
    let mut buf = String::new();
    io::stdin().read_to_string(&mut buf).unwrap();
    let mut iter = buf.trim().split_ascii_whitespace().peekable();

    loop {
        let n: usize = iter.next().unwrap().parse().unwrap();
        let k: usize = iter.next().unwrap().parse().unwrap();

        let mut x: Vec<i32> = Vec::new();

        for _ in 0..n {
            x.push(iter.next().unwrap().parse::<i32>().unwrap().signum());
        }

        let mut commands: Vec<Command> = Vec::new();

        for _ in 0..k {
            let cmd_type = iter.next().unwrap();
            let command: Command = match cmd_type {
                "C" => Command::Change {
                    idx: iter.next().unwrap().parse::<usize>().unwrap() - 1,
                    value: iter.next().unwrap().parse::<i32>().unwrap().signum(),
                },
                "P" => Command::Product {
                    i: iter.next().unwrap().parse::<usize>().unwrap() - 1,
                    j: iter.next().unwrap().parse::<usize>().unwrap() - 1,
                },
                _ => unreachable!(),
            };

            commands.push(command);
        }

        println!("{}", solution(x, commands));

        if iter.peek() == None {
            break;
        }
    }
}

fn solution(x: Vec<i32>, commands: Vec<Command>) -> String {
    let mut tree = SegmentTree::new(&x);
    let mut answer = String::new();

    for command in commands {
        match command {
            Command::Change { idx, value } => {
                tree.update(idx, value);
            }
            Command::Product { i, j } => {
                let res = tree.query(&(i..=j));
                write!(&mut answer, "{}", ["-", "0", "+"][(res + 1) as usize]).unwrap();
            }
        }
    }

    answer
}
