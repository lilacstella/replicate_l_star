# L* Replication

[Learning regular sets from queries and counterexamples](https://www.sciencedirect.com/science/article/pii/0890540187900526?via%3Dihub)

## Setup
This module depends on the "automathon" library that uses graphviz to visualize the DFA that we genereate. 


To use the `graphviz` library, we need the executable of the same name on our path. For mac, 

```shell
brew install graphviz
```

In the python environment for this project
```shell
pip install -r requirements.txt
```

To run the project, in the root of this repository 
```shell
python -m l_star
```

## Output
In the console, the module will repeatedly ask for membership information for specific strings. After a DFA is ready, the program will automatically generate two files. The image visualization of `DFA.gv.png` as well as the plain text description of the graph in `DFA.gv` in the location of the command execution. Afterwards, continue following the prompt to either confirm the DFA or provide a counter example that does not fit in the proposed DFA. 

## Further Configuration
Refer to the `__init__.py` file to configure the alphabet that we are generating for. 
