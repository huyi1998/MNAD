import os, shutil, glob

sourcefile = 'anomaly_data/factory/frames/training'
# new_file=str(glob.glob(os.path.join(sourcefile,'*.txt')))
Txt = glob.glob(os.path.join(sourcefile, '*.jpg'))
for file_path in Txt:
    new_dir = (file_path.split('_')[:5])[0]+'_'+(file_path.split('_')[:5])[1] + '_' + (file_path.split('_')[:5])[2] + '_' + (file_path.split('_')[:5])[3]
    try:
        os.makedirs(new_dir)
    except:
        pass

    if new_dir in file_path:
        shutil.move(file_path, new_dir)
        continue