# Algorithms and data structures

Brendan Herger, drafted 2020-04-30

**tl;dr:** TODO

Most CS programs feature a data structures and algorithms course, and most software engineering / DS interviews focus 
on these skills heavily. Every few years, I like to revisit this coursework, and implement some fundamental algorithms 
and data structures by hand. A decent engineer would never do this in prod code, but it's a helpful excercise for 
prepping for interviews, shifting into more granular work, or killing time.  

## Quick start

```bash
# Install requirements
pip install -r requirements.txt

# Run tests on reference implementations
python -m unittest discover -p test_reference_implementation.py

# Run tests on your solutions (this command will show test failures, until solutions are implemented)
python -m unittest discover -p test_solution.py

# Start learning, and implement an algorithm
open algorithms/linked_list/solution.py
```

## Usage

Each base folder contains five files:

 - `interface.py`: The bear bones methods necessary for the data structure
 - `solution.py`: A blank canvas, to be filled in (probably by you, or maybe by your students)
 - `test_solution.py`: A series of simple tests to confirm that the data structure performs as expected. These are likely not exhaustive. 
 - `reference_implementation.py`: A sample implementation, which balances pithiness, readability, and run time. It likely is not fully optimized, and is only one of many acceptable implementations.
 - `test_reference_implementation.py`: The exact same tests as in `test_solution.py`, but testing the reference_implementation
 
I would recommend tackling algorithms in the following order, and implementing the class in `solution.py`. 

 - `linked_list`
 - `queue`
 - `stack` (might look similar to queue)
 - `min_heap`

To run the tests for a single algorithm, you can use the command below (replacing `linked_list` with the relevant algorithm): 
```commandline
python -m unittest algorithms.linked_list.test_solution
```

To run the tests for all algoriths, you can use the command below:
```commandline
python -m unittest discover -p test_solution.py
```


## Contact

Hey, I'm Brendan Herger, avaiable at [https://www.hergertarian.com/](https://www.hergertarian.com/). Please feel free 
to reach out to me at `13herger <at> gmail <dot> com`

I enjoy bridging the gap between data science and engineering, to build and 
deploy data products. I'm not currently pursuing contract work. 

I've enjoyed building a unique combination of machine learning, deep learning, and software engineering skills. In my 
previous work at Capital One and startups, I've has built authorization fraud, insider threat, and legal discovery 
automation platforms. In each of these cases I've lead a team of data scientists and data engineers to enable and 
elevate our client's business workflow (and capture some amazing data).

When I'm not knee deep in a code base, I can be found traveling, sharing my collection of Japanese teas, and playing 
board games with my partner in Seattle. 

## Changelog

### Development

### 1.0

 - Added `README.md`
 - Added `linked_list`, `queue`, `stack`, and `min_heap`
