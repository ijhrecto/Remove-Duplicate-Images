from PIL import Image
import imagehash, os
import argparse

def remove_images(path, all_files, files_retain):
    for file in all_files:
        if file not in files_retain:
            os.remove(os.path.join(path, file))
    print("\nRemoved Duplicate Files!!!\n")

def get_unique_files(files, hashes):
    # compare each hashes then list out the duplicate files to be removed
    unique_hash = []
    unique_file = []
    for idx, (file, hash) in enumerate(zip(files, hashes)):
        # if new hash append to list
        if hash not in unique_hash:
            unique_hash.append(hash)
            unique_file.append(file)
            # print("Unique Image: ", hash, " : ", file )

        print(f"Comparing Image Hashes: {idx+1} / {len(files)}") # progress counts
    print("\nComparing Hashes Complete!!!\n")
    return unique_file

def create_hashes(path, remove_fail):
    # get list of files
    img_ls = os.listdir(path)
    # convert images into hashes
    hash_ls = []; fname_ls = []; c = 0 
    for idx, img in enumerate(img_ls):
        filename = os.path.join(path, img)
        
        # if image failed to load, go to next file
        try:
            ih = imagehash.phash(Image.open(filename))
        except:
            if remove_fail:
                c += 1 # add to subtract to the total number of list
                os.remove(filename) 
            continue

        print(f"{idx} / {len(img_ls)-c} = {img} : {ih}")
        fname_ls.append(filename)
        hash_ls.append(ih)

    print(f"\nTotal Unsuccessful Images = {c}")
    print("Image Hashes Created!!!\n")
    return fname_ls, hash_ls

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p","--path", default=os.getcwd(), type=str, help="directory of the images")
    parser.add_argument("-r","--remove_fail", default=True, type=bool, help="remove image if it can not be read, (True or False)")
    args = parser.parse_args()

    # change the folder location
    # have all your photos be in one folder
    # img_folder = "images"
    # path = os.path.join(os.getcwd(), img_folder)
    path = args.path
    remove_fail = args.remove_fail

    # creates hashes using percetion hashing
    # yields the file list and their respective hashes
    # remove_fail, deletes files which are not able to be read by PIL
    files, hashes = create_hashes(path, remove_fail)

    # returns unique files based on hashes
    # disregards subsequent hashes/file if hash already exists
    unique_files = get_unique_files(files, hashes)

    # needs path, list of all files, and uniques files not to be removed
    remove_images(path, files, unique_files)


if __name__ == "__main__":
    main()



    