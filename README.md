# System Check
## Installation 
1- Clone the repo 

```git clone https://github.com/Arslanex/System-Check ```

```cd System-Check ```

2- Install requirements

```pip install -r requirements.txt```

3- OpenCV installation
There are two ways to install OpenCV package. 
- First way you can use terminal for installation. But when you install like this OpenCV will not be enable to use CUDA. 

    ```pip install opencv-python```

- Second way you can build OpenCV with Cmake 
    - For Linux :: https://qengineering.eu/install-opencv-4.5-on-jetson-nano.html (for nano)
    - For Windows ::  https://drive.google.com/file/d/1XcZ0L99fTqlRhOl56nbNvEnUkm3lfq2F/view?usp=sharing (Türkçe)


4- Run main file 

Windows:

```python __main__.py```

Linux:

```python3 __main__.py```

## Use Of the Program
When you install requirments and run the main file you will see the main menu and choices you can make in the progran. I put all the choices you can make wthin the program.

```
Main Menu
├── System Check  (Menu 1)
│   ├── Basic Info
│   ├── CPU Info
│   ├── GPU('s) Info
│   ├── RAM Info
│   ├── Memory Info
│   ├── Disk Info
│   ├── Network Info
│
├── CUDA and FPS Tests  (Menu 2)
    ├── Is OpenCV CUDA Enabled
    ├── CPU vs GPU 
    ├── FPS Tests
```

In every menu there is an option that does all the operations one after the other. 
If you want a new feature please create a issue.  

## Screen Shots
![merge_from_ofoct (1)](https://user-images.githubusercontent.com/44752389/176218085-90fd76ea-e621-499f-8bba-9e81206c8da0.jpg)




https://user-images.githubusercontent.com/44752389/176256918-f0d28f9a-e100-43fd-a7c6-fea0cf80ebea.mp4



https://user-images.githubusercontent.com/44752389/176264134-c3224b13-acd0-4976-8bcd-b6672ce70915.mp4

