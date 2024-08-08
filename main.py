import cv2

def by_size():
    width = int(input("Enter Width: "))
    height = int(input("Enter Height:"))
    return (width,height)

try:
    path = cv2.imread(input("Enter the path of your image: "),cv2.IMREAD_UNCHANGED)
    name = input("Give it a name with extension: ")
    choice = int(input("Chose the option by number:\n1)By Size\n2)By %age\n"))
    if choice == 1:
       size = by_size()
    else:
        scale = int(input("Enter the resize percentage: "))
        height = int(path.shape[0] * scale /100)
        width = int(path.shape[1] * scale /100)
        size = (width,height)

    result_image = cv2.resize(path,size)

    cv2.imshow("Output",result_image)
    cv2.waitKey(0)
    cv2.imwrite(name,result_image)
except:
    print("Error!")

