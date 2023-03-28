import os, shutil


def clear_file(dir):
    if dir != 'Compress_file':
        raise Exception("Illegal File Path.")

    for filename in dir:
        fullpath = os.path.join(dir, filename)
        if os.path.isdir(fullpath):
            os.unlink(fullpath)


def Compress(directory):
    clear_file("Compress_file")

    for image in os.listdir(directory):
        fullpath = os.path.join(directory, image)
        name = "compressed_" + os.path.splitext(os.path.basename(image))[0]
        save_name = f"Compress_file//{name}.jp2"
        command = f"opj_compress.exe -i {fullpath} -o {save_name} -r 16 -I"
        os.system(command)

