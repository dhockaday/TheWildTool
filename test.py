from TheWildTool.WorkData import GenerateDataset

gen = GenerateDataset()
gen.dataset_name = 'SEXOOOOOOOO'
gen.save_route = r'C:\Users\ferdh\Downloads\datatest'
gen.audio_quality = 4
gen.youtube('https://www.youtube.com/playlist?list=PLOYDNc5FY_0q8i9a7akJRjU8g6LWZ2kZh', delete_original=True, video_mode = False)








# from TheWildTool.WorkData import VideoExtract

# extract = VideoExtract()
# extract.add_to_queue([r'C:\Users\ferdh\Downloads\datatest\MyDataset\0.mp4'])
# # print(extract.converter_queue)

# extract.to_audio(remove_original = False, audio_fps=6)





# import os
# a =os.path.normpath(r'C:\Users\ferdh\Downloads\datatest\MyDataset/0.mp4')
# print(a)