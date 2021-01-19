Dynamic Allocation and Coordination of Resources and Volunteers in Humanitarian Crises
===============
This repository contains the source code and results discussed in my research paper [Dynamic Resource Allocation and Coordination for High-Load Crisis Volunteer Management](https://www.emerald.com/insight/content/doi/10.1108/JHLSCM-02-2018-0019/full/html)
written together with coauthors [Ghaith Rabadi](https://www.odu.edu/directory/people/g/grabadi) and [Femida Handy](https://www.sp2.upenn.edu/people/view/femida-handy/). 
Humanitarian crises unfold unpredictably, and plans often need to be readjusted on an ongoing basis as more
information comes to light in the aftermath. Crisis responses need to be put together with very little time to plan and require coordination of many types of resources (including 
renewable resources such as bulldozers and consumable resources such as water) as well as paid staff and volunteers with differing skills and capabilities. 

#### Solution Approach
In this work we develop a multi-objective mixed integer programming (MIP) framework for optimally allocating and re-allocating resources and personnel with different skills in a crisis. This 
framework also takes into account a wide variety of volunteer constraints such as availability, skills, the need to work with specific individuals or in groups, and more. 
Rather than relying on stochastic characterizations of the changing needs (which requires data not often available until the crisis is over) this framework allows for re-planning
in a way that best meets the new demands while minimizing the disruption to current plans. We showed that MIP is capable in practice of solving both the initial planning problem
as well as the re-planning in very short amounts of time for realistically large problems covering a wide variety of characteristics.


#### Code Organization and How to Run
The code in this repository is organized as follows: 

* *models* - contains the MIP models in OPL format
* *params* - contains the parameter files for generating problem classes and running the experiments. The *base* subfolder contains the parameters for experiments without
              transportation concerns, and the *transp* subfolder contains parameters for experiments involving transportation.
* *solutions* - contains the output from the experiments, using the same subfolder structure as above.
* *src* - contains the main Python source code.
* *test* - contains code used for testing. 

The file *run_experiments.bat* allows the experiments to be re-run on a Windows machine. To run on another OS just open this file and manually
run the python and file deletion commands in the order specified, or else simply copy them into a new script and run. As an additional note, this
code was written before [DOcplex](https://ibmdecisionoptimization.github.io/docplex-doc/) was widely used and therefore requires the CPLEX solver output
format to be the same as CPLEX 12.4. You may need to make small changes to the ProblemExecutor.opl_solve method in the
[/data/experiment_runner.py](https://github.com/chrisgarcia001/Crisis-Volunteer-Resource-Allocation/blob/main/src/experiment_runner.py) file for later
versions of CPLEX.

#### Paper and Citation
The full paper can be found [here.](https://www.emerald.com/insight/content/doi/10.1108/JHLSCM-02-2018-0019/full/html)
If you wish to cite this work, please use the following reference:
Garcia C., Rabadi. G., and Handy, F. (2018), "Dynamic resource allocation and coordination for high-load crisis volunteer management", *Journal of Humanitarian Logistics and Supply Chain Management*, Vol. 8 No. 4, pp. 533-556.

