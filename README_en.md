[简体中文](README.md) | English

## Introduction

![License](https://img.shields.io/badge/License-Apache%202-red.svg)
![python version](https://img.shields.io/badge/Python-3.8+-blue.svg)
![support os](https://img.shields.io/badge/OS-Windows/macOS/Linux-green.svg)

video-subtitle-extractor aims at extracting hard-coded subtitles and generating **srt** file.  It includes the following 
implementations:

- detect and extract subtitle frames (and keyframes using traditional graphic method)
- detect subtitle areas (i.e., coordinates) (as well as scene text if you want) (using deep learning algorithms)
- recognise the content of subtitles (i.e., converting graphic text into plain-text) (using deep learning algorithms)
- filter non-subtitle text
- remove duplicated subtitle line
- generate srt file
- multiple language support: **Chinese/English(中文/英文)**, **Traditional Chinese(繁体中文)**, **Japanese(日语)**, **Korean(韩语)**, **French(法语)**, **German(德语)**
- multiple mode:
  - **fast(快速)**: high extraction speed while few subtitle missing
  - **accurate(精准)**: no subtitle missing while low extraction speed

**Download**：

- Windows GPU version：<a href="https://github.com/YaoFANGUK/video-subtitle-extractor/releases/download/0.2.0/vse_windows_GPU.7z">vse_windows_GPU.7z</a>

- Windows CPU version：<a href="https://github.com/YaoFANGUK/video-subtitle-extractor/releases/download/0.2.0/vse_windows_CPU.zip">vse_windows_CPU.zip</a>

- MacOS：<a href="https://github.com/YaoFANGUK/video-subtitle-extractor/releases/download/0.1.0/vse_macOS_CPU.dmg">vse_macOS_CPU.dmg</a>

## Features

- You don't need to do any preprocessing to get an ideal result.
- This is an offline project. You don't need to make any API call from Internet service provider in order to get results. 
- For Command Line Interface(CLI) version, you don't need to manually set the location of subtitle. This program will automatically detect the subtitle area for you.
- GPU support is available. You can install CUDA and cuDNN to speed up the detection and recognition process and even get more accurate results.

<img src="https://z3.ax1x.com/2021/04/09/cNrA1A.png" alt="demo">

> **Provide your suggestions to improve this project in ISSUES**


## Demo

- Graphic User Interface (GUI):

<p style="text-align:center;"><img src="design/demo.gif" alt="demo.gif"/></p>


- Command Line Interface (CLI): 

[![Demo Video](https://s1.ax1x.com/2020/10/05/0JWVeJ.png)](https://www.bilibili.com/video/BV1t5411h78J "Demo Video")


## Running Online

- **Google Colab Notebook with free GPU**: <a href="https://colab.research.google.com/github/YaoFANGUK/video-subtitle-extractor/blob/main/google_colab_en.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a>

> PS: can only run CLI version on Google Colab


## Getting Started 

#### 1. Download and Install Anaconda 

<a href="https://www.anaconda.com/products/individual">https://www.anaconda.com/products/individual#Downloads</a>

#### 2. Create and activate a conda virtual environment

```shell
conda create --name videoEnv python=3.8
```

```shell
conda activate videoEnv  
```

#### 3. Install dependencies via pip

make sure you have python 3.8 installed

- For macOS users and users who have CPU only:: 

  - Install dependencies：

    ```shell
    pip install -r requirements.txt
    ```

- For users who have Nvidia graphic card： **GPU version can achieve better accuracy**

  - Install **CUDA 11.2** and **cuDNN 8.1.1**

    <details>
        <summary>Linux</summary>
        <h5>(1) Download CUDA 11.2</h5>
        <pre><code>wget https://developer.download.nvidia.com/compute/cuda/11.2.0/local_installers/cuda_11.2.0_460.27.04_linux.run</code></pre>
        <h5>(2) Install CUDA 11.2</h5>
        <pre><code>sudo sh cuda_11.2.0_460.27.04_linux.run --override</code></pre>
        <p>1. Input accept</p>
        <img src="https://z3.ax1x.com/2021/05/24/gv0AVU.png" width="500" alt="">
        <p>2. make sure CUDA Toolkit 11.2 is chosen (If you have already installed driver, do not select Driver)</p>
        <img src="https://z3.ax1x.com/2021/10/11/5VnwfH.png" width="500" alt="">
        <p>3. Add environment variables</p>
        <p>add the following content in  <strong>~/.bashrc</strong></p>
        <pre><code># CUDA
    export PATH=/usr/local/cuda-11.2/bin${PATH:+:${PATH}}
    export LD_LIBRARY_PATH=/usr/local/cuda-11.2/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}</code></pre>
        <p>Make sure it works</p>
        <pre><code>source ~/.bashrc</code></pre>
        <h5>(3) Download cuDNN 8.1.1</h5>
        <p><a href="https://github.com/YaoFANGUK/video-subtitle-extractor/releases/download/0.2.0/cudnn-11.2-linux-x64-v8.1.1.33.tgz">cudnn-11.2-linux-x64-v8.1.1.33.tgz</a></p>
        <h5>(4) Install cuDNN 8.1.1</h5>
        <pre><code> tar -zxvf cudnn-11.2-linux-x64-v8.1.1.33.tgz
     sudo cp ./cuda/include/* /usr/local/cuda-11.2/include/
     sudo cp ./cuda/lib64/* /usr/local/cuda-11.2/lib64/
     sudo chmod a+r /usr/local/cuda-11.2/lib64/*
     sudo chmod a+r /usr/local/cuda-11.2/include/*</code></pre>
    </details>

    <details>
        <summary>Windows</summary>
        <h5>(1) Download CUDA 11.2</h5>
        <a href="https://developer.download.nvidia.com/compute/cuda/11.2.0/local_installers/cuda_11.2.0_460.89_win10.exe">cuda_11.2.0_460.89_win10.exe</a>
        <h5>(2) Install CUDA 11.2</h5>
        <h5>(3) Download cuDNN 8.1.1</h5>
        <p><a href="https://github.com/YaoFANGUK/video-subtitle-extractor/releases/download/0.2.0/cudnn-11.2-windows-x64-v8.1.1.33.zip">cudnn-11.2-windows-x64-v8.1.1.33.zip</a></p>
        <h5>(4) Install cuDNN 8.1.1</h5>
        <p>
           unzip "cudnn-11.2-windows-x64-v8.1.1.33.zip", then move all files in "bin, include, lib" in cuda 
    directory to C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2\
        </p>
    </details>
 


  - Install paddlepaddle:

    ```shell
    conda install paddlepaddle-gpu==2.1.3 cudatoolkit=11.2 -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/Paddle/ -c conda-forge 
    ```

    > If you installed cuda 10.2，please install cuDNN 7.6.5 instead of cuDNN v8.x

  - Install other dependencies:

    ```shell
    pip install -r requirements_gpu.txt
    ```


#### 4. Running the program

- Run GUI version

```shell
python gui.py
```

- Run CLI version

```shell    
python main.py
```

## Q & A

- For Windows users, if you encounter errors related to "geos_c.dll"

```text
    _lgeos = CDLL(os.path.join(sys.prefix, 'Library', 'bin', 'geos_c.dll'))
  File "C:\Users\Flavi\anaconda3\envs\subEnv\lib\ctypes\__init__.py", line 364, in __init__
    self._handle = _dlopen(self._name, mode)
OSError: [WinError 126] The specified module could not be found。
```

Solution：

1) Uninstall Shapely

```shell
pip uninstall Shapely -y
```

2) Reinstall Shapely via conda (make sure you have anaconda or miniconda installed)

```shell
conda install Shapely             
```

