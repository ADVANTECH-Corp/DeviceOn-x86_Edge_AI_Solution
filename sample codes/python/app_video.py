import cv2
import os
# Imports for prediction
from predict import initialize, predict_image, predict_url


def video_play(file_path):
    cap = cv2.VideoCapture(file_path)
    
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    videoWrite = cv2.VideoWriter("docker_video.avi", fourcc, 30, (1920, 1080))
    
    color = (255, 153, 255)
    while True:
        ret, frame = cap.read()
        h, w, _ = frame.shape
        if ret:
            results = predicter(frame)
            for obj in results["predictions"]:
                if obj["probability"] <= 0.2:
                    continue
                    
                tagName = obj["tagName"]
                left = int(obj["boundingBox"]["left"] * w)
                top = int(obj["boundingBox"]["top"] * h)
                right = int(obj["boundingBox"]["width"] * w) + left
                button = int(obj["boundingBox"]["height"] * h) + top
            
                color = tag_color(tagName)
                cv2.rectangle(frame, (left, top), (right, button), color, 2)
                cv2.putText(frame, tagName, (left, top), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 1, cv2.LINE_AA)
            
            videoWrite.write(frame)
            
            cv2.imshow("Result", frame)
            if cv2.waitKey(1) == ord('q'):
                break
    
    cap.release()    
    cv2.destroyAllWindows()    
    videoWrite.release()

def tag_color(tag_name):
    if tag_name == "Foam":
        return (255, 153, 255)
    
    if tag_name == "hand_1" or tag_name == "hand_2" or tag_name == "hand_3":
        return (255, 0, 0)

    if tag_name == "People":
        return (255, 0, 255)

    if tag_name == "hat":
        return (255, 128, 0)
    
    return (1, 190, 200)   

def predicter(imageData):
    try:
        initialize()
        results = predict_image(imageData)
        return results
    except Exception as e:
        print('EXCEPTION:', str(e))


if __name__ == "__main__":
    print("Start")
    file_path = "../advan/Factory_A_with_mosaic.mp4"
    #file_path = "Factory_A_with_mosaic.mp4"
    video_play(file_path)


