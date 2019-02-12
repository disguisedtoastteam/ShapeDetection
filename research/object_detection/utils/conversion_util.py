def parseDetection(prediction):
  detection = {}
  detection["box"] = parseBox(prediction[0])
  detection["score"] = float(prediction[1])
  if prediction[2] == 2.0 :
    detection["class"] = float(3.0)
  else:
    detection["class"] = float(prediction[2])

  return detection

def parseBox(box):
  serBox = {}
  serBox["ymin"] = box[0]
  serBox["xmin"] = box[1]
  serBox["ymax"] = box[2]
  serBox["xmax"] = box[3]

  return serBox