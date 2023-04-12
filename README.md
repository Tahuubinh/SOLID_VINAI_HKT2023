# SOLID - Soundtrack Of Life In Digital

Our app suggests music for an image.

## Contributors

+ Phạm Huy Tùng (Beloved leader)
+ Hồ Lai Tuân (Techie guy)
+ Tạ Hữu Bình
+ Nguyễn Ngọc Hải
+ Lê Thanh Thiên
+ Vũ Quang Trường
+ Nguyễn Văn Việt


## Getting Started

### Dependencies

* Python 3.10 (recommended)
* [LAVIS](https://github.com/salesforce/LAVIS)
* [Microsoft Visual C++ 14.0 or greater is required](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

### Installing

* You can import environment in anaconda using SOLID2.yaml (LAVIS) or Hug.yaml (VIT GPT2). VIT GPT2 seems faster with same accuracy.

* LAVIS

Install Microsoft Visual C++ 14.0 or greater is required for LAVIS: https://stackoverflow.com/questions/64261546/how-to-solve-error-microsoft-visual-c-14-0-or-greater-is-required-when-inst

Install pycocotools
```
conda install -c conda-forge pycocotools
```

Install LAVIS from PyPi
```
pip install salesforce-lavis
```

* VIT GPT2

```
pip install torch
pip install torchvision
pip install transformers
pip install pillow
```

### Executing program

* How to run the program
* Step-by-step bullets
```
streamlit run app.py
```


## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments
