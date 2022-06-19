import cv2
import HandDetecting
import serial

fingerTips = [8,12,16,20]

#open video camera and set the width and height
stream = cv2.VideoCapture(0)
stream.set(3,1280)
stream.set(4,720)

#create object in HandDetector class
detector = HandDetecting.HandDetector()


serialPort = serial.Serial("COM8")
while True:
    stat, img = stream.read()  # read image from stream
    img = cv2.flip(img,1)
    img,count,label = detector.drawLandmarks(img)
    print(count)

    if count == 0:
        serialPort.write('4'.encode('utf-8'))
        print("Stop")

    elif count == 2:
        cv2.putText(img, 'Both Hands Detected', (20, 50), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 255, 0), 2)
        cv2.rectangle(img, (760, 10), (1150, 70), (0, 255, 255), cv2.FILLED)
        cv2.putText(img, 'Setting: Forward/Backward', (800, 50), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 255, 0), 2)

        lmList1,label1 = detector.fingerPosition(img,hand_no=0)
        lmList2, label2 = detector.fingerPosition(img, hand_no=1)
        if label1 == "Right":
            lmList_R = lmList1
            lmList_L = lmList2

        else:
            lmList_R = lmList2
            lmList_L = lmList1

        sequence_R = []
        if len(lmList_R) != 0:
            if lmList_R[4][1] > lmList_R[3][1]:
                sequence_R.append(1)
            else:
                sequence_R.append(0)

            for tip in fingerTips:
                if lmList_R[tip][2] < lmList_R[tip - 2][2]:
                    sequence_R.append(1)
                else:
                    sequence_R.append(0)

        sequence_L = []
        if len(lmList_L) != 0:
            if lmList_L[4][1] < lmList_L[3][1]:
                sequence_L.append(1)
            else:
                sequence_L.append(0)

            for tip in fingerTips:
                if lmList_L[tip][2] < lmList_L[tip - 2][2]:
                    sequence_L.append(1)
                else:
                    sequence_L.append(0)

        value_L = sequence_L.count(1)
        value_R = sequence_L.count(1)
        if value_L+value_R >= 8:
            print("Forward")
            serialPort.write('0'.encode('utf-8'))

        if value_L+value_R <=2:
            print("Backward")
            serialPort.write('1'.encode('utf-8'))



    else:
        if label == 'Right':
            cv2.putText(img, 'Right Hand', (20, 50), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 255, 0), 2)
            cv2.rectangle(img, (760, 10), (1150, 70), (0, 255, 255), cv2.FILLED)
            cv2.putText(img, 'Setting: Turn Right', (800, 50), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 255, 0), 2)

            serialPort.write('3'.encode('utf-8'))
            print("Right")



        if label == 'Left':
            cv2.putText(img, 'Left Hand', (460, 50), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 255, 0), 2)
            cv2.rectangle(img, (760, 10), (1150, 70), (0, 255, 255), cv2.FILLED)
            cv2.putText(img, 'Setting: Turn Left', (800, 50), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 255, 0), 2)

            serialPort.write('2'.encode('utf-8'))
            print("Left")

    cv2.imshow("LIVE", img)
    cv2.waitKey(1)


