# Tool-for-SSSID
Tools and code for self supervised single image denoising.

## 🚀 News

- 2025.3 The first version of the repo is uploaded. :star:
- 2025.3 We release the dataset and evaluation for SSSID. :gift_heart:

If you find this repo useful, please give it a star ⭐ and consider citing our paper in your research. Thank you.

## ⏳ Todo lists
- [ ] We will follow the recent methods and supplement it. 
- [ ] We will release our reproduced code for methods that didn't release the offical code.

## 1. :cloud: Dataset

The widely used datasets for self supervised single image denoising task is CC, PolyU, FMDD and SIDD.

CC, PolyU and FMDD can directly download from [DMID code]([https://github.com/Li-Tong-621/DMID/releases/tag/v1.0](https://github.com/Li-Tong-621/DMID/releases/tag/v1.0)  

## 2. :ocean: Evaluation

The widely used datasets for self supervised single image denoising task is PSNR and SSIM.

DMID used the PSNR and SSIM calculation methods from Restormer, which is widely used in supervied image denoising methods. However,  after the publication of DMID, we found that this SSIM calculation method tends to overestimate SSIM values, making it inconsistent with previous self supervised single image denoising methods.

Positive2Negative fixed this problem and used the PSNR and SSIM calculation method from DnCNN, which is consistent with other self supervised single image denoising methods.

