### Musical Instrument Recognition
An attempt to detect a musical instrument, given an audio clip. 

Currently the app only supports four instruments at present(limited to the training data available):
* Flute
* Guitar
* Violin
* Piano


### Usage
The project comes with a `Dockerfile` which bases off the [Yaafe] library(Yet another audio feature extractor)

The container kickstarts a basic Django app accesible at http://localhost:8000

`docker build -t mir . ; docker run -it -p 8000:8000 mir`

#### TODO

This is a WIP project and currently uses python2.7, mostly due to dependencies on libsvm and Yaafe.

* Migrate to python 3 - replace libsvm with any other svm lib(eg. scikit-learn)
* Yaafe's build dependencies are non-trivial, replace this library with other audio processing libs such as [librosa] that make it easier to extract [MFCC]


[Yaafe]: https://github.com/Yaafe/Yaafe
[librosa]: https://github.com/librosa/librosa
[MFCC]: https://en.wikipedia.org/wiki/Mel-frequency_cepstrum