import PIL as pillow
from PIL import Image
from PIL import ImageOps
import sys

def main():
    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    input_filename = sys.argv[1]
    if input_filename[input_filename.rfind("."):].lower() in (".jpg",".jpeg",".png"):
        pass
    else:
        sys.exit("Invalid input")
    output_filename = sys.argv[2]
    if output_filename[output_filename.rfind("."):].lower() in (".jpg",".jpeg",".png"):
        pass
    else:
        sys.exit("Invalid output")
    if output_filename[output_filename.rfind("."):].lower() != input_filename[input_filename.rfind("."):].lower():
        sys.exit("Input and output have different extensions")

    input_to_output(input_filename,output_filename)

def input_to_output(input_filename,output_filename):
    try:
        shirt_img=Image.open("shirt.png")
        muppet_before_img=Image.open(input_filename)
    except FileNotFoundError:
        sys.exit("Input does not exist")
    else:
        muppet_before_img=ImageOps.fit(muppet_before_img,shirt_img.size)
        muppet_before_img.paste(shirt_img,(0,0),mask=shirt_img)
        muppet_before_img.save(output_filename)


if __name__=="__main__":
    main()
