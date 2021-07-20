from chardet.universaldetector import UniversalDetector
class directory():
    def __init__(self):
        pass

    def determine_codec(self, file_path):
        # check the encoding of the file
        file_encode = None
        detector = UniversalDetector()
        rawdata = open(file_path, 'rb')
        for line in rawdata:
            # line = bytes(line,"utf-8")
            detector.feed(line)
            if detector.done:
                break
        detector.close()
        rawdata.close()
        file_encode = detector.result  # export the data
        return file_encode