# Image Filter pixel and ascii art


[//]: # "References"
[contact-alberto]: albgarjim1@gmail.com
[unsplash-link]: https://unsplash.com/
[image-elephant]: ./docs/images/elephant.png
[image-tiger]: ./docs/images/tiger.jpg
[image-filter-elephant]: ./docs/images/filter-elephant.png
[image-filter-tiger]: ./docs/images/filter-tiger.jpeg

<!-- description of what the project does  -->
Service to apply filters to images

## Table of Contents

- [Project title](#project-title)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Installation](#installation)
  - [Documentation](#documentation)
  - [License](#license)
  - [Contact](#contact)

## Introduction

This project contains filters to pixelate images and convert them to ascii art. The sample images used are obtained from [Unsplash][unsplash-link]


## Results

Showcase of the pixel filter:

Original         |    Filtered
:-------------------------:|:-------------------------:
![image tiger][image-tiger]  |  ![image tiger][image-filter-tiger]


Showcase of the ascii filter:

Original         |    Filtered
:-------------------------:|:-------------------------:
![image elephant][image-elephant]  |  ![image elephant][image-filter-elephant]

## Installation

Clone this repository with the command:

```sh
git clone https://github.com/albgarjim/image-filter.git
```

Navigate into the src file insidie the `image-filter` folder:

```sh
cd ./src/image-filter
```

## Usage

The 2 main functions are `filter_pixelated` and `filter_ascii` called from the `image_read` file and implemented on `libs_image_filter.py`.

- `filter_pixelated` receives a path to the image to apply the filter

- `filter_ascii` receives a path to the image aswell as 2 parameters for the scaling of the resulting image

## License

Released under MIT License


## Contact

Maintainer: [Alberto Garcia][contact-alberto]
