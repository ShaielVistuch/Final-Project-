# Final Project<br/>
Readme includes: Instructions on how to run the code, a short explanation on the required background information as well as the code itself, and a screenshot of the result from the code.  **For a more detailed explantion see the pdf file**. <br/> 
## How to run the code<br/>
You need to download the numpy library version 1.26.4 via PyChar Python Packages window or using the command:<br/>
pip install numpy==1.26.4<br/>
To run the program, simply run the main function. <br/>

## Background explanation<br/>
Each graph represents the state of the activators and inhibitors (repressors) of the component c in check. <br/>
 
![image](https://github.com/user-attachments/assets/741bf3f0-3705-472c-96fc-8aed1196f82e)

<br/>In the given table, each row represents a certain Boolean function. Looking at each row, wherever the box is red – it means that in during the state described by the corresponding graph, the regulated component is active.<br/>
For example, if we look at the row marked with 0: We can infer that the regulated component is active only if all >the activators are present. and none of the repressors are present.<br/>
If we look at the row marked with 1: We can infer that the regulated component is active only if:<br/>
1)	All the activators are present and none of the repressors are present, OR<br/>
2)	Some but not all the activators are present, and none of the repressors are present.<br/>

In a similar matter we can go over each regulation condition at the table. <br/><br/>
**Monotonic property**: if a regulated component is active, and one of its activators switches from inactive to active, the regulated component will remain active. Similarly, if a regulated component is inactive, and one of its inhibitors switches from inactive to active, the regulated component will remain inactive.

## Code explanation<br/>
First, we made a list corresponding to each of the states describbed in the first row of the table. Each of the list items was created in a way to resamble the original graphs at the table and represents their meaning. For example:<br/>
![image](https://github.com/user-attachments/assets/22b3eead-5145-4994-aac7-53afc65ccd3e)
<br/>The function _generate_possible_functions_ returns a list, whose items are all the possible combinations to make a list using just of 0 and 1. The length of each generated 0s-and-1s list is given as a parameter. The number 1 is used to represent active component, the number 0 is used to represent inactive component. <br/>
We then must remove the functions [1, 1, 1, 1, 1, 1, 1, 1, 1], and [0, 0, 0, 0, 0, 0, 0, 0, 0], since they correspond to the case were the regulated component remains always active\ always inactive regardless of the state of its activators and repressors. 
<br/><br/>Afterwards, using the function find_monotonic_functions we iterate over each function. For each function, we iterate over its value in each of the states described by the graphs. If we find a situation where the regulated component is active (equal to 1), we also must check if when its activators switches from inactive to active, the regulated component remains active. Similarly, if we find a situation where the regulated component is inactive (equal to 0), we must check if when one of its inhibitors switches from inactive to active, the regulated component remains inactive. The function _find_monotonic_functions_ takes the list of all possible functions, as well as the list of all the different states of the activators and repressors, as inputs. It returns a list of all the monotonic functions. <br/>
Throughout the iteration over a function, we maintain a Boolean flag variable named _monotonic_. If we find a case where the monotonic property doesn’t hold, we change this flag variable from True to False, and break from the sub-loop. If through the entire iteration the flag was not change, we can infer the function is monotonic and add it to a pre-designated list named _monotonic_functions_. This list is what the function will return eventually. 


## Results of the code <br/>
All the monotonic functions are saved as items of the list _monotonic_functions_. We can see that the resulting functions in the list each corresponds to one of the 18 rows in the table:<br/>
![image](https://github.com/user-attachments/assets/5aeb5d59-124c-4a4d-8edb-47ad750598ca) <br/>
[0, 0, 1, 0, 0, 0, 0, 0, 0] – row 0<br/>
[0, 0, 1, 0, 0, 1, 0, 0, 0] – row 2<br/>
[0, 0, 1, 0, 0, 1, 0, 0, 1] – row 4<br/>
[0, 1, 1, 0, 0, 0, 0, 0, 0] – row 1<br/>
[0, 1, 1, 0, 0, 1, 0, 0, 0] – row 3<br/>
[0, 1, 1, 0, 0, 1, 0, 0, 1] – row 5<br/>
[0, 1, 1, 0, 1, 1, 0, 0, 0] – row 6<br/>
[0, 1, 1, 0, 1, 1, 0, 0, 1] – row 7<br/>
[0, 1, 1, 0, 1, 1, 0, 1, 1] – row 8<br/>
[1, 1, 1, 0, 0, 0, 0, 0, 0] – row 9<br/>
[1, 1, 1, 0, 0, 1, 0, 0, 0] – row 10<br/>
[1, 1, 1, 0, 0, 1, 0, 0, 1] – row 13<br/>
[1, 1, 1, 0, 1, 1, 0, 0, 0] – row 11<br/>
[1, 1, 1, 0, 1, 1, 0, 0, 1] – row 14<br/>
[1, 1, 1, 0, 1, 1, 0, 1, 1] – row 16<br/>
[1, 1, 1, 1, 1, 1, 0, 0, 0] – row 12<br/>
[1, 1, 1, 1, 1, 1, 0, 0, 1] – row 15<br/>
[1, 1, 1, 1, 1, 1, 0, 1, 1] – row 17<br/>
