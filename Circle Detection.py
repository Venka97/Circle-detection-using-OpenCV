{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "import cv2\n",
    "import numpy as np\n",
    "\n",
    "def count_circle(image):\n",
    "   \n",
    "    params = cv2.SimpleBlobDetector_Params()\n",
    "   \n",
    "    params.filterByCircularity = True\n",
    "   \n",
    "    params.minCircularity = 0.5\n",
    "    \n",
    "    params.filterByArea = True\n",
    "    params.maxArea = 700\n",
    "    \n",
    "    params.filterByInertia = True\n",
    "    \n",
    "    params.minInertiaRatio = 0.01\n",
    "    \n",
    "    detector = cv2.SimpleBlobDetector(params)\n",
    "   \n",
    "    keypoint = detector.detect(image)\n",
    "   \n",
    "    blank = np.zeros((1,1))\n",
    "   \n",
    "    blobs = cv2.drawKeypoints(image, keypoint, blank, (0,255,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)\n",
    "   \n",
    "    number_of_blobs = len(keypoint)\n",
    "   \n",
    "    text = \"Number of circular blobs\" + str(len(keypoint))\n",
    "   \n",
    "    cv2.putText(image, text, (20, 550), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2)\n",
    "   \n",
    "    return blobs\n",
    "\n",
    "cap = cv2.VideoCapture(0)\n",
    "while True:\n",
    "    ret,frame = cap.read()\n",
    "    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)\n",
    "    cv2.imshow(\"image\",count_circle(frame))\n",
    "    if cv2.waitKey(1)& 0xFF == ord('q'):\n",
    "        break\n",
    "   \n",
    "cap.release()\n",
    "cv2.destroyAllWindows()"
   ]
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python [conda root]",
   "language": "python",
   "name": "conda-root-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
