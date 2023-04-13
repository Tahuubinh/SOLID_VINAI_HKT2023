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

### System requirements

* Python 3.10 (recommended)
* [Microsoft Visual C++ 14.0 or greater is required](https://visualstudio.microsoft.com/visual-cpp-build-tools/) to install LAVIS

### Components

* LAVIS and ViT-GPT2: generating captions for image
* [riffusion](https://github.com/riffusion/riffusion): generating music based on text prompt (caption + genre + mood)
* ChatGPT: recommending music based on text prompt (caption + genre + mood)

### Installing

Install Microsoft Visual C++ 14.0 or greater is required for LAVIS: https://stackoverflow.com/questions/64261546/how-to-solve-error-microsoft-visual-c-14-0-or-greater-is-required-when-inst

* Run the following code to install the dependencies:

```
pip install -r requirements.txt
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
This project is done on the occasion of VinAI Hackathon Working Retreat 2023.
