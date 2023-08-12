# Hand Interaction Lines
<p align="justify">
Hand interaction with lines using OpenCV and Mediapipe. The script captures video from the webcam, detects hands, and allows users to interact with virtual lines on the screen using their hand gestures.
</p>

"lines_two_hands.py"
<p align="center">
  <img src="README-images\two-hands.png" alt="StepLast">
</p>

<p align="justify">
And working with only one hand "lines.py"
</p>

<p align="center">
  <img src="README-images\lines_hand_red.PNG" alt="StepLast">
</p>

<p align="center">
  <img src="README-images\line_hand_green.PNG" alt="StepLast">
</p>

<p align="center">
  <img src="README-images\line-hand-left-green.PNG" alt="StepLast">
</p>


----
With Two hands and  one rectangle  "detect.py"

<p align="center">
  <img src="README-images\two_hands_rectangle.png" alt="StepLast">
</p>

<p align="center">
  <img src="README-images\hand_yellow.PNG" alt="StepLast">
</p>


Explication 

```python
if rect_x < x < rect_x + rect_width and rect_y < y < rect_y + rect_height:
```

<p align="justify">
Here we are checking if the point of the finger is inside the special square. We are doing this by comparing the positions of the dot and the positions of the square.

If the number "x" of the finger point is greater than the number "x" of the beginning of the square (that is rect_x) and is less than the number "x" of the end of the square (that is rect_x + rect_width), and If the number "y" of the point of the finger is greater than the number "y" of the top of the square (that is rect_y) and is less than the number "y" of the bottom of the square (that is rect_y + rect_height), then we know that the finger is touching that special square.
</p>


## Options Steps to implement it

1. Use Dockerfile 
2. Use virtual enviroments and apply  requirements.txt 
```python

conda create -n my_env python=3.11.4

pip install -r requirements.txt
```