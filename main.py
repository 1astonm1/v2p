import cv2
import os
import easygui as esg
import math

frameFrequency = 10     # 每隔多少帧读取一次图片
path_1 = esg.fileopenbox(msg='视频', title='视频路径选择', default='*', filetypes='.avi', multiple=False)
path_2 = esg.diropenbox(msg='图片', title='图片保存路径选择', default='*')
cap = cv2.VideoCapture(path_1)   # 读入视频文件

frame_num = cap.get(7)
fill_num = int(math.log10(frame_num))+1     # 读取视频总帧数
count = 0   # 总帧数计数
output_count = 0 # 输出帧数计数
rval=cap.isOpened()
#  timeF = 1  #视频帧计数间隔频率

while rval:   # 循环读取视频帧
    count = count + 1
    print("picture:"+str(count).zfill(fill_num))
    rval, frame = cap.read()
    if rval:
        if (count%frameFrequency) ==0:
            output_count = output_count +1
           # cv2.imwrite(path_2+'/'+path_1[-42:-4]+'_'+str(count).zfill(fill_num) + '.jpg', frame)
            cv2.imwrite(path_2 + '/' + str(output_count).zfill(fill_num) + '.jpg', frame)
            cv2.waitKey(1)
        # img为当前目录下新建的文件夹
        # cv2.imwrite('E:/Recorder_2019-04-08_17-32-42/image/'+
        # 'ME630_408_Recorder_2019-04-08_17-32-42_'+str(c) + '.jpg', frame) #存储为图像
    else:
        break
cap.release()
