# CUDA

Install latest version of **CUDA** that matches major version of your **PyTorch**  
For example, CUDA 11.8 can be used with PyTorch compiled for CUDA 11.7, but CUDA 12.0 *cannot*

- <https://developer.nvidia.com/cuda-downloads>

Install latest version of **cuDNN** compatible with chosen CUDA version

- <https://developer.nvidia.com/rdp/cudnn-download>

Currently best options are **CUDA 11.8** with **cuDNN 8.7**  
Note that **CUDA 12** is not yet supported by PyTorch  

## PyTorch

*Note*: Uninstall `torch` and `triton` before attempting any new installs

> pip uninstall torch torchvision torchaudio triton -y

### Stable

**PyTorch 2.0.0** compiled with **CUDA 11.8**:

> pip install torch torchaudio torchvision triton --force --extra-index-url https://download.pytorch.org/whl/cu118  
> pip show torch  
> 2.0.0

### Nighly

**PyTorch 2.1-nightly** compiled with **CUDA 11.8**:

> pip install --pre torch triton torchvision torchaudio --force --extra-index-url https://download.pytorch.org/whl/nightly/cu118  
> pip show torch  
> 2.1.0.dev20230305+cu118

### From source

Read <https://github.com/pytorch/pytorch#from-source>  
Note: **PyTorch** heavily relies on **Anaconda** for its build process

### Monkey-patching

Torch comes with its own version of `cuDNN` which is great for simplicity,  
but not so great if your performance is 50% of what's expected  

First make sure that your `cuDNN` is installed correctly and in `ldconfig` can find it  
Then, remove `cuDNN` from `torch` package:

> rm ~/.local/lib/python3.10/site-packages/torch/lib/libcudnn*

Now check if correct `cuDNN` libraries are found
> sudo ldconfig
> ldconfig -p | grep cudnn

And if not, modify `LD_LIBRARY_PATH` to include `cuDNN` libraries and repeat `ldconfig` command

> export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib64

## SDP cross-attention optimization  

Recommended if you are using **PyTorch 2.0**  

## Xformers cross-attention optimization

`xformers` is a library of optimized attention kernels for PyTorch  
Highly recommended for significant performance boost when using `Pytorch` **1.x**  
Not required when using `Pytorch` **2.0**  

### Stable

When using release version of **PyTorch 1.13.1**, simply install `xformers` from `PyPI`:

> pip install -U xformers

### From Source

Otherwise, build process takes a bit longer...

Set your environment so `xformers` can be optimized for *your* GPU

> python -c 'import torch; print(torch.cuda.get_device_capability())'
> (8, 6)
> export TORCH_CUDA_ARCH_LIST="8.6"

Rebuild `xformers`

> sudo apt install pybind11-dev
> pip install ninja setuptools pybind11 
> pip install -v -U git+https://github.com/facebookresearch/xformers.git@main#egg=xformers  

This will compile `xformers` for your system which is preferred over using pre-built wheel

Check functionality using:

> python -m xformers.info

Make sure that all fields marked with `memory_efficient` are set to `available`  

## Triton

### Stable

There are separate `torchtriton` and `triton` packages as well as different sources for `triton`
To avoid confusion, uninstall any existing `triton` packages before installing `torch` and install `triton` in the same install command as `torch`

### From Source

Default version of `triton` package is good-enough for a fully functional system  
unless you want to further experiment with torch `dynamo` just-in-time compiler,  
in which case you may need to build & install <https://github.com/openai/triton> package from source

## Accelerate

Recommended to run in **FP16** mode with **Dynamo** accelerators  
But...**Dynamo** is only supported with **Torch 2.0**!
Otherwise, run without **Dynamo**

> pip install accelerate
> accelerate config

    In which compute environment are you running? This machine
    Which type of machine are you using? No distributed training
    Do you want to run your training on CPU only (even if a GPU is available)? [yes/NO]: no
    Do you wish to optimize your script with torch dynamo?[yes/NO]: yes
    Which dynamo backend would you like to use? inductor <- only if using torch 2.0+, otherwise no
    Do you want to use DeepSpeed? [yes/NO]: no
    What GPU(s) (by id) should be used for training on this machine as a comma-seperated list? [all]: all
    Do you wish to use FP16 or BF16 (mixed precision)? fp16

> accelerate test

## Python

PyTorch is **NOT** compatible with Python 3.11, use 3.10 instead

Just install as usual, but also possible to build from sources

### Build

You can install `python` itself from sources

Download from <https://www.python.org/downloads/source/>

Configure:
> export CFLAGS="-march=native -O3 -pipe -Wno-unused-value -Wno-empty-body -DNDEBUG"  
> ./configure --prefix /usr --enable-optimizations --with-lto --enable-loadable-sqlite-extensions  
> time make -j32  

Check: 
> ./python --version  
> ./python -c 'import sysconfig; print(sysconfig.get_config_var("PY_CFLAGS"))'  

Do side-by-side install:
> sudo make altinstall  
> sudo update-alternatives --install /bin/python3 python3 /bin/python3.11 100  
> sudo update-alternatives --list python3  

Switch to new `python`:

> sudo update-alternatives --config python3  
> python -m pip install --upgrade pip  
> python -m pip uninstall torch torchaudio triton pytorch_triton -y
> python -m pip install --pre torch triton torchaudio torchvision --extra-index-url https://download.pytorch.org/whl/nightly/cu118 --force  
> python -c 'import torch; print(torch.__path__, torch.__version__)'  

