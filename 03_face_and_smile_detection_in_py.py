import cv2

# Haar cascade : it is a machine learning based approach where a cascade function is trained
# from a lot of positive and negative images. 
# It is used to detect objects in other images.

# including the haar cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smil.xml')

# For each subsequent face detected, need to check for smiles
def detect(gray, frame):
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), ((x+w), (y+h)), (255, 0, 0), 2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]
		smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)

		for (sx, sy, sw, sh) in smiles:
			cv2.rectangle(roi_color, (sx, sy), ((sx+sw), (sy+sh)), (0, 0, 225), 2)
	return frame

# 1. Capture video_capture frame by frame
video_capture = cv2.VideoCapture(0)
while True:
	_, frame = video_capture.read()

	# 2. Capture image in monochrome
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# 3. Calls the detect() function
	canvas = detect(gray, frame)

	# 4. Display the result on camera feed
	cv2.imshow('Video', canvas)

	# 5. The control breaks once q key is pressed
	if cv2.waitKey(1) & 0xff == ord('q'):
		break

# Release the capture once all the processing is done.
video_capture.release()
cv2.destroyAllWindows()