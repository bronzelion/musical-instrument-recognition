import itertools
import os
import sys
import tempfile

from yaafelib import AudioFileProcessor, Engine, FeaturePlan

from ..settings import BASE_DIR


def extract_feature(name):
    # 1 -flute 2-guitar 3- violin 4-piano
    ins = "3"  # Choose a dummy label
    fp = FeaturePlan(sample_rate=44100, normalize=None, resample=True)

    fp.addFeature(
        "flat:SpectralFlatness FFTLength=0  FFTWindow=Hanning  blockSize=1024  stepSize=512"
    )
    fp.addFeature(
        "flux:SpectralFlux FFTLength=0  FFTWindow=Hanning  FluxSupport=All  blockSize=1024  stepSize=512"
    )
    fp.addFeature(
        "roll:SpectralRolloff FFTLength=0  FFTWindow=Hanning  blockSize=1024  stepSize=512"
    )
    fp.addFeature(
        "sss: SpectralShapeStatistics FFTLength=0  FFTWindow=Hanning  blockSize=1024  stepSize=512"
    )

    df = fp.getDataFlow()
    df.display()
    engine = Engine()
    engine.load(df)
    directory = os.getenv("MIR_UPLOAD_DIR", "uploads")

    ins = "1"

    f = tempfile.NamedTemporaryFile("w+", suffix="testinput.csv", delete=False)

    afp = AudioFileProcessor()
    names = os.path.join(directory, str(name))
    afp.processFile(engine, os.path.join(BASE_DIR, names))

    feats = engine.readAllOutputs()
    zipped = zip(feats["flat"], feats["flux"], feats["roll"], feats["sss"])
    list(zipped)

    for i in zipped:
        for _, j in enumerate(i):
            for k in j:
                f.write(str(k) + ",")
        f.write(ins)
        f.write("\n")

    f.close()

    return zipped, f.name
