import json
import numpy as np


def rle_to_mat(rle_array, inner_shape):
    mat = []
    for inner_id, val in enumerate(rle_array):
        val = int(val)
        mat.extend([inner_id % 2] * val)
        print(mat)
    mat = np.array(mat)
    mat_shape = mat.shape
    print(mat_shape)
    mat = mat.reshape(inner_shape)
    return mat


def compute_dice(mask1, mask2):
    intersect = np.sum(mask1*mask2)
    fsum = np.sum(mask1)
    ssum = np.sum(mask2)
    dice = (2 * intersect ) / (fsum + ssum + 1e-5)
    dice = np.mean(dice)
    dice = round(dice, 3) # for easy reading
    return dice


if __name__ == "__main__":
    with open("ret.json", 'r') as f:
        output = json.load(f)

    shape = [512, 512]
    arr1 = output['result'][0]['data']['mask']

    mask = rle_to_mat(arr1, shape)
    file = open("mat1.txt", "w")
    file.write(str(mask))
    rle2 = []
    file1 = open('array2.txt', 'r')
    Lines = file1.readlines()

    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        # print("Line{}: {}".format(count, line.strip()))
        rle2.append(line.strip())

    mask2 = rle_to_mat(rle2, shape)
    file = open("mat2.txt", "w")
    file.write(str(mask2))

    output = compute_dice(mask, mask2)

    print(output)