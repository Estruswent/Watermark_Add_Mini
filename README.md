# Watermark_Add_Mini

## 芝士什么？

这是手搓的一个简单python程序，主要是单次实现为相机拍摄的照片添加水印，水印会包含的信息有：
- 照片的拍摄时间
- 照相机的品牌
- 光圈大小、焦段、快门速度、感光度等

## 食用方法？

- 方案一：直接运行源码

  - 下载python_program文件夹，运行`generate.py`会出现一个弹窗，点击`Select Image`按钮，**先选择你需要添加水印的照片**，**接下来选择加水印的照片的导出位置即可**。
  - 下载font文件夹，安装字体。

- 方案二：使用可执行程序

  - 下载executable_program_windows文件夹，双击运行`generate.exe`，会出现一个弹窗，点击`Select Image`按钮，**选择你需要添加水印的照片**，**接着选择导出位置即可**。
  - 下载font文件夹，安装字体。

> 放了一些相机品牌的透明底logo的png格式图片在camera_logo文件夹里（手机自带的相机暂时不太支持），目前收录品牌有：
> 
>  - Canon
>  - Nikon
>  - Sony
>  - Panasonic
>  - FUJIFILM 
> 
> 如果您的相机品牌暂未收录，您可以先查看相机拍摄的图片的元数据，了解到相机品牌名字后，**向camera_logo文件夹内导入透明底的相机品牌的png格式图片**，**并将该图片命名为相机品牌的名字**

## 仓库结构？

- 文件夹executable_program_windows内部放有windows系统直接可以使用的可执行程序，其中：
  - `generate.exe`打开后会直接生成弹窗选择照片，接着选择导出位置即可。
  - _internal文件夹是`generate.exe`所需的一些依赖。
  - camera_logo文件夹主要放了一些常见的相机品牌的透明底logo的png格式图片。

- 文件夹python_program内部放有python源码，其中：
  - `generate.py`是生成带水印图片的程序源码，屎山代码写得很简单，~~可能有很多bug，大佬轻喷~~，它使用了python的一些库。
    1. `exifread`库主要实现读取元数据。
    2. `pillow`库主要实现绘制水印。
    3. `os`库主要实现一些文件路径的操作。
    4. `datetime`库主要实现时间的读取。
  - camera_logo文件夹主要放了一些常见的相机品牌的透明底logo的png格式图片。

- `README.md`是这个项目的说明文档，也是你正在读的东西。

- `LICENSE`是这个项目的证书，我选了个MIT证书。

## 后续考虑？

- 也许会出批量处理的程序？这段小代码是几个小时手搓的，bug啥的估计不少，功能也不全。
- 同时可能会考虑加入相机型号信息等其他细节。
