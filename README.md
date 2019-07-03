# parallel-aco-tsp :ant:

**Parallel** Ant Colony Optimization (ACO) algorithm applied to the Traveller Salesman Problem (TSP).

#### What were parallelized?

- The processing of ants was splited out into ant's chunks which are processed by the number of given processors.


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
mpiexec -n 4 python main.py 1
```

> The `1` is used to say to the program to use the parallel aco algorithm. For sequential process use `0` instead.
