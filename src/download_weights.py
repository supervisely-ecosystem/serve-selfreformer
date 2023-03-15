import os
import gdown


def download_pvt_v2_b2(output="model/pretrain/pvt_v2_b2.pth"):
    if os.path.exists(output):
        return output
    os.makedirs(os.path.dirname(output), exist_ok=True)
    id = "1l5HJWXid7JETz4gxuireVXgoMjm14jEX"
    path = gdown.download(id=id, output=output)
    return path

def download_selfreformer(output="model/pretrain/best_DUTS-TE.pt"):
    if os.path.exists(output):
        return output
    os.makedirs(os.path.dirname(output), exist_ok=True)
    id = "19kO-IjZS56rIDTfscABhErTO-SP7oP4L"
    path = gdown.download(id=id, output=output)
    return path
