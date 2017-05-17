# Reverse-Polish-Notation-Calc
This is a RPN calculator implemented in Python using OOP. 

Iterations to be saved for clarity in interaction and expended math functions. 

Future work could include implementing complex mathmatical functions and expressions.

----

Say we want to calculate the value resulting from the calculation: `6 + ((5 + 3) / 4) - 3`. In RPN, that calculation is written: `6 5 3 + 4 / + 3 −`. To input this calculation into a RPN calculator, one would enter those elements (in turn), and the corresponding operations would occur in the following order.


| Input |  Operation   |    Stack    |                   Other                   |
|:-----:|:------------:| ----------- |:-----------------------------------------:|
|   6   |  Push Value  | [ 6 ]       |                                           |
|   5   |  Push Value  | [ 6, 5 ]    |                                           |
|   3   |  Push Value  | [ 6, 5, 3 ] |                                           |
|   +   |     Add      | [ 6, 8 ]    | Pop two values (3 then 5), push result, 8 |
|   4   |  Push Value  | [ 6, 8, 4 ] |                                           |
|   /   |    Divide    | [ 6, 2 ]    | Pop two values (8 then 4), push result, 2 |
|   +   |     Add      | [ 8 ]       | Pop two values (2 then 6), push result, 8 |
|   3   |  Push Value  | [ 8, 3 ]    |                                           |
|   -   |   Subtract   | [ 5 ]       | Pop two values (3 then 8), push result  5 |
|       |    Return    |   5         |                                           |

__note__  
If you wanted to do 5 + 5 + 5 you'd do 5 5 5 + + __not__ 5 5 5 +  

Wiki on how these guys work is available [here](https://en.wikipedia.org/wiki/Reverse_Polish_notation)

An interactive RPN can be found [here](http://www.meta-calculator.com/learning-lab/reverse-polish-notation-calculator.php)
