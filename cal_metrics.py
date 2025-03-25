import glob
import PIL
import torch
import numpy as np
import cv2
from natsort import natsorted
import os 
#################SSIM和其他的自监督降噪一致。
from utils_image import calculate_psnr, calculate_ssim
import sys
import lpips

loss_fn = lpips.LPIPS(net='alex', version='0.1').to('cuda')

def cal_metric(path='',noisepath=''):

    paths_clean =natsorted(glob.glob(path+'/*')) 
    paths_denoise =natsorted(glob.glob(noisepath+'/*')) 

    avg_rgb_psnr=[]
    avg_rgb_ssim=[]
    avg_rgb_lpips = []
    
    for i in range(len(paths_clean)):
        clean_one=cv2.imread(paths_clean[i])
        denoise_one=cv2.imread(paths_denoise[i])

        if 'FMDD' in paths_clean[i]:
            clean_one=cv2.imread(paths_clean[i], cv2.IMREAD_GRAYSCALE)
            denoise_one=cv2.imread(paths_denoise[i], cv2.IMREAD_GRAYSCALE)

        current_psnr =calculate_psnr(denoise_one, clean_one,border=0)
        avg_rgb_psnr.append(current_psnr)
        current_ssim = calculate_ssim(denoise_one,clean_one,border=0)
        avg_rgb_ssim.append(current_ssim)
        avg_rgb_lpips.append(loss_fn(lpips.im2tensor(lpips.load_image(paths_clean[i])).to('cuda'),lpips.im2tensor(lpips.load_image(paths_denoise[i])).to('cuda')).to('cpu').detach().item())
  
    return np.mean(avg_rgb_psnr),np.mean(avg_rgb_ssim),np.mean(avg_rgb_lpips)

        
avg_psnr, avg_ssim, avg_lpips=cal_metric(path='./P2N/PolyU/RDC+DSC-sigma0.75-L1.5/photo_ema/',
            noisepath='./Dataset/benchmark/PolyU/PolyU_png/')
print('&{:.2f} / {:.4f}  / {:.3f}'.format(avg_psnr, avg_ssim, avg_lpips))
    
