### Musical Instrument Recognition
An attempt to detect musical instrument, given an audio clip.

### Usage
The project comes with a `Dockerfile` which bases off the [Yaafe] library(Yet another audio feature extractor)

The container kickstarts a basic Django app accesible at http://localhost:8000/upload

`docker build -t mir . ; docker run -it -p 8000:8000 mir`

#### Note
This is a WIP project and currently uses python2.7, but there isn't any need for it untill the `libsvm` migrations can take place or be replaced with any other SVM libraries out there.

[Yaafe]: https://github.com/Yaafe/Yaafe