# nVidia CUDA

## Windows WSL2

Requirements:
- Latest versions of Windows: not included in RTM  
  Note: Insider builds are no longer required as CUDA support is present in Beta builds  
- Updated WSL kernel: `wsl --update`, minimum **4.19.121** recommended **5.15.74**  
- Updated nVidia drivers: minimum **460** recommended **510**  

Links:
- [nVidia install docs](https://docs.nvidia.com/cuda/wsl-user-guide/index.html)
- [Ubuntu install docs](https://ubuntu.com/blog/getting-started-with-cuda-on-ubuntu-on-wsl-2)
- [CUDA download](https://developer.nvidia.com/cuda-downloads)

## Install

Install both `CUDA` and `cuDNN`  
- Note: Do not install drivers if running in VM, let host drivers be as-is  

Driver can be higher than runtime, but not opposite  
- Example: driver 510 supports Cuda 12 and is compatible with Cuda 11.6)

Install using either:
- Add nVidia repository and install using `apt`
- Download installer and install manually  

## Check

Is CUDA detected and versions:

> apt list cuda*

List is long, but minimum packages are:

    cuda/now 11.6.1-1
    cuda-11-6/now 11.6.1-1
    cuda-cccl-11-6/now 11.6.55-1
    cuda-command-line-tools-11-6/now 11.6.1-1
    cuda-compiler-11-6/now 11.6.1-1
    cuda-cudart-11-6/now 11.6.55-1
    cuda-cupti-11-6/now 11.6.112-1
    cuda-libraries-11-6/now 11.6.1-1
    cuda-nvcc-11-6/now 11.6.112-1
    cuda-runtime-11-6/now 11.6.1-1
    cuda-toolkit-11-6/now 11.6.1-1
    cuda-tools-11-6/now 11.6.1-1

> apt list libcudnn*

    libcudnn8/now 8.3.2.44-1+cuda11.5

> nvidia-smi  

    NVIDIA-SMI 510.85.02 Driver Version: 526.98 CUDA Version: 12.0

> head /usr/local/cuda/version.json  

    "cuda" : {
      "name" : "CUDA SDK",
      "version" : "11.6.1"
    },

## NVCC

Test:

> git clone https://github.com/NVIDIA/cuda-samples

Edit `Makefile` as needed to specify compute level and run `make`

> Samples/1_Utilities/deviceQuery

    Device 0: "NVIDIA GeForce RTX 3060"
      CUDA Driver Version / Runtime Version          12.0 / 11.6
      CUDA Capability Major/Minor version number:    8.6
      Total amount of global memory:                 12288 MBytes (12884377600 bytes)
      (028) Multiprocessors, (128) CUDA Cores/MP:    3584 CUDA Cores
      GPU Max Clock rate:                            1777 MHz (1.78 GHz)
      Memory Clock rate:                             7501 Mhz
      Memory Bus Width:                              192-bit
      ...

## Stable Diffusion

Stable-Diffusion requires `CUDA` level **SM86** so version older than 11 are insufficient

## TensorFlow

Install:

> pip3 install tensorflow  

Tensorflow dynamically links to CUDA libraries, so as long as major version matches, it should work (e.g. Tensorflow 2.10 uses CUDA 11.x).
But mixing different major versions between Tensorflow and CUDA does not work

Check:  

> wget https://raw.githubusercontent.com/vladmandic/tfjs-utils/main/src/tfinfo.py  
> python src/tfinfo.py

    sysconfig: [
      ('cpu_compiler', '/dt9/usr/bin/gcc'),
      ('cuda_compute_capabilities', ['sm_35', 'sm_50', 'sm_60', 'sm_70', 'sm_75', 'compute_80']),
      ('cuda_version', '11.2'),
      ('cudnn_version', '8'),
      ('is_cuda_build', True),
      ('is_rocm_build', False),
      ('is_tensorrt_build', True)
    ]
    gpu device: PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU') {
      'compute_capability': (8, 6),
      'device_name': 'NVIDIA GeForce RTX 3060'
    }
    logical device: LogicalDevice(name='/device:GPU:0', device_type='GPU')

## PyTorch

Install **PyTorch** linked to *exact* major/minor version of **CUDA**:

> pip3 uninstall torch torchvision torchaudio  
> pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116  

Note that `cu116` at the end refers to `CUDA` **11.6** which should match `CUDA` installation on your system  

Check:  

> wget https://raw.githubusercontent.com/vladmandic/tfjs-utils/main/src/torchinfo.py
> python torchinfo.py  

    torch version: 1.12.1+cu116
    cuda available: True
    cuda version: 11.6
    cuda arch list: ['sm_37', 'sm_50', 'sm_60', 'sm_70', 'sm_75', 'sm_80', 'sm_86']
    device: NVIDIA GeForce RTX 3060

## XFormers

Download

> git clone https://github.com/facebookresearch/xformers.git
> cd xformers
> git submodule update --init --recursive

Compile

> export FORCE_CUDA="1"
> export TORCH_CUDA_ARCH_LIST=8.6
> pip install ninja pyre-extensions einops
> python setup.py build develop
> python setup.py bdist_wheel

Install

> pip install dist/*
> python -m xformers.info
