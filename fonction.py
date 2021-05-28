def analyse(frame):
    x,y=-1,-1
    flag = False

    frame = imutils.resize(frame, width=tailleImage)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, orangeLower, orangeUpper)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)

        if radius > 10:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            flag = True
        else:
            radius = -1
            x = -1
            y = -1
            flag = False
    else:
        # u=os.system('clear')
        # print("PAS DE flag")
        radius = -1
        x = -1
        y = -1
        flag = False

    return  flag,(x,y),frame,mask