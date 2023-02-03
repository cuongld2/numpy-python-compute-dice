import numpy as np
import cv2 


def convert_rle(mat):
    if np.sum(mat) == 0:
        return [mat.shape[0] * mat.shape[1]]
    pixels = mat.flatten()
    pixels = np.concatenate([[0], pixels, [0]])
    runs = np.where(pixels[1:] != pixels[:-1])[0]
    final_el = len(pixels) - 2 - runs[-1]
    # print(runs.shape)
    runs_new = runs.copy()
    runs_new[1::2] = runs[1::2] - runs[::2]
    runs_new[::2][1:] = runs[::2][1:] - runs[1::2][:-1]
    runs_new = np.append(runs_new, final_el)
    # print(runs_new.sum(), 512*512)
    # runs_new[1::2][]
    # runs[1::2] -= runs[::2]
    # return ' '.join(str(x) for x in runs_new)
    return runs_new.tolist()


ground_truth = cv2.imread("Ground/liver_GT_164.png", 0)
rle_output = convert_rle(ground_truth)
print(rle_output)