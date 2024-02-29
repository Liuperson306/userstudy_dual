from moviepy.editor import *
import os

file = open(fr"filenames.txt", "r", encoding='utf-8') 
file_list = file.readlines()
file.close()

for file in file_list:
    # 去掉每行末尾的换行符
    file = file.strip()

    # 加载两个视频文件
    video1 = VideoFileClip(f"dual/{file}")
    video2 = VideoFileClip(f"single/{file}")

    # # 确保视频时长相同
    # min_duration = min(video1.duration, video2.duration)
    # video1 = video1.set_duration(min_duration)
    # video2 = video2.set_duration(min_duration)

    # 合并两个视频
    final_clip = clips_array([[video1, video2]])

    # 保存最终合并后的视频
    final_clip.write_videofile(f"video/{file}")
