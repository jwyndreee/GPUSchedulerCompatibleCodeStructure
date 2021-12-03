# GPUSchedulerCompatibleCodeStructure

Follow the instruction of [https://github.com/fjxmlzn/GPUTaskScheduler](https://github.com/fjxmlzn/GPUTaskScheduler) to install the GPUTaskScheduler

The code setup in this repo enables using both **main.py** for original training as you have done before, and **main_scheduler.py** for scheduled training.

Read the comments in each file carefully, and adapt the code structure to your own code.

Just as before, you can run
```bash
CUDA_VISIBLE_DEVICES=0 python main.py --arg1 a --arg2 b
```
or, you can run multiple sequential experiments using
```bash
python main_scheduler.py
```
