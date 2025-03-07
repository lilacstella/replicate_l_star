# L* Replication

This repo is a replication of the L* algorithm as described in the paper
[Learning regular sets from queries and counterexamples](https://www.sciencedirect.com/science/article/pii/0890540187900526?via%3Dihub)

## Output
In the console, the module will repeatedly ask for membership information for specific strings. 
After a DFA is ready, the program will automatically generate two files. 

The image visualization of `DFA.gv.png` as well as the plain text description of the graph in `DFA.gv` 
in the location of the command execution. Afterwards, continue following the prompt to either confirm the DFA or 
provide a counter example that does not fit in the proposed DFA.

## External dependencies
This module depends on the graphviz library to visualize the DFA that we genereate.
To use the `graphviz` library, we need the executable of the same name on our path. For mac, 

```shell
brew install graphviz
```

For other operating systems, refer to the [Graphviz download page](https://graphviz.org/download/)

## Quick start to use the implementation of the L* algorithm
In a python environment, 
```sh
pip install git+https://github.com/lilacstella/replicate_l_star.git
python -c "import l_star; l_star.l_star()"
```

There can be further configuration of the alphabet by overwriting `l_star.alphabet`. 
It is currently a set of string of characters in the alphabet. 
## Developmental Set Up
In the python environment for this project
```shell
pip install -r requirements.txt
```

To run the project, in the root of this repository 
```shell
python -m l_star
```

## Further Configuration
Refer to the `__init__.py` file to configure the alphabet that we are generating for. 
