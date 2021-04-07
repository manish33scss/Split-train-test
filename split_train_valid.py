import os
import random
import shutil
import time

names = []
label = []
src= r"L:\valid"
os.chdir(src)

for root, dirs, files in os.walk(src):
    for filename in files:
        if filename.endswith("jpg"):
            names.append(filename)
    for filename in files:
        if filename.endswith("txt"):
            label.append(filename)

def chkdirec():
    if not os.path.isdir('valid'):
        os.mkdir("valid")
        v_data_p = os.path.join(src, "valid")
        time.sleep(1)
        print('directory is created')
    if not os.path.isdir("train"):
        os.mkdir("train")
        time.sleep(1)
        t_data_p = os.path.join(src, "train")
    else:
        print("Directories exist")
        
    return v_data_p,t_data_p

def copyFiles(clip , path):
    for file in clip:
        shutil.copy(file, path)

random.shuffle(names)

#find 80 percent of lr

train_no = int(len(names) * .81)
training_set = []
valid_set = []

training_set = names[: train_no].copy()

del names[:train_no]
valid_set  = names.copy()

#copy images and txt in different folders

vdata_p, tdata_p = chkdirec()

#vdata_p = r"L:\valid\valid"  #drop the path of valid and train folders that just created. 
#tdata_p = r"L:\valid\train"

copyFiles(valid_set, vdata_p )
copyFiles(training_set , tdata_p)

label_valid = []
label_train = [] 


for file in valid_set:
    label_valid.append(file.replace(".jpg" , ".txt"))
for file in training_set:
    label_train.append(file.replace(".jpg" , ".txt"))

copyFiles(label_valid, vdata_p)
copyFiles(label_train, tdata_p)

#for file in valid_set:
#    label_valid = []
#    label_valid.append(file.replace(".jpg" , ".txt"))


# TEST CODES

#train_data = "Train_set"
#valid_data = "Valid_set"

#path1 = os.path.join(src, train_data)
#path2 = os.path.join(src, valid_data)



#if not os.path.isdir('valid'):
#    os.mkdir('valid')
    

#mode = 0o666

#os.mkdir(path1,mode)
#os.mkdir(path2,mode)