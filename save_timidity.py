import csv
import subprocess
from glob import glob
import os 
import sys
import shutil
import time

def timidity(mid, wav):
    subprocess.call(["/root/share/TiMidity++-2.15.0/timidity/timidity", mid, "-Ow", "-o", wav])

def main(dirname=None):
    # get filenames   
    # parent_path = '/home/rsy/Documents/mid2wav'
    parent_path = 'C:/Users/claire.rhyu/Documents'

    file_types = ["*.mid", "*.midi"]
    files_grabbed = list()
    for file_type in file_types:
        files_grabbed.extend(glob(os.path.join(parent_path, dirname, file_type)))
    mids = sorted(files_grabbed)

    mid_dir = os.path.join(parent_path, dirname, "mid")
    if not os.path.exists(mid_dir):
        os.makedirs(mid_dir)
    new_dir = os.path.join(parent_path, dirname, "wav")
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    for mid in mids:
        midname = '.'.join(os.path.basename(mid).split('.')[:-1])
        wav = os.path.join(new_dir, "{}.wav".format(midname))
        # convert to wav
        os.chdir(os.path.dirname(mid))
        timidity(mid, wav)
        shutil.move(mid, os.path.join(mid_dir, os.path.basename(mid)))
        print()
        print('     >> saved wav file for {}.mid'.format(midname))
        print()
    print()

def convert_to_wav(mid=None, time_in_name=True, return_wavname=False):

    cwd = os.getcwd()
    dirname = os.path.dirname(mid)
    midname = '.'.join(os.path.basename(mid).split('.')[:-1])
    if time_in_name:
        time_ = time.time()
    else:
        time_ = time.strftime('%Y%m%d_%I%M%S', time.localtime(time.time()))
    wav = os.path.join(dirname, "{}.{}.wav".format(midname, time_))
    # convert to wav
    os.chdir(dirname)
    timidity(mid, wav)
    os.chdir(cwd)

    if return_wavname is True:
        return wav 



if __name__ == "__main__":

    dirname = sys.argv[1]
    main(dirname=dirname)