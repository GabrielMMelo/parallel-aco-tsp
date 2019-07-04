# parallel-aco-tsp :ant:

**Parallel** Ant Colony Optimization (ACO) algorithm applied to the Traveller Salesman Problem (TSP).

#### What were parallelized?

- The processing of ants was splited out into ant's chunks which are processed by the number of given processors.

## Structure
```shell
.
├── aco_parallel.py        # parallel version
├── aco.py                 # sequential version
├── datasets/              # input datasets
├── main.py
├── output/                # output of utils/scripts_{parallel,sequential}
├── plot.py                # for plotting purpose
├── README.md
├── requirements.txt
└── utils/
    ├── script_parallel    # get parallel execution time 
    └── script_sequential  # get sequential execution time
```


## Requirements

- Install openMPI
```shell
sudo apt install libopenmpi-dev python3-tk
```

- Create a virtualenv
```
virtualenv aco-tsp
source aco-tsp/bin/activate
pip install -r requirements.txt
```


## How to use?

For execution with **4 processes**:
```
mpiexec -n 4 python main.py --parallel
```

To use the sequential algorithm instead, just run:
```shell
python main.py
```
