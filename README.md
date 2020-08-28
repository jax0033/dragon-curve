# dragon-curve
the dragon curve fractal in python


How?
Lets say we have an array that can contain only 1 and 0. 1 turns 90° right then draws a line and 0 90° left and draws a line.
We start by appending 1 (first part), appending another 1 (divider) and then append the reverse of our first part (reversed array and 1 = 0, 0 = 1) (last part)
 = 110
 
 
If we continue doing that with our result we will get 


1


1               1 0


110             1 100


1101100         1 1100100


110110011100100 1 110110001100100


and so on. 
The result is the fractal known as the Dragon curve.
