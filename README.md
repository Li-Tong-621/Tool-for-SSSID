# Tool-for-SSSID
Tools, codes and collections for self supervised single image denoising.

Self-supervised single image denoising refers to training a denoising model using only a single image. It is also known as test-time training or zero-shot image denoising.

## 🚀 News

- 2025.3 The first version of the repo is uploaded. 🤩
- 2025.3 We release the dataset and evaluation for SSSID. 💝

If you find this repo useful, please give it a star ⭐ and consider citing our paper in your research. Thank you.

## ⏳ Todo lists
- [ ] We will follow the recent methods and supplement it. 
- [ ] We will release our reproduced code for methods that didn't release the offical code.

## 1. ☁️ Dataset

-  The widely used datasets for self supervised single image denoising task is CC, PolyU, FMDD and SIDD.
-  You can download CC, PolyU and FMDD from [DMID code](https://github.com/Li-Tong-621/DMID/releases/tag/v1.0)
-  You can download SIDD from [SIDD website](https://abdokamel.github.io/sidd/) 




## 2. 🌊 Evaluation

The widely used datasets for self supervised single image denoising task is PSNR and SSIM.


<hr />

>**Explaination:**：

>*DMID used the PSNR and SSIM calculation methods from Restormer, which is widely used in supervied image denoising methods. However,  after the publication of DMID, we found that this SSIM calculation method tends to overestimate SSIM values, making it inconsistent with previous self supervised single image denoising methods.*

>*Positive2Negative fixed this problem and used the PSNR and SSIM calculation method from DnCNN, which is consistent with other self supervised single image denoising methods.*
<hr />

-  🔨 To calculate metrics, we provied the correct [code](https://github.com/Li-Tong-621/Tool-for-SSSID/cal_metrics.py), which you should change the data path.



## 3. 🎉 Code and collection

| Name | Year | Publiaction | Code | Notes |
|-|-|-|-|-|
|Positive2Negative| 2025|CVPR |[official code](https://github.com/Li-Tong-621/P2N/)|opend before 3.25， temporally is private. |
|DMID| 2024|TPAMI |[official code](https://github.com/Li-Tong-621/DMID/)|-|
|MASH|2024| CVPR|[official code](https://github.com/hamadichihaoui/mash)| You can also directly download our reproduced images from [here].|
|ZS-N2N| 2023 |CVPR |[official code](https://colab.research.google.com/drive/1i82nyizTdszyHkaHBuKPbWnTzao8HF9b) or [our reproduced code](https://github.com/Li-Tong-621/ZS-N2N)| The official code is notebook, which is not very user-friendly. We have provided a more user-friendly version. We also offer the results images by ZS-N2N.|
|ScoreDVI| 2023| ICCV |[official code](https://github.com/alwaysuu/ScoreDVI/)| You can also directly download our reproduced images from [here].|
|R2R| 2021| CVPR |[official code](https://github.com/PangTongyao/Recorrupted-to-Recorrupted-Unsupervised-Deep-Learning-for-Image-Denoising/) or [our reproduced code](https://github.com/Li-Tong-621/R2R)| The official code did not provide the real-wolrd image denoising part, so we reproduced the code for real-wolrd image denoising according to the original paper.|
|Self2Self| 2020 |CVPR |[official code](https://github.com/scut-mingqinchen/self2self/)|-|


## 4. 🔨 Possible tools

-  🔨 As sidd benchmark has been changed to validated on kaggle, here we provide a [tool](https://github.com/Li-Tong-621/Tool-for-SSSID/edit/main/SIDD_Benchmark_rewrite.py) to transfer the SIDD bench png format to submitted csv format. You should modify the path, and run:
```
python SIDD_Benchmark_rewrite.py
```
  

## 🌹 Citation


```
@inproceedings{DMID,
  title = {Stimulating the Diffusion Model for Image Denoising via Adaptive Embedding and Ensembling},
  author = {Li, Tong and Feng, Hansen and Wang, Lizhi and Xiong, Zhiwei and Huang, Hua},
  booktitle = {IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)},
  pages = {8240-8257},
  year = {2024},
}
```


```
@inproceedings{P2N,
  title = {Positive2Negative: Breaking the Information-Lossy Barrier in Self-Supervised Single Image Denoising},
  author = {Li, Tong and Wang, Lizhi and Xu, Zhiyuan and Zhu, Lin and Lu, Wanxuan and Huang, Hua},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  pages = {1-11},
  year = {2025},
}
```

```
@misc{SSSID,
  title = {Tools, codes and collections for self supervised single image denoising},
  author = {Li, Tong},
  howpublished = {\url{https://github.com/Li-Tong-621/Tool-for-SSSID}},
  year = {2025}
}
```
