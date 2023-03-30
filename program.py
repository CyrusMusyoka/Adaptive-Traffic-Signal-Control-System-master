f = open("out.txt", "r")
no_of_vehicles=[]
no_of_vehicles.append(int(f.readline()))
no_of_vehicles.append(int(f.readline()))
no_of_vehicles.append(int(f.readline()))
no_of_vehicles.append(int(f.readline()))

baseTimer = 120  # baseTimer = int(input("Enter the base timer value"))
timeLimits = [5, 30]  # timeLimits = list(map(int,input("Enter the time limits ").split()))

print("Input no of vehicles : ", *no_of_vehicles)
t = [(i / sum(no_of_vehicles)) * baseTimer if timeLimits[0] < (i / sum(no_of_vehicles)) * baseTimer < timeLimits[1] 
else min(timeLimits, key=lambda x: abs(x - (i / sum(no_of_vehicles)) * baseTimer)) for i in no_of_vehicles]

print(t, sum(t))

#This is a Python script that counts the number of vehicles in a video using YOLOv3 object detection and centroid tracking.

#The script loads a YOLOv3 model trained on the COCO dataset, creates a CentroidTracker object to track objects across frames, and initializes some variables such as the confidence level of a detection and the number of frames to skip between detections. It then opens a video file and begins looping through each frame of the video.

#For each frame, the script runs object detection on the frame using the YOLOv3 model and filters the detections to only include those for vehicles (bicycles, cars, motorbikes, buses, and trucks). It then feeds the filtered detections into the CentroidTracker object, which updates the object's track ID and centroid position based on the object's motion between frames.

#The script also draws a bounding box around each detected vehicle and a circle at the centroid position of each tracked object. Finally, it outputs the total number of vehicles counted in the video.





