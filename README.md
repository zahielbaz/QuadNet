# QuadNet
My deep nueral network for quadcopter control

The main file ControlGen includes 3 functions:
  1. net()- Setting up the coding net and the control net, one time use.
  2. coder- recives the coding net (Resnet50) and set of images to decode (dimention: [num of images, 476, 633, 3], type: numpy array) and outputs a [num of images] set of coded images.
  3. control- recives set of 3 timestamp sequences of coded images (numpy array with dimentions [num of sets,timestamp=3,coding lenth=2048]) , and outputs a list:
  out[0]= numpy array of estimated position: [pos_x,pos_y,pos_z,rot_y]
  out[1]= numpy array of estimated control: [out_pitch, out_roll, out_throttle, out_yaw]
  
  When live testing, any image should be coded, then 3 coded consecutive images should be concatenated in order to estimate control output of the last one.
