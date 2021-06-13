import math
import wave # https://www.youtube.com/watch?v=k0lRNdmM3jg
import struct

class SoundReader:
    def __init__(self,namefile,rateOfFire, countData):
        self.nameFile = namefile # Sound\\test.wav
        self.rof = rateOfFire
        self.data = []
        self.countData = countData

    def Calculation(self):
        if self.data != []:
            return self.data
        
        source = wave.open(self.nameFile,mode = "rb")
        frames = source.getnframes()
        
        data = source.readframes(frames)
        data = struct.unpack("<" + str(frames * 2) + "h", data)

        data = list(data)[::2]

        rate = source.getframerate()
        duration = frames / float(rate)

        newData = []
        step = int((frames / duration) * self.rof) 
        print(step)

        for i in range(0,len(data),step):
            temp = 0

            cutList = data[i:i+step]
            cutList = list(map(abs,cutList))
            stepList = int(len(cutList) / self.countData)

            cutList2 = []

            for c in range(0,self.countData):
                x = cutList[c*stepList: stepList + c * stepList]
                cutList2.append(int(sum(x)/stepList))

            newData.append(cutList2)

        print(newData)

        for i in range(0,len(newData)):
            for j in range(0,len(newData[i])):
                newData[i][j] = int((newData[i][j] * newData[i][j])/100)    
        
        self.data = newData

        return self.data

if __name__ == "__main__":
    sr = SoundReader("Sound\\test.wav",1,4)
    print(sr.Calculation())