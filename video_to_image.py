import os 
import cv2
import sys

def video_to_img(root, output_path, video_name):
    video_path = os.path.join(root,video_name)
    cap = cv2.VideoCapture(video_path)
    #out put path 
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    targetdir = os.path.join(output_path,video_name[:-4])
    #targetdir =output_path
    print('targetdir: ',targetdir)
    if not os.path.exists(targetdir):
        os.mkdir(targetdir)
    #format output name
    frame_num = cap.get(7)
    num_length = len(str(frame_num))
    ret, frame = cap.read()
    cont = 0
    while(ret):
        #cv2.imshow('frame',frame)
        img_name ='frame' + str(cont).zfill(num_length) +'.jpg'
        cont+=1
        img_path = os.path.join(targetdir,img_name)
        #print(img_path)
        cv2.imwrite(img_path,frame)
        ret, frame = cap.read()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


def get_videos(path,output):
    
    for root,dirs,files in os.walk(path):
        for _file in files:
            if _file[-3:]=='mp4':
                
                print(_file)
                #convert to img
                video_to_img(root,output,_file)
            #print(os.path.join(root,_file))
        for _dir in dirs: 
            get_videos(os.path.join(root,_dir) , os.path.join(output,_dir))


path = sys.argv[1]
output = sys.argv[2]
#path = '/home/syk/test/'
#output = '/home/syk/test/output/'
print(path)
print(output)
get_videos(path,output)
