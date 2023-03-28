import os


def Decompress(directory):
    for image in os.listdir(directory):
        name, extension = os.path.splitext(os.path.basename(image))
        if extension == '.jp2':
            fullpath = os.path.join(directory, image)
            name = name.split('_')[1]
            save_name = f"Decompress_file//{name}.bmp"
            command = f"opj_decompress.exe -i {fullpath} -o {save_name}"
            os.system(command)


