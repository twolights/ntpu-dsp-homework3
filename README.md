# NTPU Fall 2023 DSP Homework #3

Source code is hosted at https://github.com/twolights/ntpu-dsp-homework3

# Pre-requisites

1. Python 3.8+ (only tested on 3.8.18 though)
2. NumPy
3. matplotlib
4. virutalenv
5. pip

# Before Running the Code

1. Setup virtualenv
 ```shell
# virtualenv `which python3` env
 ```
2. Activate virtualenv
```shell
# . env/bin/activate
```
3. Install dependency packages
```shell
# pip install -r requirements.txt
```

# How to Run the Code

_All output images/CSV's will be located in the "output" directory_

* 1 & 2

```shell
# python3 main-plot.py gen
```

This will output impulse response & frequency magnitude of low-pass filter for each order M

* 3

```shell
# python3 main-wav.py
```

This will generate original & filtered WAV file and head/tail transient state graph for each order M

* 5

```shell
# python3 main-min-phase.py
```

This will generate a graph that compares the impulse response of linear and minimum phase.

* Conclusion

Please refer to the attached PDF for assignment recap
