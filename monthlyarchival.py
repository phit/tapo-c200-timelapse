from datetime import date, timedelta
from distutils.dir_util import copy_tree, remove_tree
from distutils.file_util import copy_file
import os

import timelapseconfig

lastmonth = (date.today().replace(day=1) - timedelta(days=1)).strftime(timelapseconfig.monthly_filename_date_formatstring)
currentmonth = (date.today().replace(day=1)).strftime(timelapseconfig.monthly_filename_date_formatstring)

if os.path.isfile(timelapseconfig.output_dir_for_monthly_timelapse_videos + lastmonth + '_short.mp4') and os.path.isfile(timelapseconfig.output_dir_for_monthly_timelapse_videos + lastmonth + '_fulldays.mp4'):
    for dir in os.listdir(timelapseconfig.output_dir):
        if dir.startswith(lastmonth):
            remove_tree(timelapseconfig.output_dir + dir)
            print('removed: ' + dir)

for file in os.listdir(timelapseconfig.output_dir_for_monthly_timelapse_videos):
    if not os.path.isfile(timelapseconfig.archival_dir + file):
        copy_file(timelapseconfig.output_dir_for_monthly_timelapse_videos + file, timelapseconfig.archival_dir + file)
        print('copied: ' + file)

for file in os.listdir(timelapseconfig.output_dir_for_daily_timelapse_videos):
    if not os.path.isfile(timelapseconfig.archival_dir + file):
        copy_file(timelapseconfig.output_dir_for_daily_timelapse_videos + file, timelapseconfig.archival_dir + file)
        print('copied: ' + file)
    if not file.startswith(currentmonth) and os.path.isfile(timelapseconfig.archival_dir + file) and os.path.getsize(timelapseconfig.archival_dir + file) == os.path.getsize(timelapseconfig.output_dir_for_daily_timelapse_videos + file):
        os.remove(timelapseconfig.output_dir_for_daily_timelapse_videos + file)
        print('deleted: ' + file)
