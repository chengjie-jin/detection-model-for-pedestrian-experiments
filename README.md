# Detection model for pedestrian experiments 

## Brief introduction

This model is based on the model of [Keras-yolov3](https://github.com/qqwweee/keras-yolo3). In order to detect the red and blue caps in various pedestrian flow experiments, we train the model with the help of [LabelImg](https://github.com/tzutalin/labelImg). The current model could be helpful for extracting pedestrians’ positions from experimental video.

---

## Quick Start

It is very easy to use with cmd:
```
python yolo_video.py --image
```
which is exactly the same as in Keras-yolov3. It is possible that you may see lots of warnings, but they do not matter. 
Then input the name of the image, and you can get two results:

The first one is “_result.jpg”, which clearly shows the detection results of our model. Here is an example when 175 people are in the experiment (we use circular road):
![](https://github.com/chengjie-jin/detection-model-for-pedestrian-experiments/blob/master/fig1_result.jpg)

The second one is “_result.csv”, which saves the positions of detected pedestrians. The first column shows the colors (red or blue). The second column shows the probabilities, which are not written on the image. The other four columns are the data of bounding boxes. If you want to use the center positions of these pedestrians, just calculate the averaged values of column 3,5 and column 4,6. 

If you want to end this program, just input ```exit``` when you are asked to input the file name.

PS: We offer an even easier way to run it in Windows: just double-click the file named ```yolo_simple.py```! The results are the same. 

### Some notes

1. In this program, the labels (including the probabilities) are not shown on the image. If we really show them, the results under high-density condition will be quite bad, as below:
![](https://github.com/chengjie-jin/detection-model-for-pedestrian-experiments/blob/master/fig2_result.jpg)

Nevertheless, such situation could be produced if you delete “#” in lines 166-170 of yolo.py. These lines are used to show the labels. 

2. The current values are Score=0.5, IOU=0.4. If you want to change the values, just edit line 27 and 28 of yolo.py (the default values of class YOLO()).

3. The current setting is that in one image, for one type, the maximum value for detecting objects is 200. It is a hyper parameter of Yolo v3 (The default value in Keras-yolov3 is 20, which is not clearly mentioned in the documents). We think 200 is enough for most pedestrian flow experiments. If you really have more caps in one experiment, you should edit two files: <br>
(1) For training: “max_boxes” in line 36 of /yolo3/utils.py, the default values of get_random_data(). <br>
(2) For testing: “max_boxes” in line 191 of /yolo3/model.py, the default values of yolo_eval().

4. The current model could only detect the red and blue caps, since the two colors are frequently used in pedestrian flow experiments. If you want to detect the pedestrians with caps of other colors, just train the Yolo v3 model by yourself. 

PS: if you can read Chinese, the following links may be very helpful for you to train the model! <br>
https://blog.csdn.net/u012746060/article/details/81183006 <br>
https://blog.csdn.net/weixin_45488478/article/details/98397947 <br>

5. The current model only detects the positions of pedestrians. In the future, we will try to track their trajectories, and make this model more useful.

PS: We have published some papers about the pedestrian flow experiments recorded by UAV, and I think they are very interesting and useful. You can read them if you have interests: <br>

Microscopic events under high-density condition in uni-directional pedestrian flow experiment <br>
https://www.sciencedirect.com/science/article/pii/S0378437118304667 <br>
Single-file pedestrian flow experiments under high-density conditions <br>
https://www.sciencedirect.com/science/article/pii/S0378437119309744

In the future, more papers will be presented.
