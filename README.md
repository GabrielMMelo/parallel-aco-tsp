# ACO-TSP :ant:

Parallel Ant Colony Optimization algorithm applied to the Traveller Sale Problem.

#### What were parallelized?

- The processing of ants was splited out into ant's chunks which are processed by the number of given processors.


## Requirements

- Install openMPI
```shell
sudo apt install libopenmpi-dev
```

- Create a virtualenv
```
virtualenv aco-tsp
source aco-tsp/bin/activate
pip install -r requirements.txt
```


## How to use?

For execution with 4 processes:
```
mpiexec -n 4 python main.py 1
```
