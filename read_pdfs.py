import os
from pdf2image import convert_from_path

def pdf2imag(path):
    try:
        # Read all the pdfs in the provided path
        pdf_paths = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.pdf')]
        for one in pdf_paths:
            # Convert pdf to images
            images = convert_from_path(one)

            # get the pdf filename for the path
            file_name = os.path.basename(one)
            file_name = os.path.splitext(file_name)[0] + '/'
            # prepare output path
            output_path = os.path.join("./images", file_name)

            # make dir if not exist already
            if not os.path.exists(output_path):
                os.makedirs(output_path, exist_ok = True)

            # Save the images int the output  dir
            for i in range(len(images)):
                images[i].save(output_path + 'page_' + str(i) + '.jpg', 'JPEG')

    except Exception as e:
        print(e)
    else:
        print("sucess")


def main():
    path = str(input("Enter pdf path: "))
    pdf2imag(path)


if __name__ == "__main__":
    main()
