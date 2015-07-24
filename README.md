# simbed
A simulink-like <b>dynamic system simulation</b> environment developed in .NET with IronPython engine embedded in it to provide extensibility.

<h3>Features</h3>
<ul>
    <li><b>Step-by-Step Simulation:</b> Simulation can be done in 2 ways. Continuous and Step-By-Step. In the latter, the system behavior can be observed in a step-by-step manner which gives a closer look at the working of the system.</li>
    <li><b>Real-Time I/O:</b> The system has real-time I/O capabilities for hardware-in-loop system simulation (e.g. Software Defined Radio, Simulation of a plant control models etc.)</li>
    <li><b>Extensibility:</b> Extensibility is required to add new blocks or functionalities to the simulation environment. New functionalities can be developed using Python or any .NET compatible languages (e.g. C#, Visual Basic .NET etc.) and can be added to the tool simply by copying the files containing new functionalities into appropriate system folders.</li>
    <li><b>Exporting:</b> Once the user is done with simulating a module, he may want to reuse it as a part of a larger system this allows him to simplify the design of the larger system. For this reason, Simbed allows any system to be exported as a single block for later use. This block is called “Derived Block” and is inserted into a package “User”. </li>
</ul> 

<h3>Installation</h3>
Simbed has no installation package as of now. Simply extracting the zip file will work. 

<h3>Usage</h3>
Simbed provides 5 keywords to explain almost any system. Those are <b>assume</b>, <b>as</b>, <b>let</b>, <b>be</b>, <b>connect</b> and <b>to</b>.

<h3> Samples</h3>
Usage examples are given in the Samples folder. Be sure to check out.

