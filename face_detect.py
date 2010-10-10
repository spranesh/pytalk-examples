#!/usr/bin/python


import sys, os
from opencv.cv import *
from opencv.highgui import *
import optparse


def GetOptions():
    usage = "usage: %prog [options] input-image"
    parser = optparse.OptionParser(usage)

    parser.add_option("-w"
                     ,"--write"
                     ,action="store"
                     ,type="str"
                     ,default=""
                     ,dest="output_filename"
                     ,help="write resulting to file")

    (options, args) = parser.parse_args(args=None, values=None)

    if len(args) != 1:
      print "Error parsing options"
      print usage
      sys.exit(1)

    return (args[0], options.output_filename)


def DetectObject(image):
  grayscale = cvCreateImage(cvSize(image.width, image.height), 8, 1)
  cvCvtColor(image, grayscale, CV_BGR2GRAY)
  storage = cvCreateMemStorage(0)
  cvClearMemStorage(storage)
  cvEqualizeHist(grayscale, grayscale)
  cascade = cvLoadHaarClassifierCascade('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml',
                                        cvSize(1,1))
  faces = cvHaarDetectObjects(grayscale, cascade, storage, 1.2, 2, 
                              CV_HAAR_DO_CANNY_PRUNING, cvSize(100,100))
  
  print faces
  if faces:
    for face in faces:
      cvRectangle(image, cvPoint( int(face.x), int(face.y)), cvPoint(int(face.x+face.width), int(face.y+face.height)), CV_RGB(0,255,0), 3, 8, 0)
  return
  

def DisplayObject(image):
  cvNamedWindow("face", 1)
  cvShowImage("face", image)
  cvWaitKey(0)
  cvDestroyWindow("face")

  
def main():
  (input_filename, output_filename) = GetOptions()
  if input_filename == "-":
    os.system("v4lctl snap jpeg 640x480 /tmp/face.jpg")
    input_filename = "/tmp/face.jpg"

  image = cvLoadImage(input_filename)
  DetectObject(image)
  DisplayObject(image)

  if output_filename != "":
    cvSaveImage(output_filename, image)

if __name__ == "__main__":
  main()
